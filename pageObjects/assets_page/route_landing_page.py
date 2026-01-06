import random
import time

from playwright.sync_api import Page, expect

xpath_assets_module= "//span[text()='Assets']"
xpath_route_setup_menu = "//span[text()='Route Setup']"
add_route_page_title = "ADD ROUTE"
xpath_widget_tile_text = "//div[@class='text']"
xpath_route_page_heading = "//h2[@class='MuiTypography-root MuiTypography-h2 MuiTypography-gutterBottom page_title css-p08hmt']"
route_page_heading = "Route Setup"
xpath_total_route_count = "(//div[@class='number'])[1]"
xpath_active_route_count = "(//div[@class='number'])[2]"
xpath_inactive_route_count = "(//div[@class='number'])[3]"
xpath_total_route_count_in_pagination = "//div[@class='MuiStack-root pagination_count css-u4p24i']"
xpath_add_route_button = "//div[@class='add_assets']"
route_page_url = "https://fleete-qa-dashboard.demoapplication.net/routesetup/add-route"
xpath_back_button = "//button[@data-testid='header-back-button']"
xpath_table_column_header = "//table[@class='MuiTable-root css-1cckzu4']//thead//tr"
xpath_search_field = "//input[@placeholder='Search By Route Name']"
xpath_first_column_data = "//table[@class='MuiTable-root css-1cckzu4']//tbody/tr/td[1]"
xpath_rows = "//table[@class='MuiTable-root css-1cckzu4']//tbody/tr"
xpath_item_per_page_dropdown = "//div[@role='combobox']"
xpath_item_per_page_dropdown_values = "//ul[@class='MuiList-root MuiList-padding MuiMenu-list css-r8u8y9']//li"
xpath_fleet_name_field = "//div[@id='demo-simple-select-standard']"
xpath_fleet_values = "//li[contains(@class, 'MuiMenuItem-root')]"


