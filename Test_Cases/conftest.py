import os
import pytest
from playwright.sync_api import sync_playwright
from pageObjects.Login_Page import Login
from Utilities.ReadProperties import ReadConfig
import psycopg2
from configparser import ConfigParser, RawConfigParser
from sshtunnel import SSHTunnelForwarder
import allure
import requests
from APIs import endpoints
from APIs.payloads import AUTH_PAYLOAD
from APIs.headers import JSON_HEADERS
from pathlib import Path

# -------------------- Utilities --------------------

# Screenshots folder ensure karo
os.makedirs("screenshots", exist_ok=True)
# print("🔑 SSH KEY PATH:", ReadConfig.get_ssh_key())
# print("🔁 SSH KEY EXISTS:", os.path.exists(ReadConfig.get_ssh_key()))


# -------------------- Playwright Fixtures --------------------

base_url = ReadConfig.getApplicationURL()
username = ReadConfig.getUserName()
password = ReadConfig.getPassword()
login_Url = ReadConfig.get_login_url()
backend_url = ReadConfig.getBackEndUrl()

# @pytest.fixture(scope="session")
# def its_id():
#     # return get_its_id()
#     its_id =int(ReadConfig.getUserName())
#     return its_id

@pytest.fixture(scope="session")
def its_id():
    """Return ITS ID from config file as integer."""
    return int(ReadConfig.getUserName())
 

@pytest.fixture(scope="module")
def setup():
    """Launch browser in full screen and provide page object"""
    with sync_playwright() as p:
        # browser = p.chromium.launch(headless=True, args=["--start-maximized"])
        browser = p.chromium.launch(headless=False, args=["--start-maximized"])
        context = browser.new_context(no_viewport=True)  # Full HD window
        page = context.new_page()
        page.evaluate("""
            () => {
                window.moveTo(0, 0);
                window.resizeTo(screen.width, screen.height);
            }
        """)
        yield page
        browser.close()


@pytest.fixture(scope="module")
def login(setup):
    """Login into the application (only once per module)"""
    page = setup
    page.goto(base_url, wait_until="load", timeout=60000)
    lp = Login(page)
    lp.setUserName(username)
    lp.setPassword(password)
    lp.login()
    with allure.step("Select Mumin role"):
        lp.click_mumin_role()
    yield page

# -------------------- Queries Fixture --------------------

# @pytest.fixture(scope="module")
# def load_queries():
#     """Load queries from queries.ini file"""
#     # parser = ConfigParser(interpolation=None)
#     parser = RawConfigParser()
#     parser.read(r"D:\Backup\ELAAM\Automation\Elaam_automation_01_12_2025\Configurations\queries.ini")
#     if "queries" not in parser.sections():
#         raise KeyError("The 'queries' section is missing in queries.ini")
#     queries = {key: value for key, value in parser.items("queries")}
#     return queries

#-----------------------Fixture for load query with dynaminc ITS_ID and relative path---------

@pytest.fixture(scope="module")
def load_queries():
    """Load queries from queries.ini file"""
    # yeh file jahan hai (jaise conftest.py)
    current_file = Path(__file__).resolve()    
    # project root = uska parent ka parent (agar conftest Tests/ ke andar hai)
    project_root = current_file.parent.parent    
    # Configurations/queries.ini ka path
    ini_path = project_root / "Configuration" / "queries.ini"
    print(f"\n[DEBUG] Using queries.ini from: {ini_path}\n")
    parser = RawConfigParser()
    parser.read(ini_path)
    if "queries" not in parser.sections():
        raise KeyError("The 'queries' section is missing in queries.ini")
    queries = {key: value for key, value in parser.items("queries")}
    return queries


# -------------------- DB Connection Fixture --------------------

