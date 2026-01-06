from playwright.sync_api import sync_playwright, Page
from Test_Cases.conftest import fetch_data, db_connection, load_queries, fetch_data_transform_db
from Utilities.ReadProperties import ReadConfig

url = ReadConfig.get_back_end_url()

xpath_depot = "//div/span[contains(text(),'Depots')]"
xpath_depot_chart = "//div[@class='tab_pie_chart']"
xpath_fleet_text = "//h2[normalize-space(text()) = 'fleets']"
xpath_fleets_dashboard_tiles = "//div[@class='text']"
xpath_total_fleet_count = "(//div[@class='number'])[1]"
xpath_active_fleet_count = "(//div[@class='number'])[2]"
xpath_inactive_fleet_count = "(//div[@class='number'])[3]"
xpath_vehicle_tile = "(//div[@class='agr_data_box'])[2]"
xpath_depot_tile = "(//div[@class='agr_data_box'])[3]"
xpath_charger_tile = "(//div[@class='agr_data_box'])[4]"
xpath_vehicle_breadcrumb = "//button[@data-testid='vehicles']"
xpath_vehicle_pychart = "//div[@class='tab_pie_chart']"
xpath_Energy_point = "(//div[@class='MuiCardContent-root card_content css-1qw96cp'])[1]"
xpath_Energy_used = "(//div[@class='MuiCardContent-root card_content css-1qw96cp'])[4]"


class DepotDashboardPage:

    def __init__(self, page: Page):
        self.page = page

    def Depot_chart(self, fetch_data):
        self.page.wait_for_timeout(2000)
        expected_tabs = [
            "Commissioned",
            "Upcoming",
            "Under Maintenance",
            "Decommissioned"
        ]
        Pychart = self.page.wait_for_selector(xpath_depot_chart).inner_text().splitlines()
        print("abcd", Pychart)
        total_depot_count = int(Pychart[0])
        print("123", total_depot_count)
        Decommissioned_text = str(Pychart[-1])
        print("1234", Decommissioned_text)
        Upcoming_text = str(Pychart[2])
        print("123456", Upcoming_text)
        under_maintenance = str(Pychart[-2])
        print("1234567", under_maintenance)
        commissioned_text = str(Pychart[1])
        print("12345689", commissioned_text)

        Depot_pychart_query_key = "depot_chart_count_query"
        headers, result = fetch_data(Depot_pychart_query_key)
        print("ABCD", result)
        total_fleet_count_db = int(result[0][0] if result else 0)
        print("ABCDER", total_fleet_count_db)

        assert total_depot_count == total_fleet_count_db, f"depot count should be match with db count,but got{total_depot_count}"

        # Assert that the total depot count is correct (e.g., check that it's not zero or a negative value)
        assert total_depot_count > 0, f"Total depot count should be greater than 0, but got {total_depot_count}"

        # Assert that the actual tab values match the expected tabs in the correct order
        assert commissioned_text == expected_tabs[0], f"Expected 'Commissioned' but got '{commissioned_text}'"
        assert Upcoming_text == expected_tabs[1], f"Expected 'Upcoming' but got '{Upcoming_text}'"
        assert under_maintenance == expected_tabs[2], f"Expected 'Under Maintenance' but got '{under_maintenance}'"
        assert Decommissioned_text == expected_tabs[3], f"Expected 'Decommissioned' but got '{Decommissioned_text}'"

        # You could also add an assertion to verify the length of `circle` if needed (e.g., expecting 5 items)
        assert len(Pychart) == 5, f"Expected 5 items in circle, but got {len(Pychart)}"
        return total_depot_count

    def depot_click(self):
        self.page.wait_for_selector(xpath_depot).click()

    # from Test_Cases.conftest import login, setup, fetch_data, access_token, fetch_data_transform_db
    # from pageObjects.fleet_dashboard_page import FleetDashboardPage
    def click_vehicle_breadcrumb(self):
        self.page.wait_for_selector(xpath_vehicle_breadcrumb).click()

    def verify_vehicle_chart(self, fetch_data_transform_db):
        # Adding a timeout (you might want to adjust or remove it depending on your requirements)
        self.page.wait_for_timeout(1000)

        # Define the expected tab names
        expected_tabs = [
            "Moving",
            "Idle",
            "Parked",
            "Faulty"
        ]

        # Fetch the actual chart data (from the page) as a list of strings
        Vehicle_pychart = self.page.wait_for_selector(xpath_vehicle_pychart).inner_text().splitlines()

        # Debug: Print the fetched vehicle chart data for visibility
        print("AERRRR", Vehicle_pychart)

        # Extract the total vehicle count from the chart
        total_vehicle_count_on_chart = int(Vehicle_pychart[0])
        print("Anu", total_vehicle_count_on_chart)

        # Extract individual tabs' text from the chart
        Faulty_text = str(Vehicle_pychart[-1])
        print("1234", Faulty_text)
        Idle_text = str(Vehicle_pychart[2])
        print("123456", Idle_text)
        Parked_text = str(Vehicle_pychart[-2])
        print("1234567", Parked_text)
        Moving_text = str(Vehicle_pychart[1])
        print("12345689", Moving_text)

        # Fetch vehicle count data from the database (using the provided fetch_data_transform_db function)
        Vehicle_pychart_query_key = "vehicle_chart_count_query"
        headers, result = fetch_data_transform_db(Vehicle_pychart_query_key)
        print("ABCD", result)

        # Extract total vehicle count from the database result
        total_Vehicle_count_db = int(result[0][0] if result else 0)
        print("ABCDER", total_Vehicle_count_db)

        # Assert that the total vehicle count from the chart matches the database value
        assert total_vehicle_count_on_chart == total_Vehicle_count_db, \
            f"Vehicle count mismatch: Expected {total_Vehicle_count_db}, but got {total_vehicle_count_on_chart}"

        # Assert that the total vehicle count on the chart is greater than 0
        assert total_vehicle_count_on_chart > 0, f"Total vehicle count should be greater than 0, but got {total_vehicle_count_on_chart}"

        # Assert that the tab names match the expected values in the correct order
        assert Moving_text == expected_tabs[0], f"Expected 'Moving' but got '{Moving_text}'"
        assert Idle_text == expected_tabs[1], f"Expected 'Idle' but got '{Idle_text}'"
        assert Parked_text == expected_tabs[2], f"Expected 'Parked' but got '{Parked_text}'"
        assert Faulty_text == expected_tabs[3], f"Expected 'Faulty' but got '{Faulty_text}'"

        # Optionally, assert the length of the `Vehicle_pychart` list to be 5
        assert len(Vehicle_pychart) == 5, f"Expected 5 items in Vehicle_pychart, but got {len(Vehicle_pychart)}"
        return total_vehicle_count_on_chart

    def verify_Energy_points(self, fetch_data):
        self.page.wait_for_timeout(2000)
        # Define the expected tab names
        expected_tabs = [
            "Energy Points",
            "MT of CO2 Saved",
            "Gasoline gallon equivalent (GGE Saved)",
        ]

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
        Total_Energy, Daily_average = self.verify_Energy_points(fetch_data)  # Pass fetch_data here
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
