import pytest
from playwright.sync_api import sync_playwright
from pageObjects.Login_Page import Login
from Utilities.ReadProperties import ReadConfig, config
import psycopg2
from configparser import ConfigParser

base_url = ReadConfig.getApplicationURL()
username = ReadConfig.getUserName()
password = ReadConfig.getPassword()
login_Url = ReadConfig.get_login_url()


@pytest.fixture(scope="module")
def setup():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False,slow_mo=1000)
        context = browser.new_context()
        page = context.new_page()
        yield page
        browser.close()

@pytest.fixture(scope="module")
def login(setup):
    # base_url = ReadConfig.getApplicationURL()
    # username = ReadConfig.getUserName()
    # password = ReadConfig.getPassword()
    page = setup
    page.goto(base_url, wait_until="load",timeout=60000)
    lp = Login(page)
    lp.setUserName(username)
    lp.setPassword(password)
    lp.login()
    yield page

# Fixture to load queries from queries.ini
@pytest.fixture(scope="module")
def load_queries():
    parser = ConfigParser()
    parser.read("D:\Playwrite\FleetAutomation_17-09-2024\Configuration\queries.ini")

    # Check if 'queries' section exists
    if 'queries' not in parser.sections():
        raise KeyError("The 'queries' section is missing in the queries.ini file.")

    # Load queries from the `[queries]` section in the ini file
    queries = {key: value for key, value in parser.items("queries")}
    return queries

# Fixture to set up database connection with loaded queries
@pytest.fixture(scope="module")
def db_connection(load_queries):
    name_db = ReadConfig.get_db_name()
    user_db = ReadConfig.get_user()
    password_db = ReadConfig.get_password()  # Corrected method name here
    host_db = ReadConfig.get_host()
    port_db = ReadConfig.get_port()
    connection = psycopg2.connect(
        dbname=name_db, user=user_db, password=password_db, host=host_db, port=port_db
    )
    yield connection, load_queries  # Yield the connection and queries as a tuple
    connection.close()

# Fixture to set up database connection with loaded queries
@pytest.fixture(scope="module")
def db_connection_transform(load_queries):

    connection = psycopg2.connect(
        dbname='fleete_transform', user="postgres", password="FlEeTe@123", host="fleete-qa-dashboard.demoapplication.net", port=5432
    )
    yield connection, load_queries  # Yield the connection and queries as a tuple
    connection.close()

# Fixture to execute a query and fetch data with headers
@pytest.fixture
def fetch_data(db_connection):
    connection, queries = db_connection  # Unpack connection and queries

    def fetch(query_key, *args):
        # Retrieve the query string using the query key
        query = queries.get(query_key)
        if query:
            cursor = connection.cursor()
            cursor.execute(query, args)  # Execute with optional parameters
            data = cursor.fetchall()     # Fetch all results
            headers = [desc[0] for desc in cursor.description]  # Get column names
            cursor.close()
            return headers, data  # Return both headers and data
        else:
            raise ValueError(f"Query '{query_key}' not found in queries.ini")

    return fetch

@pytest.fixture
def fetch_data_transform_db(db_connection_transform):
    connection, queries = db_connection_transform  # Unpack connection and queries

    def fetch(query_key, *args):
        # Retrieve the query string using the query key
        query = queries.get(query_key)
        if query:
            cursor = connection.cursor()
            cursor.execute(query, args)  # Execute with optional parameters
            data = cursor.fetchall()     # Fetch all results
            headers = [desc[0] for desc in cursor.description]  # Get column names
            cursor.close()
            return headers, data  # Return both headers and data
        else:
            raise ValueError(f"Query '{query_key}' not found in queries.ini")

    return fetch

#Fixture for getting the access token
@pytest.fixture(scope="session")
def access_token():
    with sync_playwright() as p:
        # Define the login API headers and payload
        headers = {"accept": "application/json", "Authorization": "eyJraWQiOiJpRUZmUk9DRkNiSX-gqRE7JW0CJGdpZkA", "Content-Type": "application/json" }
        login_payload = {"name": username, "password": password }
        # Create a request context
        request_context = p.request.new_context()
        # Make the login request
        login_response = request_context.post(url=login_Url, headers=headers, data=login_payload)
        # Ensure the login was successful
        assert login_response.status == 200, "Login failed"
        # Extract and return the access token
        login_data = login_response.json()
        token = login_data.get("data", {}).get("accessToken")
        assert token, "Access token not found in response"
        print("Access Token:", token)
        # Dispose the request context after use
        request_context.dispose()
        return token









