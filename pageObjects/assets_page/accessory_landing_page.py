import random


from playwright.sync_api import Page, sync_playwright, expect

xpath_assets_module = "//span[text()='Assets']"
xpath_accessory_tab = "//span[text()='Accessory Setup']"
xpath_accessory_setup_menu = "h2"
accessory_text = "Accessory Setup"
xpath_accessory_button = "//h6[text()='ADD ACCESSORY']"
xpath_accessory_page_heading = "//h2[@class='MuiTypography-root MuiTypography-h2 MuiTypography-gutterBottom page_title css-p08hmt']"
xpath_total_accessory_count = "(//div[@class='number'])[1]"
xpath_accessory_cable_count = "(//div[@class='number'])[2]"
xpath_accessory_modem_count = "(//div[@class='number'])[3]"
xpath_accessory_pad_count = "(//div[@class='number'])[4]"
xpath_accessory_power_cabinet = "(//div[@class='number'])[5]"
xpath_accessory_rfid_reader_count = "(//div[@class='number'])[6]"
xpath_accessory_switch_gare_count = "(//div[@class='number'])[7]"
xpath_table_header = "//tr[@class='MuiTableRow-root MuiTableRow-head css-q4tpp9']"
xpath_search_field = "//input[@placeholder= 'Search By Device ID']"
xpath_search_record_table_data = "//tbody[@class='MuiTableBody-root css-vgykel']"
xpath_tr = "(//tr[@class='MuiTableRow-root css-1ri61x6'])[1]"
xpath_td = "(//td[@class='MuiTableCell-root MuiTableCell-body MuiTableCell-sizeMedium css-qk49cz'])[1]"
xpath_total_count_in_pagination = "//div[@class='MuiStack-root pagination_count css-u4p24i']"
xpath_row_count = "//table[@class='MuiTable-root css-1cckzu4']/tbody/tr"
xpath_column_count = "//table[@class='MuiTable-root css-1cckzu4']/thead/tr/th"
xpath_row_cels = "table tbody tr:first-child td"
xpath_first_row_value = "(//table[@class='MuiTable-root css-1cckzu4']/tbody/tr)[2]"
xpath_item_per_page = "//ul[@class='MuiList-root MuiList-padding MuiMenu-list css-r8u8y9']"

# Define XPaths as constants
DROPDOWN_XPATH = "//div[@class='MuiSelect-select MuiSelect-standard MuiInputBase-input MuiInput-input css-1cccqvr']"
OPTIONS_XPATH = "//ul[@role='listbox']//li"  # Adjust if necessary
DATA_CONTAINER_XPATH = "//div[@class='data-container']"  # Adjust as necessary