@pytest.fixture(scope="module")
def db_connection(load_queries):
    """Establish DB connection via SSH tunnel"""
    # SSH details
    ssh_host = ReadConfig.get_ssh_host()
    ssh_port = int(ReadConfig.get_ssh_port())
    ssh_user = ReadConfig.get_ssh_user()
    ssh_pkey = ReadConfig.get_ssh_key()
    # DB details
    db_host = ReadConfig.get_db_host()
    db_port = int(ReadConfig.get_db_port())
    db_user = ReadConfig.get_db_user()
    db_password = ReadConfig.get_db_password()
    db_name = ReadConfig.get_db_name()
    with SSHTunnelForwarder(
        (ssh_host, ssh_port),
        ssh_username=ssh_user,
        ssh_pkey=ssh_pkey,
        remote_bind_address=(db_host, db_port)
    ) as tunnel:
        print(f"SSH tunnel established on local port {tunnel.local_bind_port}")
        connection = psycopg2.connect(
            host="127.0.0.1",  # always localhost for tunnel
            port=tunnel.local_bind_port,
            user=db_user,
            password=db_password,
            dbname=db_name
        )
        print("Database connection established")
        yield connection, load_queries
        connection.close()
        print("Database connection closed")


# -------------------- Query Execution Fixture --------------------

# @pytest.fixture
# def elaam_prod(db_connection):
#     """Fetch query results from DB by query key"""
#     connection, queries = db_connection

#     def fetch(query_key, *args):
#         query = queries.get(query_key)
#         if not query:
#             raise ValueError(f"Query '{query_key}' not found in queries.ini")
#         cursor = connection.cursor()
#         cursor.execute(query, args)  # supports parameterized queries
#         data = cursor.fetchall()
#         headers = [desc[0] for desc in cursor.description]
#         cursor.close()
#         return headers, data
#     return fetch

@pytest.fixture
def elaam_prod(db_connection):
    """Fetch query results from DB by query key."""
    connection, queries = db_connection
    def fetch(query_key, *params):
        query = queries.get(query_key)
        if not query:
            raise ValueError(f"Query '{query_key}' not found in queries.ini")
        cursor = connection.cursor()
        try:
            # 🔹 DEBUG: dekhne ke liye kya ja raha hai
            print("\n===== DB DEBUG =====")
            print("Query key :", query_key)
            print("Raw query :", query.strip())
            print("Params    :", params)
            # agar driver mogrify support karta ho (Postgres / kuch MySQL libs)
            if params and hasattr(cursor, "mogrify"):
                try:
                    final_sql = cursor.mogrify(query, params)
                    print("Final SQL :", final_sql.decode() if isinstance(final_sql, bytes) else final_sql)
                except Exception as e:
                    print("mogrify error (ignore kar sakti ho):", e)
            # 🔹 ab actual execute
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            data = cursor.fetchall()
            headers = [desc[0] for desc in cursor.description]
        finally:
            cursor.close()
        return headers, data
    return fetch



# -------------------- Screenshot on Failure (Hook) --------------------

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Har test ke baad yeh hook chalega.
    Agar test FAIL hua hai to:
    - us test ke fixture se page nikaalenge (login ya setup)
    - screenshot lenge
    - Allure report me attach karenge
    """
    outcome = yield
    result = outcome.get_result()

    # Sirf test body phase (call) aur sirf FAIL hone par
    if result.when == "call" and result.failed:
        # Jo fixture tum use kar rahi ho, usme se page nikaalo
        page = item.funcargs.get("login") or item.funcargs.get("setup")

        if page:
            screenshot_path = f"screenshots/{item.name}.png"
            page.screenshot(path=screenshot_path, full_page=True)

            allure.attach.file(
                screenshot_path,
                name="Failure Screenshot",
                attachment_type=allure.attachment_type.PNG,
            )

@pytest.fixture(scope="module")
def get_token():
    """Authenticate and return bearer token."""
    
    response = requests.post(url=endpoints.AUTHENTICATE, json=AUTH_PAYLOAD, headers=JSON_HEADERS)
    print("Token API Response Code:", response.status_code)
    # 🔴 Agar API 200 nahi de rahi, yahin test fail kara do
    if response.status_code != 200:
        print("Token API failed:", response.text)
        pytest.fail(f"Token API failed with status {response.status_code}")
    # Yahan aayega matlab status 200 hai
    data = response.json()
    token = data.get("token")    
    # Token missing ho to bhi clean failure
    if not token:
        pytest.fail("Token not found in API response")
    return token
