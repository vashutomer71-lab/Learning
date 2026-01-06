import random
import time
import uuid
import string
from datetime import datetime
from playwright.sync_api import Page, sync_playwright
import re



xpath_assets_module = "//span[text()='Assets']"
xpath_accessory_tab = "//span[text()='Accessory Setup']"
xpath_accessory_button = "//h6[text()='ADD ACCESSORY']"
xpath_fleet_dropdown = "(//div[@id='demo-simple-select-standard'])[1]"
xpath_Fleet_dropdown_value = "//li[@data-value='12121']"
xpath_depot_name_dropdown = "(//div[@id='demo-simple-select-standard'])[2]"
xpath_depot_dropdown_value = "//li[@data-value='12127']"
xpath_accessory_dropdown = "(//div[@id='demo-simple-select-standard'])[3]"
xpath_accessory_dropdown_value = "//li[@data-value='Modem']"  ## Accessory type :> Modem
xpath_serial_number = "//input[@name='serial']"
xpath_device_id = "//input[@name='deviceId']"
xpath_status_dropdown = "(//div[@id='demo-simple-select-standard'])[4]"
xpath_status_dropdown_value = "//li[text()='Active']"
xpath_carrier_name = "//input[@name='carrier']"
xpath_Imei_number = "//input[@name='imei']"
xpath_Id_address = "//input[@name='ip']"
xpath_make_id = "(//div[@class='MuiInputBase-root MuiInput-root MuiInput-underline MuiInputBase-colorPrimary MuiInputBase-formControl css-1al598k'])[5]"
xpath_make_dropdown_value = "//li[text()='256 QAM']"
xpath_model_id = "(//div[@class='MuiInputBase-root MuiInput-root MuiInput-underline MuiInputBase-colorPrimary MuiInputBase-formControl css-1al598k'])[5]"
xpath_model_dropdown_value = "//li[text()='Sample Modem']"
xpath_Sim_number = "//input[@name='sim']"
xpath_modem_type = "(//div[@class='MuiInputBase-root MuiInput-root MuiInput-underline MuiInputBase-colorPrimary MuiInputBase-formControl css-1al598k'])[7]"
xpath_modem_type_value = "//li[@data-value=1]"
xpath_warranty_start_date = "(//button[@aria-label='Choose date'])[1]"
xpath_date_visible = ".MuiPickersDay-root"
xpath_enabled_date = "//button[@class='MuiButtonBase-root MuiPickersDay-root MuiPickersDay-dayWithMargin css-6exafu' and @aria-selected='false' and @role='gridcell']"
xpath_warranty_end_date = "//button[@aria-label='Choose date']"
xpath_calendar = "//div[@class='MuiDateCalendar-root css-5oi4td']"
xpath_Installation_Date = "(//button[@class='MuiButtonBase-root MuiIconButton-root MuiIconButton-edgeEnd MuiIconButton-sizeMedium css-slyssw'])[3]"
xpath_submit_button = "//button[@type='submit']"
xpath_total_accessory_count="(//div[@class='number'])[1]"
xpath_total_updated_accessory_count="(//div[@class='number'])[1]"
xpath_modem_initial_count = "(//div[@class='MuiGrid-root MuiGrid-item MuiGrid-grid-xs-2 text_component css-yi49kw'])[2]"
xpath_modem_update_count = "(//div[@class='MuiGrid-root MuiGrid-item MuiGrid-grid-xs-2 text_component css-yi49kw'])[2]"


