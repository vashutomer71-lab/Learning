import random
import time
import uuid
import string
import re
from datetime import datetime
from playwright.sync_api import Page, sync_playwright



xpath_assets_module = "//span[text()='Assets']"
xpath_accessory_tab = "//span[text()='Accessory Setup']"
xpath_accessory_button = "//h6[text()='ADD ACCESSORY']"
xpath_fleet_dropdown = "(//div[@id='demo-simple-select-standard'])[1]"
xpath_Fleet_dropdown_value = "//li[@data-value='12121']"
xpath_depot_name_dropdown = "(//div[@id='demo-simple-select-standard'])[2]"
xpath_depot_dropdown_value = "//li[@data-value='12127']"
xpath_accessory_dropdown = "(//div[@id='demo-simple-select-standard'])[3]"
xpath_accessory_dropdown_value = "//li[@data-value='Cable']"
xpath_serial_number = "//input[@name='serial']"
xpath_device_id = "//input[@name='deviceId']"
xpath_status_dropdown = "(//div[@id='demo-simple-select-standard'])[4]"
xpath_status_dropdown_value = "//li[text()='Active']"
xpath_make_id = "(//div[@class='MuiInputBase-root MuiInput-root MuiInput-underline MuiInputBase-colorPrimary MuiInputBase-formControl css-1al598k'])[4]"
xpath_make_dropdown_value = "//li[text()='Siemens CCS Combo 1']"
xpath_model_id = "(//div[@class='MuiInputBase-root MuiInput-root MuiInput-underline MuiInputBase-colorPrimary MuiInputBase-formControl css-1al598k'])[5]"
xpath_model_dropdown_value = "//li[text()='SI-EXT-1500']"
xpath_warranty_start_date = "(//button[@aria-label='Choose date'])[1]"
xpath_date_visible = ".MuiPickersDay-root"
xpath_enabled_date = "//button[@class='MuiButtonBase-root MuiPickersDay-root MuiPickersDay-dayWithMargin css-6exafu' and @aria-selected='false' and @role='gridcell']"
xpath_warranty_end_date = "//button[@aria-label='Choose date']"
xpath_calendar = "//div[@class='MuiDateCalendar-root css-5oi4td']"
xpath_submit_button = "//button[@type='submit']"
xpath_total_accessory_count="(//div[@class='number'])[1]"
xpath_total_updated_accessory_count="(//div[@class='number'])[1]"
xpath_cable_initial_count = "(//div[@class='MuiGrid-root MuiGrid-item MuiGrid-grid-xs-2 text_component css-yi49kw'])[1]"
xpath_cable_update_count = "(//div[@class='MuiGrid-root MuiGrid-item MuiGrid-grid-xs-2 text_component css-yi49kw'])[1]"