class AccessoryPageHeader:
    initial_count = None
    modem_initial_count = None

    def __init__(self, page: Page):
        self.desired_value = None
        self.total_count_pagination_after_search = None
        self.page = page
        self.start_date = None

    def click_assets(self):
        try:
            self.page.wait_for_selector(xpath_assets_module).click()
        except Exception as e:
            self.page.screenshot(path="Screenshots/assets_module.png")
            print(f"An error occurred: {str(e)}")  # This will now execute
            raise AssertionError(f"{str(e)}. Screenshot captured.")

    def click_accessory_tab(self):
        try:
            self.page.wait_for_selector(xpath_accessory_tab).click()
            expect(self.page.locator(xpath_accessory_setup_menu)).to_contain_text(accessory_text)
        except Exception as e:
            self.page.screenshot(path="Screenshots/accessory_tab.png")
            print(f"An error occurred: {str(e)}")  # This will now execute
            raise AssertionError(f"{str(e)}. Screenshot captured.")

    def verify_landing_page_heading(self):
        try:
            text_accessory_locator = self.page.locator(xpath_accessory_page_heading)

            expect(text_accessory_locator).to_contain_text(accessory_text)
        except Exception as e:
            self.page.screenshot(path="Screenshots/accessory_page_heading.png")
            print(f"An error occurred: {str(e)}")  # This will now execute
            raise AssertionError(f"{str(e)}. Screenshot captured.")


    def verify_widget_total_count_with_sum_sub_count(self):
        try:
            count = self.page.inner_text(xpath_total_accessory_count).strip()
            total_count = int(count)  # Convert the total count to an integer
            print("Total count:", total_count)
            # Fetch the counts for each accessory
            cable_count = int(self.page.inner_text(xpath_accessory_cable_count).strip())
            print("Cable Count:", cable_count)
            modem_count = int(self.page.inner_text(xpath_accessory_modem_count).strip())
            print("modem count:", modem_count)
            pad_count = int(self.page.inner_text(xpath_accessory_pad_count).strip())
            print("pad count:", pad_count)
            power_cabinet = int(self.page.inner_text(xpath_accessory_pad_count).strip())
            print("power cabinet count:", power_cabinet)
            rfid_reader_count = int(self.page.inner_text(xpath_accessory_rfid_reader_count).strip())
            print("rfid card count:", rfid_reader_count)
            switch_gare_count = int(self.page.inner_text(xpath_accessory_switch_gare_count).strip())
            print("switch gare count:", switch_gare_count)
            # Calculate the total from individual counts
            calculated_total = (cable_count+modem_count+pad_count+power_cabinet+rfid_reader_count+switch_gare_count)
            print("Sum of all the accessory category", calculated_total)
            if total_count == calculated_total:
                print("The total count matches the sum of individual accessory counts.")
            else:
                print("The total count does not match the sum of individual accessory counts.")
                print(f"Calculated total: {calculated_total}, Expected total: {total_count}")

            pagination_count = self.page.inner_text(xpath_total_count_in_pagination).strip()
            print("Total pagination count: ", pagination_count)
            total_pagination_count = int(pagination_count.split("of")[-1].strip().split()[0])
            print("total_pagination_count:", total_pagination_count)

            if total_count == total_pagination_count:
                print("total count and the pagination count is matched")
            else:
                print("The total count and the pagination count are not matched")
        except Exception as e:
            self.page.screenshot(path="Screenshots/widget_count_matched.png")
            print(f"An error occurred: {str(e)}")  # This will now execute
            raise AssertionError(f"{str(e)}. Screenshot captured.")


    def verify_table_header(self):
        try:
            # Locate the table headers (assuming the headers are within <th> tags)
            headers = self.page.locator(xpath_table_header).all_inner_texts()[0]
            header_column_split = headers.split("\n")
            # Expected header values
            expected_headers = ['Accessory Category', 'Device ID', 'Make', 'Model', 'Installation Date', 'Status', 'Action']
            # Compare extracted headers with expected headers
            if header_column_split == expected_headers:
                print("Headers match expected values.")
            else:
                print("Headers do not match expected values.")
        except Exception as e:
            self.page.screenshot(path="Screenshots/table_header.png")
            print(f"An error occurred: {str(e)}")  # This will now execute
            raise AssertionError(f"{str(e)}. Screenshot captured.")

    def click_enter_search_key(self, search_key=None):
        try:
            # Wait for the first row and get its inner text
            row_value = self.page.wait_for_selector(xpath_first_row_value).inner_text()
            print("First row data:", row_value)

            # Select the first row and get all cell values
            row_cells = self.page.locator(xpath_row_cels)
            cell_count = row_cells.count()
            print("Cell count:", cell_count)

            # Collect text from each cell
            row_data = [row_cells.nth(i).inner_text() for i in range(cell_count)]
            print("Row cell data:", row_data)

            # Check if we have enough data
            if len(row_data) > 1:
                self.desired_value = row_data[1]  # Set desired_value for later use
                print(f"Desired Value: {self.desired_value}")

                # Fill in the search field
                search_field = self.page.wait_for_selector(xpath_search_field)
                search_field.click()
                self.page.fill(xpath_search_field, self.desired_value)

                # Get row and column counts
                row_count = self.page.locator(xpath_row_count).count()
                column_count = self.page.locator(xpath_column_count).count()
                print("Row count:", row_count, "Column count:", column_count)

                # Iterate through rows and columns to print values
                for r in range(1, row_count + 1):
                    for c in range(1, column_count + 1):
                        value = self.page.wait_for_selector(
                            f"//table[@class='MuiTable-root css-1cckzu4']/tbody/tr[{r}]/td[{c}]").text_content()
                        if value == "":
                            expect(value).to_contain_text(self.desired_value)
                        print(value, end="   ")
                    print()  # New line after each row

                # Extract total count from pagination
                total_count_text = self.page.wait_for_selector(xpath_total_count_in_pagination).inner_text()
                total_count = int(total_count_text.split("of ")[-1].strip().split()[0])
                print("Total count from pagination:", total_count)

                # Check if row count matches the pagination count
                if row_count == total_count:
                    print("Pagination count matches row count.")
                else:
                    print("Pagination count does not match row count.")
            else:
                print("Not enough data in row_data to extract desired_value.")
        except Exception as e:
            self.page.screenshot(path="Screenshots/search_random_value.png")
            print(f"An error occurred: {str(e)}")


     # it is correct code for the item per page value
    def verify_item_per_page(self):
        # Click the dropdown to reveal options
        self.page.click(
            "//div[@class='MuiSelect-select MuiSelect-standard MuiInputBase-input MuiInput-input css-1cccqvr']")

        # Get all the dropdown option elements
        option_elements = self.page.query_selector_all("//ul[@role='listbox']//li")  # Adjust the XPath if needed
        print("Get all the dropdown option elements:", option_elements)

        # Extract the text from each option
        item_per_page_dropdown_values = [option.inner_text() for option in option_elements]
        print("Dropdown values:", item_per_page_dropdown_values)

        # Choose a random value
        selected_value = random.choice(item_per_page_dropdown_values)
        print("Selected value:", selected_value)

        # Click on the randomly selected value
        self.page.click(f"//li[text()='{selected_value}']")
        row_count = self.page.locator(xpath_row_count).count()
        print("The total row count:", row_count)

    # def verify_item_per_page1(self):
    #     # Click the dropdown to reveal options
    #     self.page.click(DROPDOWN_XPATH)
    #
    #     # Get all the dropdown option elements
    #     option_elements = self.page.query_selector_all(OPTIONS_XPATH)
    #
    #     # Extract the text from each option
    #     item_per_page_dropdown_values = [option.inner_text() for option in option_elements]
    #     print("Dropdown values:", item_per_page_dropdown_values)
    #
    #     # Choose a random value
    #     selected_value = random.choice(item_per_page_dropdown_values)
    #     print("Selected value:", selected_value)
    #
    #     # Click on the randomly selected value
    #     self.page.click(f"{OPTIONS_XPATH}[text()='{selected_value}']")
    #
    #     # Wait for the data to load
    #     self.page.wait_for_selector(DATA_CONTAINER_XPATH)
    #
    #     # Get the displayed data
    #     displayed_data = self.page.inner_text(DATA_CONTAINER_XPATH)
    #     print("Displayed data:", displayed_data)
    #
    #     # Verify that the displayed data matches the selected value
    #     if selected_value in displayed_data:
    #         print("Verification successful: The displayed data matches the selected value.")
    #     else:
    #         print("Verification failed: The displayed data does not match the selected value.")











