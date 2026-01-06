import psycopg2
from tabulate import tabulate
from tabulate import tabulate
from playwright.sync_api import sync_playwright
from Test_Cases.conftest import access_token
from Test_Cases.conftest import db_connection, fetch_data, load_queries
from Utilities.ReadProperties import ReadConfig

url = ReadConfig.get_back_end_url()
print("hfdhfgdsjgsdjfds", url)


# Database Connection Setup
def fetch_data_from_db(query, database_name="postgres"):
    try:
        # Connect to the specified PostgreSQL database (update with your credentials)
        connection = psycopg2.connect(
            dbname="fleete_new",
            user="postgres",
            password="FlEeTe@123",
            host="fleete-qa-dashboard.demoapplication.net",
            port="5432"
        )
        cursor = connection.cursor()
        cursor.execute(query)

        # Fetch column names and data
        columns = [desc[0] for desc in cursor.description]
        db_data = cursor.fetchall()

        cursor.close()
        connection.close()

        # Return both column names and data
        return columns, db_data

    except Exception as error:
        print(f"Error fetching data from DB: {error}")
        return [], []


# Main Execution
if __name__ == "__main__":
    # Specify the database name you want to connect to
    database_name = "fleete_new"
    query = "select * from user_details ud where network_id =12084;"

    # Fetch column names and data
    columns, data = fetch_data_from_db(query, database_name)

    if data:
        # Display data in table format
        print(tabulate(data, headers=columns, tablefmt="grid"))
    else:
        print("No data found.")

import pytest

#
# # Test function for fetching active users
# def test_fetch_active_users(fetch_data):
#     query_key = "fetch_active_users"
#     headers, result = fetch_data(query_key)  # Execute the "fetch_active_users" query
#     # Assuming the query result contains a single row with the count in the first column
#     active_user_count = result[0][0] if result else 0  # Store the count value
#     inactive_user_count = result[0][1] if result else 0
#     # Check if there's a count to display
#     assert active_user_count > 0, f"No active users found with query '{query_key}'"
#     # Print the count
#     print(f"Active User Count: {active_user_count}")
#     print(f"Inactive User Count: {inactive_user_count}")
#
# # Test function for fetching a user by ID
# def test_fetch_user_by_id(fetch_data):
#     query_key = "fetch_user_by_id"
#     user_id = 1  # Example user ID to pass as a parameter
#
#     headers, result = fetch_data(query_key, user_id)  # Execute "fetch_user_by_id" with an argument
#
#     assert result, f"No user found with ID {user_id} using query '{query_key}'"
#
#     print(f"Results for {query_key} with user ID {user_id}:\n")
#     print(tabulate(result, headers=headers, tablefmt="grid"))  # Use dynamic headers






def test_extract_api_data(access_token):
    with sync_playwright() as p:
        # Define headers, including Authorization
        url1 = f"{url}api/v1/getFleetsTiles"
        print("uuuuuuuuuuuu", url1)
        headers = {
            "accept": "application/json",
            "Authorization": f"{access_token}",
            "Content-Type": "application/json" }

        # Create a request context with headers
        request_context = p.request.new_context(extra_http_headers=headers)


        # Make an API request
        response = request_context.get(url=url1)
        print("RRRRRRRRRRRRR:", response)

        # Check the response status
        assert response.status == 200

        # Parse and print the JSON response to understand its structure
        response_data = response.json()
        print("The full JSON response data:", response_data)

        # Check if 'data' exists in the response and contains the expected fields
        if "data" in response_data:
            # Check for each specific key to prevent KeyErrors
            total_fleets = response_data["data"].get("totalFleets")
            nested_data = response_data["data"].get("data")

            if nested_data and isinstance(nested_data, list) and len(nested_data) > 0:
                healthy_fleets = nested_data[0].get("healthyFleets")
                impacted_fleets = nested_data[0].get("impactedFleets")

                print("Total Fleets:", total_fleets)
                print("Healthy Fleets:", healthy_fleets)
                print("Impacted Fleets:", impacted_fleets)

                # Example assertions if you want to validate values
                assert total_fleets is not None, "totalFleets not found in response"
                assert healthy_fleets is not None, "healthyFleets not found in response"
                assert impacted_fleets is not None, "impactedFleets not found in response"
            else:
                print("Nested data structure is missing or empty.")
        else:
            print("'data' key is missing in the response.")

        # Dispose of the request context
        request_context.dispose()