class AccessoryPageModel:
    initial_count = None
    modem_initial_count = None
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
            self.page.screenshot(path="Screenshots/accessory_button.png")
            print(f"An error occurred: {str(e)}")  # This will now execute
            raise AssertionError(f"{str(e)}. Screenshot captured.")

    def click_fleet_name_dropdown_and_select_value(self):
        try:
            self.page.wait_for_selector(xpath_fleet_dropdown).click()
            self.page.wait_for_selector(xpath_Fleet_dropdown_value).click()
        except Exception as e:
            self.page.screenshot(path="Screenshots/fleet_drop_down_name.png")
            print(f"An error occurred: {str(e)}")  # This will now execute
            raise AssertionError(f"{str(e)}. Screenshot captured.")

    def click_depot_name_dropdown_and_select_value(self):
        try:
            self.page.wait_for_selector(xpath_depot_name_dropdown).click()
            self.page.wait_for_selector(xpath_depot_dropdown_value).click()
        except Exception as e:
            self.page.screenshot(path="Screenshots/depot_drop_down_name.png")
            print(f"An error occurred: {str(e)}")  # This will now execute
            raise AssertionError(f"{str(e)}. Screenshot captured.")

    def click_accessory_dropdown_and_select_value(self):
        try:
            self.page.wait_for_selector(xpath_accessory_dropdown).click()
            self.page.wait_for_selector(xpath_accessory_dropdown_value).click()
        except Exception as e:
            self.page.screenshot(path="Screenshots/accessory_category_drop_down.png")
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
            self.page.screenshot(path="Screenshots/accessory_status.png")
            print(f"An error occurred: {str(e)}")  # This will now execute
            raise AssertionError(f"{str(e)}. Screenshot captured.")

    def click_fill_carrier_name(self):
        try:
            self.page.wait_for_selector(xpath_carrier_name).click()
            # Generate random carrier name without using a function
            prefixes = ['Global', 'Trans', 'Swift', 'Sky', 'Air']
            suffixes = ['Express', 'Logistics', 'Cargo', 'Freight', 'Transport']
            random_carrier = f"{random.choice(prefixes)} {random.choice(suffixes)}"
            print(f"Random Carrier Name: {random_carrier}")
            self.page.fill(xpath_carrier_name, random_carrier)  # Fill the carrier name field
        except Exception as e:
            self.page.screenshot(path="Screenshots/carrier_name.png")
            print(f"An error occurred: {str(e)}")  # This will now execute
            raise AssertionError(f"{str(e)}. Screenshot captured.")

    def click_fill_imei_number(self):
        try:
            self.page.wait_for_selector(xpath_Imei_number).click()
            imei = ''.join([str(random.randint(0, 9)) for _ in range(14)])  # Generate first 14 digits
            checksum = sum(
                int(digit) if i % 2 == 0 else sum(divmod(int(digit) * 2, 10)) for i, digit in enumerate(imei)) * 9 % 10
            imei += str(checksum)  # Append the checksum as the 15th digit
            print(imei)
            self.page.fill(xpath_Imei_number, imei)
        except Exception as e:
            self.page.screenshot(path="Screenshots/imei_number.png")
            print(f"An error occurred: {str(e)}")  # This will now execute
            raise AssertionError(f"{str(e)}. Screenshot captured.")

    def click_fill_ip_address(self):
        try:
            self.page.wait_for_selector(xpath_Id_address).click()
            ip_address = '.'.join(str(random.randint(0, 255)) for _ in range(4))
            print(ip_address)  # Generated random IP address
            self.page.fill(xpath_Id_address, ip_address)
        except Exception as e:
            self.page.screenshot(path="Screenshots/ip_address.png")
            print(f"An error occurred: {str(e)}")  # This will now execute
            raise AssertionError(f"{str(e)}. Screenshot captured.")



    def click_make_id_dropdown_and_select_value(self):
        try:
            self.page.wait_for_selector(xpath_make_id).click()
            self.page.wait_for_selector(xpath_make_dropdown_value).click()
        except Exception as e:
            self.page.screenshot(path="Screenshots/make_id_drop_down.png")
            print(f"An error occurred: {str(e)}")  # This will now execute
            raise AssertionError(f"{str(e)}. Screenshot captured.")

    def click_model_id_dropdown_and_select_value(self):
        try:
            self.page.wait_for_selector(xpath_model_id).click()
            self.page.wait_for_selector(xpath_model_dropdown_value).click()
        except Exception as e:
            self.page.screenshot(path="Screenshots/model_id_drop_down.png")
            print(f"An error occurred: {str(e)}")  # This will now execute
            raise AssertionError(f"{str(e)}. Screenshot captured.")

    def click_fill_sim_number(self):
        try:
            self.page.wait_for_selector(xpath_Sim_number).click()
            sim_number = ''.join([str(random.randint(0, 9)) for _ in range(19)])  # Generate a 19-digit SIM number
            print(sim_number)  # Generated SIM number (ICCID)
            self.page.fill(xpath_Sim_number, sim_number)
            time.sleep(3)
        except Exception as e:
            self.page.screenshot(path="Screenshots/sim_number.png")
            print(f"An error occurred: {str(e)}")  # This will now execute
            raise AssertionError(f"{str(e)}. Screenshot captured.")

    def click_select_fill_modem_type(self):
        try:
            self.page.wait_for_selector(xpath_modem_type).click()
            self.page.wait_for_selector(xpath_modem_type_value).click()
        except Exception as e:
            self.page.screenshot(path="Screenshots/modem_type.png")
            print(f"An error occurred: {str(e)}")  # This will now execute
            raise AssertionError(f"{str(e)}. Screenshot captured.")


    def click_warranty_start_date(self):
        try:
            self.page.wait_for_selector(xpath_warranty_start_date).click()
            self.page.wait_for_selector(xpath_date_visible)
            enabled_start_dates = self.page.query_selector_all(xpath_enabled_date)
            date_array = [date.inner_text() for date in enabled_start_dates]
            if not date_array:
                raise Exception("No available start dates.")
            self.start_date = random.choice(date_array)
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

    def click_select_installation_date(self):
        try:
            self.page.wait_for_selector(xpath_Installation_Date).click()
            self.page.wait_for_selector(xpath_date_visible)
            enabled_start_dates = self.page.query_selector_all(xpath_enabled_date)
            date_array = [date.inner_text() for date in enabled_start_dates]
            if not date_array:
                raise Exception("No available start dates.")
            self.start_date = random.choice(date_array)
            self.page.click(f"text='{self.start_date}'")
            self.page.click('body')
        except Exception as e:
            self.page.screenshot(path="Screenshots/installation_date.png")
            print(f"An error occurred: {str(e)}")  # This will now execute
            raise AssertionError(f"{str(e)}. Screenshot captured.")



    def verify_accessory_count(self):
        try:
            # Assuming 'self.page' and 'xpath_total_accessory_count' are defined in the class
            count = self.page.inner_text(xpath_total_accessory_count).strip()
            self.initial_count = int(count)  # Convert the count to an integer
            print('Accessory Initial count:', self.initial_count)
            return self.initial_count
        except Exception as e:
            self.page.screenshot(path="Screenshots/accessory_count.png")
            print(f"An error occurred: {str(e)}")  # This will now execute
            raise AssertionError(f"{str(e)}. Screenshot captured.")



    def verify_accessory_modem_count(self):
        try:
            count = self.page.inner_text(xpath_modem_initial_count).strip()
            # Extract the first sequence of digits from the string
            numeric_count = re.search(r'\d+', count).group()
            self.modem_initial_count = int(numeric_count)
            print('Accessory modem initial count', self.modem_initial_count)
            return self.modem_initial_count
        except Exception as e:
            self.page.screenshot(path="Screenshots/accessory_modem_count.png")
            print(f"An error occurred: {str(e)}")  # This will now execute
            raise AssertionError(f"{str(e)}. Screenshot captured.")


    def click_submit_button_verify_updated_count(self):
        try:
            self.page.wait_for_selector(xpath_submit_button).click()
            time.sleep(3)
            total_updated_count = self.page.inner_text(xpath_total_updated_accessory_count).strip() # Get the updated count after waiting
            print('Total Accessory Updated count:', total_updated_count)
            if int(total_updated_count) == self.initial_count + 1:
                print("The updated count is correct (+1).")
            else:
                print(f"Counts do not match. Initial count: {self.initial_count}, Updated count: {total_updated_count}")

            total_modem_updated_count = self.page.inner_text(xpath_modem_update_count).strip()  # Get the updated count after waiting
            modem_updated_numeric_count = re.search(r'\d+', total_modem_updated_count).group()
            print('Total modem Accessory Updated count:', modem_updated_numeric_count)
            if int(modem_updated_numeric_count) == int(self.modem_initial_count) + 1:
                print("The updated count is correct (+1).")
            else:
                print(f"Counts do not match. Initial count: {self.modem_initial_count}, Updated count: {modem_updated_numeric_count}")
        except Exception as e:
            self.page.screenshot(path="Screenshots/submit_button_verify_updated_count.png")
            print(f"An error occurred: {str(e)}")  # This will now execute
            raise AssertionError(f"{str(e)}. Screenshot captured.")





