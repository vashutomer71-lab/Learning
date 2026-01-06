import random
import string
from playwright.sync_api import Page

xpath_total_initial_tickets_count = "//div[@data-testid='total-ticket-count']"
xpath_total_update_tickets_count = "//div[@data-testid='total-ticket-count']"
xpath_total_vehicle_count_widget = "//div[@data-testid='total-vehicle-count']"
xpath_ticket_module = "//span[contains(text(), 'Tickets')]"
xpath_add_ticket_button = "//div[@class='add_icon']"
xpath_entity_type_dropdown = "(//div[@id='demo-simple-select-standard'])[1]"
xpath_entity_type_dropdown_value = "//ul[@class='MuiList-root MuiList-padding MuiMenu-list css-r8u8y9']"
xpath_entity_type_dropdown_value_vehicle = "//li[@data-value='3']"
xpath_ticket_type_dropdown = "(//div[@id='demo-simple-select-standard'])[2]"
xpath_ticket_type_dropdown_values = "//ul[@class='MuiList-root MuiList-padding MuiMenu-list css-r8u8y9']"
xpath_ticket_type_dropdown_Regeneration_and_Braking = "//li[@data-value='19']"
xpath_description_field = "//input[@id='standard-basic' and @name='description']"
xpath_ticket_priority = "(//div[@id='demo-simple-select-standard'])[3]"
xpath_ticket_priority_dropdown_value_urgent = "//li[@data-value='2']"
xpath_fleet_Name_dropdown = "(//div[@id='demo-simple-select-standard'])[4]"
xpath_fleet_Name_dropdown_value = "//ul[@class='MuiList-root MuiList-padding MuiMenu-list css-r8u8y9']"
xpath_fleet_name_value_Singhania_Logistic = "//li[@data-value='12121']"
xpath_depot_Name_dropdown = "(//div[@id='demo-simple-select-standard'])[5]"
xpath_depot_Name_dropdown_value = "//ul[@class='MuiList-root MuiList-padding MuiMenu-list css-r8u8y9']"
xpath_depot_Name_Singhania_DP_001 = "//li[@data-value='12127']"
xpath_vehicle_licence_plate_number_dropdown = "(//div[@id='demo-simple-select-standard'])[6]"
xpath_vehicle_licence_plate_number_dropdown_value = "//ul[@class='MuiList-root MuiList-padding MuiMenu-list css-r8u8y9']"
xpath_vehicle_licence_plate_number_HTM5FF2B3 = "//li[@data-value='HTM5FF2B3']"
xpath_assignee_to_dropdown = "(//div[@id='demo-simple-select-standard'])[8]"
xpath_assignee_to_dropdown_values = "//ul[@class='MuiList-root MuiList-padding MuiMenu-list css-r8u8y9']"
xpath_assignee_to_dropdown_values_Mr_AnanndR = "//li[@data-value='188452']"
xpath_submit_button = "//button[@type='submit']"


def generate_description_dynamic(min_length=20, max_length=200):
    # Generate a description that starts with a letter and is followed by alphanumeric, dot, hyphen, or space
    length = random.randint(min_length, max_length)
    first_char = random.choice(string.ascii_letters)
    # The rest of the string can be alphanumeric, space, dot, or hyphen
    valid_chars = string.ascii_letters + string.digits + " .-"
    rest_of_description = ''.join(random.choices(valid_chars, k=length - 1))
    description = first_char + rest_of_description
    return description


