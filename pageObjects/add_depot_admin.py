import time

from playwright.sync_api import Page, sync_playwright


class CreateDepotAdmin:
    user_management_xpath = "//*[contains(text(),'User Management')]"
    Depot_admin_xpath = "//span[contains(text(),'Depot Admin')]"
    add_depot_admin_xpath = "//div[@class='add_assets']"
    fleet_name_xpath = "//div[@id='demo-simple-select-standard']"
    fleet_name_input_xpath = "//li[contains(text(),'Tomer Fleet')]"
    Depot_name_xpath = "//div[@id='mui-component-select-operatorUserMapperCommand']"
    depot_name_input_xpath = "//li[@data-value='NPX Depot']"
    first_name_xpath = "(//input[@class='MuiInputBase-input MuiInput-input css-mnn31'])[1]"
    last_name_xpath = "//input[@name='lastName']"
    email_xpath = "//input[@name='email']"
    mobile_xpath = "//input[@name='mobile']"
    next_xpath = "//*[contains(text(),'Next')]"
    address1_xpath = "//input[@name='address1']"
    address2_xpath = "//input[@name='address2']"
    country_xpath = "(//div[@id='demo-simple-select-standard'])[1]"
    choose_country_xpath = "//*[contains(text(),'INDIA')]"
    state_xpath = "(//div[@id= 'demo-simple-select-standard'])[2]"
    select_state_xpath = "//*[contains(text(),'DELHI')]"
    city_xpath = "//input[@name='city']"
    zipcode_xpath = "//input[@name='postalCode']"
    submit_xpath = "//button[@type='submit']"
    input_box_xpath = "//input[@id='inbox_field']"

    def __init__(self, page: Page):
        self.initial_count = None
        self.page = page

    def click_add_depot_admin(self):
        self.page.click(self.user_management_xpath)
        self.page.click(self.Depot_admin_xpath)
        self.page.click(self.add_depot_admin_xpath)
        self.page.click(self.fleet_name_xpath)
        self.page.click(self.fleet_name_input_xpath)

    def click_depot_name(self):
        self.page.wait_for_selector("(//div[@class='MuiFormControl-root form_box css-13sljp9'])[3]").click()
        self.page.wait_for_selector("//li[@data-value='NPX Depot']").click()
        self.page.click('body')


    def first_name(self):
        self.page.click(self.first_name_xpath)
        self.page.click(self.first_name_xpath)
        self.page.fill(self.first_name_xpath, "Decent")

    def last_name(self):
        self.page.wait_for_selector(self.last_name_xpath, state='visible')
        self.page.fill(self.last_name_xpath, "Ford")

    def email(self, email):
        self.page.wait_for_selector(self.email_xpath, state='visible')
        self.page.fill(self.email_xpath, email)

    def mobile(self, number):
        self.page.wait_for_selector(self.mobile_xpath, state='visible')
        self.page.fill(self.mobile_xpath, number)
        self.page.click(self.next_xpath)

    def address(self, address, address2, city):
        self.page.wait_for_selector(self.address1_xpath, state='visible')
        self.page.fill(self.address1_xpath, address)
        self.page.click(self.address1_xpath)
        self.page.fill(self.address2_xpath, address2)
        self.page.click(self.address2_xpath)
        self.page.click(self.country_xpath)
        self.page.click(self.choose_country_xpath)
        self.page.click(self.state_xpath)
        self.page.click(self.select_state_xpath)
        self.page.fill(self.city_xpath, city)
        self.page.click(self.city_xpath)
        self.page.fill(self.zipcode_xpath, "110044")
        self.page.click(self.submit_xpath)

    def mailinator(self):
        self.page.click(self.input_box_xpath)

