from playwright.sync_api import sync_playwright, Page
from Test_Cases.conftest import fetch_data, db_connection,load_queries, fetch_data_transform_db
from Utilities.ReadProperties import ReadConfig
from tabulate import tabulate

url = ReadConfig.get_back_end_url()


xpath_fleet_text = "//h2[normalize-space(text()) = 'fleets']"
xpath_fleets_dashboard_tiles = "//div[@class='text']"
xpath_total_fleet_count = "(//div[@class='number'])[1]"
xpath_active_fleet_count = "(//div[@class='number'])[2]"
xpath_inactive_fleet_count = "(//div[@class='number'])[3]"
xpath_vehicle_tile = "(//div[@class='agr_data_box'])[2]"
xpath_depot_tile = "(//div[@class='agr_data_box'])[3]"
xpath_charger_tile = "(//div[@class='agr_data_box'])[4]"
xpath_fleet_list_heading = "(//div[@class='MuiGrid-root MuiGrid-item MuiGrid-grid-xs-12 MuiGrid-grid-sm-8 css-1iqiv84'])[2]"
xpath_fleet_data_tiles = "//div[@class='MuiGrid-root MuiGrid-item MuiGrid-grid-xs-12 MuiGrid-grid-sm-6 MuiGrid-grid-md-6 MuiGrid-grid-lg-4 css-60bez']"
xpath_pagination= "//div[@class='MuiStack-root pagination_count css-u4p24i']"
xpath_bottom_tiles = "(//div[@class='MuiGrid-root MuiGrid-container MuiGrid-spacing-xs-2 css-isbt42'])[3]"
xpath_search_field = "//input[@class='MuiInputBase-input css-mnn31']"
xpath_first_fleet_tile = "(//h2[@class='MuiTypography-root MuiTypography-h2 MuiTypography-gutterBottom card_heading css-p08hmt'])[3]"


xpath_vehicle_breadcrumb = "//button[@data-testid='vehicles']"
xpath_vehicle_pychart = "//div[@class='tab_pie_chart']"
xpath_Energy_point = "(//div[@class='MuiCardContent-root card_content css-1qw96cp'])[1]"
xpath_charging_nfrastructure_bottom_card = "(//div[@class='MuiCardContent-root card_content css-1qw96cp'])[3]"
xpath_Energy_used = "(//div[@class='MuiCardContent-root card_content css-1qw96cp'])[4]"