class AddTicketVehicleEntity:
    initial_count_after_split = None
    ticket_vehicle_count = None


    def __init__(self, page: Page):
        self.total_ticket_count_vehicles = None
        self.page = page

    def click_ticket_module(self):
        self.page.wait_for_selector(xpath_ticket_module).click()
        self.page.wait_for_timeout(500)

    def total_ticket_initial_count(self):
        initial_count = self.page.inner_text(xpath_total_initial_tickets_count)
        initial_count_after_split = int(initial_count.split("/")[-1].strip())
        self.initial_count_after_split = initial_count_after_split  # Store count in instance variable
        print("Total tickets initial count after split is:", self.initial_count_after_split)
        return self.initial_count_after_split

    def total_ticket_for_vehicle_count_initial(self):
        ticket_vehicle_count = int(self.page.inner_text(xpath_total_vehicle_count_widget).split("/")[-1].strip())
        self.total_ticket_count_vehicles = ticket_vehicle_count
        print("Tickets for vehicle :", self.total_ticket_count_vehicles)
        return self.total_ticket_count_vehicles


    def click_add_ticket_button(self):
        self.page.wait_for_selector(xpath_add_ticket_button).click()

    def click_entity_type_dropdown(self):
        self.page.wait_for_selector(xpath_entity_type_dropdown).click()

    def select_entity_type_dropdown_value(self):
        vehicle_entity = self.page.locator(xpath_entity_type_dropdown_value_vehicle)
        vehicle_entity.click()

    def click_ticket_type_dropdown(self):
        self.page.wait_for_selector(xpath_ticket_type_dropdown).click()

    def select_ticket_type_dropdown_value(self):
        self.page.wait_for_selector(xpath_ticket_type_dropdown_Regeneration_and_Braking).click()

    def fill_description_field(self):
        description = generate_description_dynamic()
        self.page.wait_for_selector(xpath_description_field).fill(description)

    def click_ticket_priority_dropdown(self):
        self.page.wait_for_selector(xpath_ticket_priority).click()

    def select_ticket_priority_dropdown_value_urgent(self):
        self.page.wait_for_selector(xpath_ticket_priority_dropdown_value_urgent).click()

    def click_fleet_name_dropdown(self):
        self.page.wait_for_selector(xpath_fleet_Name_dropdown).click()

    def select_fleet_dropdown_value(self):
        self.page.wait_for_selector(xpath_fleet_name_value_Singhania_Logistic).click()

    def click_depot_name_dropdown(self):
        self.page.wait_for_selector(xpath_depot_Name_dropdown).click()

    def select_depot_dropdown_value(self):
        self.page.wait_for_selector(xpath_depot_Name_Singhania_DP_001).click()

    def click_vehicle_licence_plate_number_dropdown(self):
        self.page.wait_for_selector(xpath_vehicle_licence_plate_number_dropdown).click()

    def select_vehicle_licence_plate_number_value(self):
        self.page.wait_for_selector(xpath_vehicle_licence_plate_number_HTM5FF2B3).click()

    def click_assignee_to_dropdown(self):
        self.page.wait_for_selector(xpath_assignee_to_dropdown).click()

    def select_assignee_to_dropdown_value(self):
        self.page.wait_for_selector(xpath_assignee_to_dropdown_values_Mr_AnanndR).click()

    def click_submit_button(self):
        self.page.wait_for_selector(xpath_submit_button).click()
        self.page.wait_for_timeout(1000)
        total_ticket_update_count = int(self.page.inner_text(xpath_total_update_tickets_count).split("/")[-1].strip())
        print("Total tickets update count is:", total_ticket_update_count)
        # Using the stored value of initial ticket count
        if total_ticket_update_count == self.initial_count_after_split + 1:
            print(f"The total ticket initial count {self.initial_count_after_split+1} is matched with the total ticket update count {total_ticket_update_count}")
        else:
            print(f"The count is not matched. Initial count: {self.initial_count_after_split}, Updated count: {total_ticket_update_count}")

        total_ticket_update_count_vehicle = int(self.page.inner_text(xpath_total_vehicle_count_widget).split("/")[-1].strip())
        print("Total tickets Vehicles update count is:", total_ticket_update_count_vehicle)
        if total_ticket_update_count_vehicle== self.total_ticket_count_vehicles +1:
            print(f"The Vehicles initial count {self.total_ticket_count_vehicles+1} is matched with the total ticket Vehicles update count {total_ticket_update_count_vehicle}")
        else:
            print(
                f"The count is not matched. Initial count: {self.initial_count_after_split}, Updated count: {total_ticket_update_count}")