class RouteLandingPage:


    def __init__(self, page: Page):
        self.page= page
    def click_assets_menu(self):
        self.page.wait_for_selector(xpath_assets_module).click()
    def click_route_setup_sub_menu(self):
        self.page.wait_for_selector(xpath_route_setup_menu).click()
    def verify_route_tile_text(self):
        tile_text = self.page.locator(xpath_widget_tile_text).all_text_contents()
        # print("Tile text:", tile_text)
        expected_tile_text = ['Routes', 'Active ', 'Inactive']
        if tile_text == expected_tile_text:
            print("Tile text matched successfully")
        else:
            print("The tile text not matched")
    def verify_landing_page_heading(self):
        text_accessory_locator = self.page.locator(xpath_route_page_heading)
        expect(text_accessory_locator).to_contain_text(route_page_heading)



    def verify_tile_total_count_with_some_of_sub_count(self):
        total_routes_count = int(self.page.inner_text(xpath_total_route_count).strip())
        # print("Total route count is:", total_routes_count)
        active_route_count = int(self.page.inner_text(xpath_active_route_count).strip())
        # print("Total active route count is:", active_route_count)
        inactive_route_count = int(self.page.inner_text(xpath_inactive_route_count).strip())

        # print("Total active route count is:", inactive_route_count)
        sum_of_sub_count = active_route_count + inactive_route_count

        if total_routes_count== sum_of_sub_count:
            print("The total route count is matched with the sum of the active + inactive count")
        else:
            print("The total route count is not matched with the sum of the active + inactive count")

        total_route_count_in_pagination = self.page.inner_text(xpath_total_route_count_in_pagination).strip()
        print("total route count in pagination:", total_route_count_in_pagination)
        pagination_total_route_count = int(total_route_count_in_pagination.split("of")[-1].strip().split()[0])
        print("Pagination total count after split the values;", pagination_total_route_count)
        if total_routes_count == pagination_total_route_count:
            print("Total route count matched with the pagination total route count")
        else:
            print("Total route count is not matched with the pagination total route count")


    def verify_table_header(self):
        table_header_column = self.page.locator(xpath_table_column_header).all_inner_texts()[0]
        # print("Table header column:", table_header_column)
        column_split_values = table_header_column.split("\n")
        # print("Column split values:", column_split_values)
        expected_table_header_columns = ['Route Name', 'Fleet Name', 'Start Point', 'Destination Point', 'Start Lat/Long', 'Destination Lat/Long', 'Distance', 'Active Journey', 'Completed Journey', 'Action']
        if column_split_values == expected_table_header_columns:
            print("Table column valuer are matched")
        else:
            print("Table column valuer are not matched")

    def verify_the_search_functionality(self):
        # Click on the search input
        self.page.locator(xpath_search_field).click()
        # Get the inner text of all rows in the first column
        first_column_data = self.page.locator(xpath_first_column_data).all_inner_texts()
        # print("First column data is:", first_column_data)
        # Pick a random route name from the list
        selected_route = random.choice(first_column_data).strip()  # Strip whitespace if needed
        print("Selected Route Name:", selected_route)
        self.page.locator(xpath_search_field).fill(selected_route)
        # Verify how many rows are displayed in the table
        time.sleep(5)
        row_count = self.page.locator(xpath_rows).count()
        print("Number of rows displayed in the table:", row_count)

        total_update_route_count_in_pagination_after_search = self.page.inner_text(xpath_total_route_count_in_pagination).strip()
        print("total route count in pagination:", total_update_route_count_in_pagination_after_search)
        pagination_total_route_count_after_split = int(total_update_route_count_in_pagination_after_search.split("of")[-1].strip().split()[0])
        print("Pagination total count after split the values in search;", pagination_total_route_count_after_split)
        if row_count == pagination_total_route_count_after_split:
            print("Total route count matched with the pagination total route count  after search")
        else:
            print("Total route count is not matched with the pagination total route count after search")
            # Clear the search input field after validation
        self.page.locator(xpath_search_field).fill('')  # Clear the search input
        print("Search input cleared.")



    def verify_item_per_page(self, pagination_total_route_count_after_split=None):
        self.page.wait_for_selector(xpath_item_per_page_dropdown).click()
        dropdown_values = self.page.locator(xpath_item_per_page_dropdown_values).all_inner_texts()
        print("Dropdown values:", dropdown_values)
        random_value_pick = random.choice(dropdown_values).strip()
        print("Random picked value from the item per page dropdown:", random_value_pick)
        # Click on the selected value in the dropdown
        self.page.click(f"text='{random_value_pick}'")
        # Wait for the rows to update dynamically
        self.page.wait_for_selector(xpath_rows)  # Wait until the rows are available
        row_displayed_after_select_item_per_page = self.page.locator(xpath_rows).count()   # Count the displayed rows
        print("Displayed rows after selecting item per page:", row_displayed_after_select_item_per_page)
        if int(random_value_pick) == row_displayed_after_select_item_per_page:    # Validate displayed rows against the selected item per page
            print("The rows are displayed correctly and match the selected item per page data.")
        else:
            print("The rows are not displayed correctly and do not match the selected item per page data.")
        # Validate against pagination total count if provided
        total_route_count_in_pagination = self.page.inner_text(xpath_total_route_count_in_pagination).strip()
        print("Total route count in pagination after select the item per page:", total_route_count_in_pagination)

        # Extract total count from pagination text
        try:
            pagination_total_route_count_after_select_item_per_page = int(total_route_count_in_pagination.split("of")[0].strip().split()[-1])
        except (IndexError, ValueError):
            print("Error extracting pagination count. Please check the pagination text format.")
            return

        print("Pagination total count after split the values after select the item per page:",
              pagination_total_route_count_after_select_item_per_page)

        if int(random_value_pick) == pagination_total_route_count_after_select_item_per_page:
            print("Total rows count matched with the pagination total route count.")
        else:
            print("Total rows count is not matched with the pagination total route count.")

    def verify_add_route_button(self):
        self.page.locator(xpath_add_route_button).click()

        # Fetch the text and assert it directly
        add_route_page_heading = self.page.inner_text(xpath_route_page_heading)

        # Using a simple assert instead of expect for strings
        assert add_route_page_heading == "ADD ROUTE", f"Expected 'ADD ROUTE', but got '{add_route_page_heading}'"
        self.page.wait_for_url(route_page_url)
        # self.page.locator(xpath_back_button).click()

    def click_select_fleet_name(self):
        self.page.wait_for_selector(xpath_fleet_name_field)
        print("open  the fleet drondwn")
        time.sleep(4)
        self.page.wait_for_selector(xpath_fleet_values).click()
        print("fhgdhfsgdfdhgfsdfs")




















