import pytest
from playwright.sync_api import sync_playwright
from pageObjects.Login_Page import Login
from Utilities.ReadProperties import ReadConfig
import psycopg2
from configparser import ConfigParser
from sshtunnel import SSHTunnelForwarder
import allure


# -------------------- Playwright Fixtures --------------------

base_url = ReadConfig.getApplicationURL()
username = ReadConfig.getUserName()
password = ReadConfig.getPassword()
login_Url = ReadConfig.get_login_url()


@pytest.fixture(scope="module")
def setup():
    """Launch browser in full screen and provide page object"""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000 )
        context = browser.new_context(
            viewport= {"width": 1366, "height": 768}  # Full HD window
        )
        page = context.new_page()
        yield page
        browser.close()


@pytest.fixture(scope="module")
def login(setup):
    """Login into the application"""
    page = setup
    page.goto(base_url, wait_until="load", timeout=60000)
    lp = Login(page)
    lp.setUserName(username)
    lp.setPassword(password)
    lp.login()
    with allure.step(""):
        lp.click_mumin_role()
    yield page

# @pytest.fixture(scope="function")
# def login_with_role(login, request):
#     """Login and select role (role comes from parametrize)"""
#     role = request.param
#     role_page = RoleSelection(login)
#     role_page.select_role(role)
#     yield login

# -------------------- Queries Fixture --------------------

@pytest.fixture(scope="module")
def load_queries():
    """Load queries from queries.ini file"""
    parser = ConfigParser()
    parser.read(r"D:\Backup\ELAAM\Automation\ELAAM_Automation_08-09-2025\Configuration\queries.ini")
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

@pytest.fixture
def elaam_prod(db_connection):
    """Fetch query results from DB by query key"""
    connection, queries = db_connection

    def fetch(query_key, *args):
        query = queries.get(query_key)
        if not query:
            raise ValueError(f"Query '{query_key}' not found in queries.ini")
        cursor = connection.cursor()
        cursor.execute(query, args)  # supports parameterized queries
        data = cursor.fetchall()
        headers = [desc[0] for desc in cursor.description]
        cursor.close()
        return headers, data
    return fetch
