class AccessoryPageCable:
    initial_count = None
    cable_initial_count = None

    def __init__(self, page: Page):

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
        except Exception as e:
            self.page.screenshot(path="Screenshots/accessory_tab.png")
            print(f"An error occurred: {str(e)}")  # This will now execute
            raise AssertionError(f"{str(e)}. Screenshot captured.")

    def click_add_accessory_button(self):
        try:
            self.page.wait_for_selector(xpath_accessory_button).click()
        except Exception as e:
            self.page.screenshot(path="Screenshots/add_accessory_button.png")
            print(f"An error occurred: {str(e)}")  # This will now execute
            raise AssertionError(f"{str(e)}. Screenshot captured.")

    def click_fleet_name_dropdown_and_select_value(self):
        try:
            self.page.wait_for_selector(xpath_fleet_dropdown).click()
            self.page.wait_for_selector(xpath_Fleet_dropdown_value).click()
        except Exception as e:
            self.page.screenshot(path="Screenshots/fleet_name_drop_down_value.png")
            print(f"An error occurred: {str(e)}")  # This will now execute
            raise AssertionError(f"{str(e)}. Screenshot captured.")

    def click_depot_name_dropdown_and_select_value(self):
        try:
            self.page.wait_for_selector(xpath_depot_name_dropdown).click()
            self.page.wait_for_selector(xpath_depot_dropdown_value).click()
        except Exception as e:
            self.page.screenshot(path="Screenshots/depot_name_dropdown_and_select_value.png")
            print(f"An error occurred: {str(e)}")  # This will now execute
            raise AssertionError(f"{str(e)}. Screenshot captured.")

    def click_accessory_dropdown_and_select_value(self):
        try:
            self.page.wait_for_selector(xpath_accessory_dropdown).click()
            self.page.wait_for_selector(xpath_accessory_dropdown_value).click()
        except Exception as e:
            self.page.screenshot(path="Screenshots/accessory_dropdown_and_select_value.png")
            print(f"An error occurred: {str(e)}")  # This will now execute
            raise AssertionError(f"{str(e)}. Screenshot captured.")


    def click_fill_serial_number(self, length=21):
        try:
            self.page.wait_for_selector(xpath_serial_number).click()
            self.page.wait_for_selector(xpath_serial_number)
            random_number = random.randint(21, 39)
            additional_chars = ''.join(random.choices(string.ascii_uppercase + '0123456789', k=length - 2))
            serial_number = f"{random_number}{additional_chars}"
            unique_id = str(uuid.uuid4()).replace('-', '').upper()  # Remove dashes and convert to uppercase
            unique_serial_number = f"{unique_id}-{serial_number}"  # Example of prepending
            self.page.fill(xpath_serial_number, unique_serial_number)
        except Exception as e:
            self.page.screenshot(path="Screenshots/serial_number.png")
            print(f"An error occurred: {str(e)}")  # This will now execute
            raise AssertionError(f"{str(e)}. Screenshot captured.")

    def click_fill_device_id(self, length=10):
        try:
            self.page.wait_for_selector(xpath_device_id).click()
            random_device_id = random.randint(9, 16)
            additional_chars = ''.join(random.choices(string.ascii_uppercase + '0123456789', k=length - 2))
            device_id = f"{random_device_id}{additional_chars}"
            unique_id = str(uuid.uuid4()).replace('-', '').upper()  # Remove dashes and convert to uppercase
            unique_device_id = f"{unique_id}-{device_id}"  # Example of prepending
            self.page.fill(xpath_device_id, unique_device_id)
        except Exception as e:
            self.page.screenshot(path="Screenshots/device_id.png")
            print(f"An error occurred: {str(e)}")  # This will now execute
            raise AssertionError(f"{str(e)}. Screenshot captured.")

    def click_status_dropdown_and_select_value(self):
        try:
            self.page.wait_for_selector(xpath_status_dropdown).click()
            self.page.wait_for_selector(xpath_status_dropdown_value).click()
        except Exception as e:
            self.page.screenshot(path="Screenshots/accessory_status_dropdown.png")
            print(f"An error occurred: {str(e)}")  # This will now execute
            raise AssertionError(f"{str(e)}. Screenshot captured.")

    def click_make_id_dropdown_and_select_value(self):
        try:
            self.page.wait_for_selector(xpath_make_id).click()
            self.page.wait_for_selector(xpath_make_dropdown_value).click()
        except Exception as e:
            self.page.screenshot(path="Screenshots/make_id_dropdown_and_select_value.png")
            print(f"An error occurred: {str(e)}")  # This will now execute
            raise AssertionError(f"{str(e)}. Screenshot captured.")

    def click_model_id_dropdown_and_select_value(self):
        try:
            self.page.wait_for_selector(xpath_model_id).click()
            self.page.wait_for_selector(xpath_model_dropdown_value).click()
        except Exception as e:
            self.page.screenshot(path="Screenshots/model_id_dropdown_and_select_value.png")
            print(f"An error occurred: {str(e)}")  # This will now execute
            raise AssertionError(f"{str(e)}. Screenshot captured.")

    def click_warranty_start_date(self):
            try:
                self.page.wait_for_selector(xpath_warranty_start_date).click()
                self.page.wait_for_selector(xpath_date_visible)
                enabled_start_dates = self.page.query_selector_all(xpath_enabled_date)
                print("dates:::", enabled_start_dates)
                date_array = [date.inner_text() for date in enabled_start_dates]
                print("arrays date:", date_array)

                if not date_array:
                    raise Exception("No available start dates.")
                self.start_date = random.choice(date_array)
                print("start date:", self.start_date)
                self.page.click(f"text='{self.start_date}'")
                self.page.click('body')
            except Exception as e:
                self.page.screenshot(path="Screenshots/warranty_start_date.png")
                print(f"An error occurred: {str(e)}")  # This will now execute
                raise AssertionError(f"{str(e)}. Screenshot captured.")

    def click_warranty_end_date(self):
        try:
            if not self.start_date:
                raise Exception("Start date must be selected before end date.")

            self.page.wait_for_selector(xpath_warranty_end_date).click()
            self.page.wait_for_selector(xpath_date_visible)
            enabled_end_dates = self.page.query_selector_all(xpath_enabled_date)
            end_date_array = [date.inner_text() for date in enabled_end_dates]
            # Check and filter valid end dates
            valid_end_dates = [
                date for date in end_date_array
                if datetime.strptime(date, '%d') > datetime.strptime(self.start_date, '%d')
            ]
            if not valid_end_dates:
                raise Exception("No valid end dates available.")
            random_end_date = random.choice(valid_end_dates)
            self.page.click(f"text='{random_end_date}'")
            self.page.click('body')
        except Exception as e:
            self.page.screenshot(path="Screenshots/warranty_end_date.png")
            print(f"An error occurred: {str(e)}")  # This will now execute
            raise AssertionError(f"{str(e)}. Screenshot captured.")

    def verify_accessory_total_count(self):
        try:
            # Assuming 'self.page' and 'xpath_total_accessory_count' are defined in the class
            count = self.page.inner_text(xpath_total_accessory_count).strip()
            self.initial_count = int(count)  # Convert the count to an integer
            print('Accessory total Initial count:', self.initial_count)
            return self.initial_count
        except Exception as e:
            self.page.screenshot(path="Screenshots/accessory_count.png")
            print(f"An error occurred: {str(e)}")  # This will now execute
            raise AssertionError(f"{str(e)}. Screenshot captured.")



    def verify_accessory_cable_initial_count(self):
        try:
            count = self.page.inner_text(xpath_cable_initial_count).strip()
            # Extract the first sequence of digits from the string
            numeric_count = re.search(r'\d+', count).group()
            self.cable_initial_count = int(numeric_count)
            print("cable type:    ", type(self.cable_initial_count))
            print('Accessory cable initial count', self.cable_initial_count)
            return self.cable_initial_count
        except Exception as e:
            self.page.screenshot(path="Screenshots/accessory_cable_count.png")
            print(f"An error occurred: {str(e)}")  # This will now execute
            raise AssertionError(f"{str(e)}. Screenshot captured.")

    def click_submit_button_verify_updated_count(self):
        try:
            self.page.wait_for_selector(xpath_submit_button).click()
            time.sleep(3)

            # Get the updated total accessory count
            total_updated_count = self.page.inner_text(xpath_total_updated_accessory_count).strip()
            print('Total Accessory Updated count:', total_updated_count)

            # Ensure initial count is set
            if self.initial_count is None:
                raise ValueError("Initial count not set. Call verify_accessory_count first.")

            if int(total_updated_count) == self.initial_count + 1:
                print("The updated count is correct (+1).")
            else:
                print(f"Counts do not match. Initial count: {self.initial_count}, Updated count: {total_updated_count}")

            # Get the updated cable count
            total_cable_updated_count = self.page.inner_text(xpath_cable_update_count).strip()
            cable_updated_numeric_count = re.search(r'\d+', total_cable_updated_count).group()
            print('Total cable Accessory Updated count:', cable_updated_numeric_count)

            # Ensure cable initial count is set
            if self.cable_initial_count is None:
                raise ValueError("Cable initial count not set. Call verify_accessory_cable_count first.")

            if int(cable_updated_numeric_count) == self.cable_initial_count + 1:
                print("The updated cable count is correct (+1).")
            else:
                print(
                    f"Counts do not match. Initial count: {self.cable_initial_count}, Updated count: {cable_updated_numeric_count}")
        except Exception as e:
            self.page.screenshot(path="Screenshots/submit_button_verify_updated_count.png")
            print(f"An error occurred: {str(e)}")  # This will now execute
            raise AssertionError(f"{str(e)}. Screenshot captured.")