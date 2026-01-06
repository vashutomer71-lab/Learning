import time
from playwright.sync_api import Page, sync_playwright
from select import select

xpath_usermanagement_content= "//span[text()='User Management']"
xpath_usermanagement_attribute = "//span[contains(@class, 'MuiListItemText-primary') and text()='User Management']"
xpath_fleet_customer_menu = "//span[text()='Fleet Customer']"
xpath_add_fleetcustomer_button ="//h6[text()='ADD FLEET CUSTOMER']"
xpath_first_name ="//input[@name='firstName']"
xpath_last_name = "//input[@name='lastName']"
xpath_email = "//input[@name='email']"
xpath_mobile_number = "//input[@name='mobile']"
xpath_next_button = "//button[text()='Next']"
xpath_address1 = "//input[@name='address1']"
xpath_address2 = "//input[@name='address2']"
xpath_country ="(//div[@id='demo-simple-select-standard'])[1]"
xpath_country_dropdown_vaules = "//ul[@role='listbox']"
xpath_select_country_value= 'li[data-value="1"]'
xpath_state = "(//div[@id='demo-simple-select-standard'])[2]"
xpath_state_dropdown_vaules = "//ul[@role='listbox']"
xpath_select_state_values ="li[data-value='36']"
xpath_city = "//input[@name='city']"
xpath_zipcode = "//input[@name='postalCode']"



class FleetCustomerPage:

    def __init__(self, page: Page):
        self.page = page

    def click_user_management(self):
        self.page.wait_for_selector(xpath_usermanagement_content).click()


    def add_Fleet_customer(self):
        self.page.wait_for_selector(xpath_fleet_customer_menu).click()
        self.page.wait_for_selector(xpath_add_fleetcustomer_button).click()
        self.page.wait_for_selector(xpath_first_name).fill('Fleet Customer 1')
        self.page.wait_for_selector(xpath_last_name).fill('last Name')
        self.page.wait_for_selector(xpath_email).fill('test@yopmail.com')
        self.page.wait_for_selector(xpath_mobile_number).fill('+918232456785')
        self.page.wait_for_selector(xpath_next_button).click()
        self.page.wait_for_selector(xpath_address1).fill('HS-01')
        self.page.wait_for_selector(xpath_address2).fill('Sector -20')
        self.page.wait_for_selector(xpath_country).click()
        self.page.wait_for_selector(xpath_country_dropdown_vaules)
        self.page.click(xpath_select_country_value)
        self.page.wait_for_selector(xpath_state).click()
        self.page.wait_for_selector(xpath_state_dropdown_vaules)
        self.page.click(xpath_select_state_values)
        self.page.wait_for_selector(xpath_city).fill('Greater Noida')
        self.page.wait_for_selector(xpath_zipcode).fill('201305')