class FleetDashboardPage:
    active_fleet_count_db = None
    total_fleet_tiles = None

    def __init__(self, page:Page):
        self.page = page


    def verify_fleet_dashboard_heading(self):
        expected = "FLEETS"
        fleet_text_frontend = self.page.inner_text(xpath_fleet_text)
        # Improved print message for clarity
        print(f"Verifying Fleet Dashboard Heading...\nExpected: '{expected}'\nActual: '{fleet_text_frontend}'")
        assert fleet_text_frontend == expected, \
            f"Test failed: Expected '{expected}', but the actual text was '{fleet_text_frontend}'."
        self.page.wait_for_timeout(1000)

    def verify_fleet_tiles_text(self):
        expected_tiles = {"Fleets", "Vehicles", "Depots", "Chargers"}
        tiles = self.page.locator(xpath_fleets_dashboard_tiles).all_text_contents()
        actual_tiles_set = set(tiles)    # Convert tiles to a set for comparison
        missing_tiles = expected_tiles - actual_tiles_set
        if not missing_tiles:
            print("All expected tiles are present: Fleets, Vehicles, Depots, Chargers")
        else:
            print(f"Missing tiles: {', '.join(missing_tiles)}")
            self.page.screenshot(path="./Screenshots/fleet_dashboard_tiles.png")
            raise AssertionError(f"Missing tiles: {', '.join(missing_tiles)}")

    def verify_fleet_counts_on_tile(self, fetch_data):
        self.page.wait_for_timeout(1000)
        total_fleet_count = int(self.page.inner_text(xpath_total_fleet_count).strip())
        active_fleet_count = int(self.page.inner_text(xpath_active_fleet_count).strip())
        inactive_fleet_count = int(self.page.inner_text(xpath_inactive_fleet_count).strip())
        fleet_query_key = "fleet_tile_count_query"      #Define the query key to fetch the active fleet count from the database
        # Fetch headers and result from the database using the provided query key
        headers, result = fetch_data(fleet_query_key)
        # Retrieve the active fleet count from the result; if no result, set to 0
        total_fleet_count_db = int(result[0][0] if result else 0)
        active_fleet_count_db = int(result[0][1] if result else 0)
        inactive_fleet_count_db= int(result[0][2] if result else 0)
        assert total_fleet_count_db > 0, f"No active users found with query '{fleet_query_key}'"
        assert total_fleet_count == total_fleet_count_db, f"Displayed total fleet count ({total_fleet_count}) does not match total fleet count in DB ({total_fleet_count_db})"
        assert active_fleet_count_db == active_fleet_count, f"Displayed active fleet count{active_fleet_count} does not matched active fleet count in db {active_fleet_count_db}"
        assert inactive_fleet_count_db == inactive_fleet_count, f"Displayed active fleet count{inactive_fleet_count} does not matched active fleet count in db {inactive_fleet_count_db}"
        return active_fleet_count_db

    def verify_vehicle_tile(self, fetch_data_transform_db):
        self.page.wait_for_timeout(1000)
        vehicle_expected_tile_text = ['Vehicles', 'Moving', 'Idle', 'Parked']
        vehicle_tile_text = self.page.inner_text(xpath_vehicle_tile).splitlines()   # Split the text by line breaks
         # Assign each line to a separate variable
        total_vehicles = int(vehicle_tile_text[0])  # Expected format: total count
        vehicles_text = vehicle_tile_text[1]  # Expected text: 'Vehicles text
        moving_count = int(vehicle_tile_text[2])  # Expected format: moving count
        moving_text = vehicle_tile_text[3]  # Expected text: 'Moving text'
        idle_count = int(vehicle_tile_text[4])  # Expected format: idle count
        idle_text = vehicle_tile_text[5]  # Expected text: 'Idle text'
        parked_count = int(vehicle_tile_text[6])  # Expected format: parked count
        parked_text = vehicle_tile_text[7]  # Expected text: 'Parked text'
        vehicle_tile_query = "vehicle_tile_count_query"
        headers, result = fetch_data_transform_db(vehicle_tile_query)
        print("vehicle count:", result)
        columns, data = fetch_data_transform_db(vehicle_tile_query, fetch_data_transform_db)
        print(tabulate(data, headers=columns, tablefmt="grid"))
        total_vehicle_count = int(result[0][0])
        moving_vehicle_count = int(result[0][1])
        idle_vehicle_count = int(result[0][2])
        parked_vehicle_count = int(result[0][3])

        # Assert that the captured labels and count match the expected labels
        assert vehicles_text == vehicle_expected_tile_text[
            0], f"Expected '{vehicle_expected_tile_text[0]}', but got '{vehicles_text}'"
        assert moving_text == vehicle_expected_tile_text[
            1], f"Expected '{vehicle_expected_tile_text[1]}', but got '{moving_text}'"
        assert idle_text == vehicle_expected_tile_text[
            2], f"Expected '{vehicle_expected_tile_text[2]}', but got '{idle_text}'"
        assert parked_text == vehicle_expected_tile_text[
            3], f"Expected '{vehicle_expected_tile_text[3]}', but got '{parked_text}'"
        assert total_vehicles == total_vehicle_count, f"Expected moving count '{total_vehicle_count}', but got '{total_vehicles}'"
        assert moving_count == moving_vehicle_count, f"Expected total vehicles '{moving_vehicle_count}', but got '{moving_count}'"
        assert idle_count == idle_vehicle_count, f"Expected idle count '{idle_vehicle_count}', but got '{idle_count}'"
        assert parked_count == parked_vehicle_count, f"Expected parked count '{parked_vehicle_count}', but got '{parked_count}'"
        print("All assertions passed for vehicle tile")

    def verify_depot_tile(self, fetch_data):
        self.page.wait_for_timeout(3000)
        depot_tile_text_count = self.page.inner_text(xpath_depot_tile).splitlines()
        print("Depot text & count in line:", depot_tile_text_count)
        # Extract individual components from the text
        total_depot_count = int(depot_tile_text_count[0])  # Assuming the total count is the first line
        depot_text = depot_tile_text_count[1]  # Should say "Chargers"
        upcoming_count = int(depot_tile_text_count[2])  # Count for Available
        upcoming_text = depot_tile_text_count[3]  # Should say "Available"
        decommissioned_count = int(depot_tile_text_count[4])  # Count for Busy
        decommissioned_text = depot_tile_text_count[5]  # Should say "Busy"
        commissioned_count = int(depot_tile_text_count[6])  # Count for Offline
        commissioned_text = depot_tile_text_count[7]  # Should say "Offline"
        undermaintenance_count = int(
            depot_tile_text_count[-3])  # Count for Faulty (assuming it's the third-to-last line)
        undermaintenance_text = depot_tile_text_count[-2]  # Should say "Faulty"
        # Execute SQL query to fetch data from the database
        depot_tile_query = "depot_tile_count_query"
        headers, result = fetch_data(depot_tile_query)
        # Display the database results in a tabular format
        print(tabulate(result, headers=headers, tablefmt="grid"))
        # Process database results to store counts by status
        status_counts = {row[1] if row[1] else 'Unknown': row[0] for row in result}
        total_depot_count_db = int(result[0][0])
        upcoming_count_db = int(result[0][1])
        decommissioned_count_db = int(result[0][2])
        commissioned_count_db = int(result[0][3])
        undermaintenance_count_db = int(result[0][4])

        assert total_depot_count == total_depot_count_db, f"Expected  total depot count '{total_depot_count}', but got '{total_depot_count_db}'"
        assert upcoming_count == upcoming_count_db, f"Expected upcoming count {upcoming_count}, but got {upcoming_count_db}"
        assert decommissioned_count == decommissioned_count_db, f"Expected decommissioned count {decommissioned_count}, but got {decommissioned_count_db}"
        assert commissioned_count == commissioned_count_db, f"Expected commissioned count {commissioned_count}, but got {commissioned_count_db}"
        assert undermaintenance_count == undermaintenance_count_db, f"Expected undermaintenance count {undermaintenance_count}, but got {undermaintenance_count_db}"
        print("All assertions passed successfully for depot tile")


    def verify_chargers_tile(self, fetch_data):
        self.page.wait_for_timeout(3000)
        charger_tile_text_count = self.page.inner_text(xpath_charger_tile).splitlines()   # Splitting the text by lines to extract each piece of data
        # Extract individual components from the text
        total_charger_count = int(charger_tile_text_count[0])  # Assuming the total count is the first line
        charger_text = charger_tile_text_count[1]  # Should say "Chargers"
        available_count = int(charger_tile_text_count[2])  # Count for Available
        available_text = charger_tile_text_count[3]  # Should say "Available"
        busy_count = int(charger_tile_text_count[4])  # Count for Busy
        busy_text = charger_tile_text_count[5]  # Should say "Busy"
        offline_count = int(charger_tile_text_count[6])  # Count for Offline
        offline_text = charger_tile_text_count[7]  # Should say "Offline"
        faulty_count = int(charger_tile_text_count[-3])  # Count for Faulty (assuming it's the third-to-last line)
        faulty_text = charger_tile_text_count[-2]  # Should say "Faulty"
        # Execute SQL query to fetch data from the database
        charger_tile_query = "charger_tile_count_query"
        headers, result = fetch_data(charger_tile_query)
        db_table_view= tabulate(result, headers=headers, tablefmt="grid")   # Display the database results in a tabular format
        print("DB table view: ", db_table_view)
        # Process database results to store counts by status
        status_counts = {row[1] if row[1] else 'Unknown': row[0] for row in result}
        # Retrieve individual status counts from the dictionary
        available_count_db = status_counts.get('Available', 0)
        busy_count_db = status_counts.get('Busy', 0)
        faulted_count_db = status_counts.get('Faulted', 0)
        offline_count_db = status_counts.get('Offline', 0)
        unknown_count_db = status_counts.get('Unknown', 0)
        total_status_count = available_count_db + busy_count_db + faulted_count_db + offline_count_db + unknown_count_db
        total_offline_count_db = offline_count_db+unknown_count_db
        assert total_charger_count == total_status_count, f"Expected  total charger count '{total_charger_count}', but got '{total_status_count}'"
        assert available_count == available_count_db, f"Expected available count {available_count}, but got {available_count_db}"
        assert busy_count == busy_count_db, f"Expected busy count {busy_count}, but got {busy_count_db}"
        assert faulty_count == faulted_count_db, f"Expected faulty count {faulty_count}, but got {faulted_count_db}"
        assert offline_count == total_offline_count_db, f"Expected offline count {offline_count}, but got {total_offline_count_db}"
        print("All assertions passed successfully for charger tile")


    def verify_fleet_list_heading(self):
        expected= "Fleet List"
        list_heading = self.page.inner_text(xpath_fleet_list_heading)
        assert list_heading==expected, f"Expected heading {expected}, but got {list_heading}"

    def verify_fleet_list_data(self):
        self.page.wait_for_timeout(4800)
        fleet_tile_elements = self.page.query_selector_all(xpath_fleet_data_tiles)
        # Store data for each tile in a list
        fleet_tile_data = []
        for tile in fleet_tile_elements:
            tile_text = tile.text_content()  # Get the text content of each tile
            fleet_tile_data.append(tile_text.strip())  # Append cleaned text to the list
        total_fleet_tiles = len(fleet_tile_data)
        # Optional: Print each tile's data separately
        for i, tile_data in enumerate(fleet_tile_data, start=1):
            print(f"Fleet Tile {i} Data:", tile_data)
        pagination_count = self.page.inner_text(xpath_pagination).strip()
        # Extract the pagination range (e.g., "1-6") and the total count (e.g., "7")
        pagination_range = pagination_count.split("of")[0].strip()  # This will give "1-6"
        # Split the range to pick the second number (6 in this case)
        first_page_number = int(pagination_range.split("-")[-1].strip())  # This will give "6"
        # Assert to ensure the count of fleet tiles matches the active fleet count from the database
        assert total_fleet_tiles == first_page_number, (
            f"Expected fleet count {first_page_number}, but got {total_fleet_tiles}"
        )
        # Return the total count of fleet tiles for use in pagination verification
        return total_fleet_tiles

    def verify_fleet_count_in_pagination(self, fetch_data):
        # Get the active fleet count from the first function
        active_fleet_count_db = self.verify_fleet_counts_on_tile(fetch_data)
        # Get the total fleet tiles count from the second function
        total_fleet_tiles_count = self.verify_fleet_list_data()
        pagination_count = self.page.inner_text(xpath_pagination).strip()
        pagination_range = pagination_count.split("of")[0].strip()  # This will give "1-6"
        total_count = int(pagination_count.split("of")[-1].strip().split()[0])  # Strip and get the first number
        # Split the range to pick the second number (6 in this case)
        first_page_count = int(pagination_range.split("-")[-1].strip())  # This will give "6"
        # Assert to check if the pagination matches the expected fleet counts
        assert active_fleet_count_db == total_count, f"Expected fleet count {active_fleet_count_db}, but got {total_count}"
        assert first_page_count == total_fleet_tiles_count, f"Expected first page count {first_page_count} is matched with the {total_fleet_tiles_count}"

    def verify_search_functionality(self):
        variable = self.page.inner_text(xpath_first_fleet_tile).splitlines()
        first_fleet_name = variable[0]
        search_key = first_fleet_name
        self.page.wait_for_selector(xpath_search_field).click()
        self.page.locator(xpath_search_field).fill(search_key)
        print(search_key)
        self.page.wait_for_timeout(1000)
        first_tile_after_search = self.page.inner_text(xpath_first_fleet_tile).strip().splitlines()
        first_one = first_tile_after_search[0]

        # Assert to check if the search result matches the search key
        assert first_one == search_key, (
            f"Expected '{search_key}' in the first tile after search, but got '{first_one}'"
        )


    def verify_energy_points(self, fetch_data):
        self.page.wait_for_timeout(2000)
        # Define the expected tab names
        expected_tabs = ["Energy Points","MT of CO2 Saved","Gasoline gallon equivalent (GGE Saved)", ]

        # Extracting data from the page
        Energy_points = self.page.wait_for_selector(xpath_Energy_point).inner_text().splitlines()
        print("13nov", Energy_points)

        Energypoint_tittle_heading = str(Energy_points[0])
        print("14 nov", Energypoint_tittle_heading)
        count_of_MT_of_CO2_Saved = float(Energy_points[1])
        print("1234", count_of_MT_of_CO2_Saved)
        text_MT_of_CO2_Saved = str(Energy_points[2])
        print("Anuhuti", text_MT_of_CO2_Saved)
        count_of_Gasoline_gallon_equivalent = float(Energy_points[-2])
        print("Anubhuti pathak", count_of_Gasoline_gallon_equivalent)
        text_Gasoline_gallon_equivalent = str(Energy_points[-1])
        print("123456778", text_Gasoline_gallon_equivalent)

        # Fetch data from database
        energy_point = "energy_tile_query"
        header, result = fetch_data(energy_point)
        print("db", result)

        # Unpack the first tuple in the result directly
        Total_Energy, Daily_average, db_value3, db_value4 = result[0]  # Unpacking the tuple directly
        print("db_value1:", Total_Energy)
        print("db_value2:", Daily_average)
        print("db_value3:", db_value3)
        print("db_value4:", db_value4)

        GGE = round(((Total_Energy / 1000) / 33.705), 2)
        print("GGE", GGE)

        assert GGE == count_of_Gasoline_gallon_equivalent, f"total energy value should be{GGE},but got{count_of_Gasoline_gallon_equivalent}"
        MT_CO2_SAVED = round(GGE * (19.592480 * 0.00045359), 2)
        print("MT_CO2_SAVED", MT_CO2_SAVED)

        assert MT_CO2_SAVED == count_of_MT_of_CO2_Saved, f"MT co2 save should be{MT_CO2_SAVED},but got{count_of_MT_of_CO2_Saved}"
        assert Energypoint_tittle_heading == expected_tabs[
            0], f"Energy tile heading should be {expected_tabs[0]},but got{Energypoint_tittle_heading}"
        assert text_MT_of_CO2_Saved == expected_tabs[
            1], f"Mt of CO2 Saved should be {expected_tabs[1]},but got{text_MT_of_CO2_Saved}"
        assert text_Gasoline_gallon_equivalent == expected_tabs[
            -1], f"Gasoline gallon gas equivalent text should be{expected_tabs[-1]},but got{text_Gasoline_gallon_equivalent}"
        return Total_Energy, Daily_average

    def Energy_used(self, fetch_data):
        global print
        self.page.wait_for_timeout(2000)
        expected_tabs = [
            "Energy Used",
            "Total Energy",
            "Daily Energy",
        ]

        # Call verify_Energy_points() and unpack the return values
        Total_Energy, Daily_average = self.verify_energy_points(fetch_data)  # Pass fetch_data here
        print("Returned Total Energy:", Total_Energy)
        print("Returned Daily Average:", Daily_average)

        # Extracting energy used data from the page
        Energy_used = self.page.wait_for_selector(xpath_Energy_used).inner_text().splitlines()
        print("14th november", Energy_used)

        Energy_used_tittle_heading = str(Energy_used[0])
        print("14 nov", Energy_used_tittle_heading)
        energy_string = str(Energy_used[2])  # Assuming this is a number
        print("1234", energy_string)
        cleaned_energy_string = ''.join(char for char in energy_string if char.isdigit() or char == '.')
        print("Cleaned energy string:", cleaned_energy_string)
        count_of_Total_energy_kwh = float(cleaned_energy_string)
        print("Converted Total Energy (kWh):", count_of_Total_energy_kwh)
        print(type(count_of_Total_energy_kwh))
        text_totalEnergy = str(Energy_used[1])
        print("Anuhuti", text_totalEnergy)
        Daily_average_string = str(Energy_used[-3])  # Assuming this is a number
        print("Anubhuti pathak", Daily_average_string)
        Daily_average_split_string = ''.join(char for char in Daily_average_string if char.isdigit() or char == '.')
        print("total", Daily_average_split_string)
        count_of_daily_average = float(Daily_average_split_string)
        print(count_of_daily_average, type(count_of_daily_average))

        energy_point = "energy_tile_query"
        header, result = fetch_data(energy_point)
        print("db", result)

        # Unpack the first tuple in the result directly
        Total_Energy, Daily_average, db_value3, db_value4 = result[0]  # Unpacking the tuple directly
        print("db_value1:", Total_Energy)
        print("db_value2:", Daily_average)
        print("db_value3:", db_value3)
        print("db_value4:", db_value4)

        db_value_total_energy = Total_Energy / 1000
        print("Assitant:", db_value_total_energy)
        print(type(db_value_total_energy))

        db_value_daily_average_in_kwh = float(round(Daily_average / 1000, 2))
        print("sssssss", type(db_value_daily_average_in_kwh))

        assert count_of_Total_energy_kwh == db_value_total_energy, (
            f"Expected value form db {db_value_total_energy} is "
            f"matched with the FE vaule {count_of_Total_energy_kwh}")

        assert db_value_daily_average_in_kwh == count_of_daily_average, f"expected value from db{db_value_daily_average_in_kwh},but got {count_of_daily_average}"
        assert Energy_used_tittle_heading == expected_tabs[
            0], f"expected value {expected_tabs[0]},but got{Energy_used_tittle_heading}"
        assert text_totalEnergy == expected_tabs[
            1], f"expected value from db {expected_tabs[1]},but got{text_totalEnergy}"

    def verify_charging_infrastructure_bottom_card(self, fetch_data):
        self.page.wait_for_timeout(2000)
        expected_tabs = ["Charging Infrastructure","Total Depot","Total Chargers", ]
        charging_infrastructure_bottom_card_data_and_text = self.page.wait_for_selector(xpath_charging_nfrastructure_bottom_card).inner_text().splitlines()
        charging_infrastructure_tittle_heading = str(charging_infrastructure_bottom_card_data_and_text[0])
        total_count_of_depot = int(charging_infrastructure_bottom_card_data_and_text[1])
        total_depot_text_bottom_card= str(charging_infrastructure_bottom_card_data_and_text[2])
        total_count_of_chargers = int(charging_infrastructure_bottom_card_data_and_text[-2])
        total_charger_text_bottom_card = str(charging_infrastructure_bottom_card_data_and_text[-1])
        # Fetch data from database
        charging_infrastructure = "charging_infrastructure_bottom_tile_count"
        header, result = fetch_data(charging_infrastructure)
        total_depot_from_count_db = int(result[0][0] if result else 0)
        total_chargers_from_count_db = int(result[0][1] if result else 0)

        assert total_count_of_depot == total_depot_from_count_db, f"The FE depot count is: {total_count_of_depot}, and the db depot count are not matched{total_depot_from_count_db}"
        assert total_count_of_chargers == total_chargers_from_count_db, f"The FE charger count is: {total_count_of_chargers}, and the DB charger count is: {total_chargers_from_count_db}"
        assert total_depot_text_bottom_card ==  expected_tabs[1], f"expected value on FE {expected_tabs[2]},but got{total_depot_text_bottom_card}"
        assert total_charger_text_bottom_card == expected_tabs[-1], f"expected value on FE {expected_tabs[2]},but got{total_charger_text_bottom_card}"






