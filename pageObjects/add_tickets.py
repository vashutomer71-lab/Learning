import random
import string
import time

from playwright.sync_api import Page

#xpaths for the entity type depot
xpath_total_initial_tickets_count = "//div[@data-testid='total-ticket-count']"
xpath_total_update_tickets_count = "//div[@data-testid='total-ticket-count']"
xpath_total_depot_count_widget = "//div[@data-testid='total-depot-count']"
xpath_ticket_module = "//span[contains(text(), 'Tickets')]"
xpath_add_ticket_button = "//div[@class='add_icon']"
xpath_entity_type_dropdown = "(//div[@id='demo-simple-select-standard'])[1]"
xpath_entity_type_dropdown_value_depot = "//li[@data-value='1']"
xpath_ticket_type_dropdown = "(//div[@id='demo-simple-select-standard'])[2]"
xpath_ticket_type_dropdown_infrastructure = "//li[@data-value='1']"
xpath_description_field = "//input[@id='standard-basic' and @name='description']"
xpath_ticket_priority = "(//div[@id='demo-simple-select-standard'])[3]"
xpath_ticket_priority_dropdown_value_urgent = "//li[@data-value='2']"
xpath_fleet_Name_dropdown = "(//div[@id='demo-simple-select-standard'])[4]"
xpath_fleet_name_value_Singhania_Logistic = "//li[@data-value='12121']"
xpath_depot_Name_dropdown = "(//div[@id='demo-simple-select-standard'])[5]"
xpath_depot_Name_Singhania_DP_001 = "//li[@data-value='12127']"
xpath_assignee_to_dropdown = "(//div[@id='demo-simple-select-standard'])[6]"
xpath_assignee_to_dropdown_values_Mr_AnanndR = "//li[@data-value='188452']"
xpath_submit_button = "//button[@type='submit']"

#xpath for the entity type charger
xpath_total_charger_count_widget = "//div[@data-testid='total-charger-count']"
xpath_entity_type_dropdown_value_charger = "//li[@data-value='2']"
xpath_ticket_type_dropdown_values = "//ul[@class='MuiList-root MuiList-padding MuiMenu-list css-r8u8y9']"
xpath_ticket_type_dropdown_Charging_Station_Malfunctions = "//li[@data-value='7']"
xpath_fleet_Name_dropdown_value = "//ul[@class='MuiList-root MuiList-padding MuiMenu-list css-r8u8y9']"
xpath_charge_box_id_dropdown = "(//div[@id='demo-simple-select-standard'])[6]"
xpath_charge_box_id_dropdown_value = "//ul[@class='MuiList-root MuiList-padding MuiMenu-list css-r8u8y9']"
xpath_charge_box_id_DVS3321 = "//li[@data-value='DVS3321']"
xpath_assignee_to_dropdown_charger = "(//div[@id='demo-simple-select-standard'])[7]"
xpath_assignee_to_dropdown_values_charger = "//ul[@class='MuiList-root MuiList-padding MuiMenu-list css-r8u8y9']"
xpath_assignee_to_dropdown_values_Mr_AnanndR__charger = "//li[@data-value='188452']"

#xpath for the entity type vehicle
xpath_total_vehicle_count_widget = "//div[@data-testid='total-vehicle-count']"
xpath_entity_type_dropdown_value_vehicle = "//li[@data-value='3']"
xpath_ticket_type_dropdown_Regeneration_and_Braking = "//li[@data-value='19']"
xpath_vehicle_licence_plate_number_dropdown = "(//div[@id='demo-simple-select-standard'])[6]"
xpath_vehicle_licence_plate_number_HTM5FF2B3 = "//li[@data-value='HTM5FF2B3']"
xpath_assignee_to_dropdown_vehicle = "(//div[@id='demo-simple-select-standard'])[8]"
xpath_assignee_to_dropdown_values_Mr_AnanndR_vehicle = "//li[@data-value='188452']"

#xpaths for the entity type Driver
xpath_total_driver_count_widget = "//div[@data-testid='total-driver-count']"
xpath_entity_type_dropdown_value_driver = "//li[@data-value='4']"
xpath_ticket_type_dropdown_Route_and_Schedule_Adherence = "//li[@data-value='30']"
xpath_driver_name_dropdown = "(//div[@id='demo-simple-select-standard'])[5]"
xpath_vehicle_licence_plate_number_dropdown_driver = "(//div[@id='demo-simple-select-standard'])[6]"
xpath_assignee_to_dropdown_driver = "(//div[@id='demo-simple-select-standard'])[7]"
xpath_assignee_to_dropdown_values_index_one = "(//li[@class='MuiButtonBase-root MuiMenuItem-root MuiMenuItem-gutters MuiMenuItem-root MuiMenuItem-gutters select_menu_item css-1km1ehz'])[1]"

#xpaths for the entity type Journey
xpath_total_journey_count_widget = "//div[@data-testid='total-journey-count']"
xpath_entity_type_dropdown_value_journey = "//li[@data-value='5']"
xpath_journey_name_dropdown = "//div[@name='journeyId']"
xpath_journey_name_dropdown_value_index_one = "li[id='combo-box-demo-option-0']"
xpath_ticket_type_dropdown_journey = "(//div[@id='demo-simple-select-standard'])[3]"
xpath_ticket_type_dropdown_Vehicle_issue = "//li[@data-value='102']"
xpath_ticket_priority_journey = "(//div[@id='demo-simple-select-standard'])[4]"
xpath_ticket_priority_dropdown_value_urgent_journey = "//li[@data-value='2']"
xpath_depot_name_dropdown_journey = "(//div[@id='demo-simple-select-standard'])[6]"
xpath_depot_Name_Singhania_DP_001_journey = "//li[@data-value='12127']"
xpath_assignee_to_dropdown_journey = "(//div[@id='demo-simple-select-standard'])[9]"
xpath_assignee_to_dropdown_values_index_one_journey = "(//li[@class='MuiButtonBase-root MuiMenuItem-root MuiMenuItem-gutters MuiMenuItem-root MuiMenuItem-gutters select_menu_item css-1km1ehz'])[1]"

def generate_description_dynamic(min_length=20, max_length=200):
    # Generate a description that starts with a letter and is followed by alphanumeric, dot, hyphen, or space
    length = random.randint(min_length, max_length)
    first_char = random.choice(string.ascii_letters)
    # The rest of the string can be alphanumeric, space, dot, or hyphen
    valid_chars = string.ascii_letters + string.digits + " .-"
    rest_of_description = ''.join(random.choices(valid_chars, k=length - 1))
    description = first_char + rest_of_description
    return description


class AddTicket:
    initial_count_after_split = None
    ticket_depot_count = None
    ticket_charger_count = None
    ticket_vehicle_count = None
    ticket_driver_count = None
    ticket_journey_count = None

    def __init__(self, page: Page):
        self.page = page
        self.total_ticket_count_depots = None
        self.total_ticket_count_chargers = None
        self.total_ticket_count_vehicles = None
        self.total_ticket_count_drivers = None
        self.total_ticket_count_journeys = None


    def click_ticket_module(self):
        self.page.wait_for_selector(xpath_ticket_module).click()
        self.page.wait_for_timeout(500)

    def total_ticket_initial_count(self):
        initial_count = self.page.inner_text(xpath_total_initial_tickets_count)
        initial_count_after_split = int(initial_count.split("/")[-1].strip())
        self.initial_count_after_split = initial_count_after_split  # Store count in instance variable
        print("Total tickets initial count after split is:", self.initial_count_after_split)
        return self.initial_count_after_split

    #depot entity functions

    def total_ticket_for_depot_count_initial(self):
        ticket_depot_count = int(self.page.inner_text(xpath_total_depot_count_widget).split("/")[-1].strip())
        self.total_ticket_count_depots = ticket_depot_count
        print("Tickets for depots :", self.total_ticket_count_depots)
        return self.total_ticket_count_depots


    def click_add_ticket_button(self):
        self.page.wait_for_selector(xpath_add_ticket_button).click()

    def click_entity_type_dropdown(self):
        self.page.wait_for_selector(xpath_entity_type_dropdown).click()

    def select_entity_type_dropdown_value(self):
        depot_entity = self.page.locator(xpath_entity_type_dropdown_value_depot)
        depot_entity.click()

    def click_ticket_type_dropdown(self):
        self.page.wait_for_selector(xpath_ticket_type_dropdown).click()

    def select_ticket_type_dropdown_value(self):
        self.page.wait_for_selector(xpath_ticket_type_dropdown_infrastructure).click()

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

    def click_assignee_to_dropdown(self):
        self.page.wait_for_selector(xpath_assignee_to_dropdown).click()

    def select_assignee_to_dropdown_value(self):
        self.page.wait_for_selector(xpath_assignee_to_dropdown_values_Mr_AnanndR).click()

    def click_submit_button(self):
        try:
            self.page.wait_for_selector(xpath_submit_button).click()
            self.page.wait_for_timeout(1000)
            total_ticket_update_count = int(self.page.inner_text(xpath_total_update_tickets_count).split("/")[-1].strip())
            print("Total tickets update count is:", total_ticket_update_count)
        # Using the stored value of initial ticket count
            if total_ticket_update_count == self.initial_count_after_split + 1:
                print(
                f"The total ticket initial count {self.initial_count_after_split + 1} is matched with the total ticket update count {total_ticket_update_count}")
            else:
                print(
                f"The count is not matched. Initial count: {self.initial_count_after_split}, Updated count: {total_ticket_update_count}")

            total_ticket_update_count_depot = int(
            self.page.inner_text(xpath_total_depot_count_widget).split("/")[-1].strip())
            print("Total tickets depots update count is:", total_ticket_update_count_depot)
            if total_ticket_update_count_depot == self.total_ticket_count_depots + 1:
                print(
                f"The depot initial count {self.total_ticket_count_depots + 1} is matched with the total ticket depot update count {total_ticket_update_count_depot}")
            else:
                print(
                f"The count is not matched. Initial count: {self.initial_count_after_split}, Updated count: {total_ticket_update_count}")
        except Exception as e:
            self.page.screenshot(path="Screenshots/ticket_depot.png")
            print(f"An error occurred: {str(e)}")  # This will now execute
            raise AssertionError(f"{str(e)}. Screenshot captured.")

    # charger entity functions

    def total_ticket_for_charger_count_initial(self):
        ticket_charger_count = int(self.page.inner_text(xpath_total_charger_count_widget).split("/")[-1].strip())
        self.total_ticket_count_chargers = ticket_charger_count
        print("Tickets for charger :", self.total_ticket_count_chargers)
        return self.total_ticket_count_chargers

    def click_entity_type_dropdown_charger(self):
        self.page.wait_for_selector(xpath_entity_type_dropdown).click()
    def select_entity_type_dropdown_value_charger(self):
        charger_entity = self.page.locator(xpath_entity_type_dropdown_value_charger)
        charger_entity.click()
    def click_ticket_type_dropdown_charger(self):
        self.page.wait_for_selector(xpath_ticket_type_dropdown).click()
    def select_ticket_type_dropdown_value_charger(self):
        self.page.wait_for_selector(xpath_ticket_type_dropdown_Charging_Station_Malfunctions).click()
    def fill_description_field_charger(self):
        description = generate_description_dynamic()
        self.page.wait_for_selector(xpath_description_field).fill(description)
    def click_ticket_priority_dropdown_charger(self):
        self.page.wait_for_selector(xpath_ticket_priority).click()
    def select_ticket_priority_dropdown_value_urgent_charger(self):
        self.page.wait_for_selector(xpath_ticket_priority_dropdown_value_urgent).click()
    def click_fleet_name_dropdown_charger(self):
        self.page.wait_for_selector(xpath_fleet_Name_dropdown).click()

    def select_fleet_dropdown_value_charger(self):
        self.page.wait_for_selector(xpath_fleet_name_value_Singhania_Logistic).click()

    def click_depot_name_dropdown_charger(self):
        self.page.wait_for_selector(xpath_depot_Name_dropdown).click()

    def select_depot_dropdown_value_charger(self):
        self.page.wait_for_selector(xpath_depot_Name_Singhania_DP_001).click()

    def click_charge_box_id_dropdown(self):
        self.page.wait_for_selector(xpath_charge_box_id_dropdown).click()

    def select_charge_box_id_value(self):
        self.page.wait_for_selector(xpath_charge_box_id_DVS3321).click()

    def click_assignee_to_dropdown_charger(self):
        self.page.wait_for_selector(xpath_assignee_to_dropdown_charger).click()

    def select_assignee_to_dropdown_value_charger(self):
        self.page.wait_for_selector(xpath_assignee_to_dropdown_values_Mr_AnanndR__charger).click()

    def click_submit_button_charger(self):
        try:
            self.page.wait_for_selector(xpath_submit_button).click()
            self.page.wait_for_timeout(1000)
            total_ticket_update_count = int(self.page.inner_text(xpath_total_update_tickets_count).split("/")[-1].strip())
            print("Total tickets update count is:", total_ticket_update_count)
            # Using the stored value of initial ticket count
            if total_ticket_update_count == self.initial_count_after_split + 1:
                print(f"The total ticket initial count {self.initial_count_after_split+1} is matched with the total ticket update count {total_ticket_update_count}")
            else:
                print(f"The count is not matched. Initial count: {self.initial_count_after_split}, Updated count: {total_ticket_update_count}")

            total_ticket_update_count_charger = int(self.page.inner_text(xpath_total_charger_count_widget).split("/")[-1].strip())
            print("Total tickets chargers update count is:", total_ticket_update_count_charger)
            if total_ticket_update_count_charger== self.total_ticket_count_chargers +1:
                print(f"The chargers initial count {self.total_ticket_count_chargers+1} is matched with the total ticket chargers update count {total_ticket_update_count_charger}")
            else:
                print(
                f"The count is not matched. Initial count: {self.initial_count_after_split}, Updated count: {total_ticket_update_count}")
        except Exception as e:
            self.page.screenshot(path="Screenshots/ticket_charger.png")
            print(f"An error occurred: {str(e)}")  # This will now execute
            raise AssertionError(f"{str(e)}. Screenshot captured.")

   #vehicle entity functions

    def click_ticket_module_vehicle (self):
        self.page.wait_for_selector(xpath_ticket_module).click()
        self.page.wait_for_timeout(500)

    def total_ticket_for_vehicle_count_initial(self):
        ticket_vehicle_count = int(self.page.inner_text(xpath_total_vehicle_count_widget).split("/")[-1].strip())
        self.total_ticket_count_vehicles = ticket_vehicle_count
        print("Tickets for vehicle :", self.total_ticket_count_vehicles)
        return self.total_ticket_count_vehicles

    def click_add_ticket_button_vehicle (self):
        self.page.wait_for_selector(xpath_add_ticket_button).click()

    def select_entity_type_dropdown_value_vehicle (self):
        vehicle_entity = self.page.locator(xpath_entity_type_dropdown_value_vehicle)
        vehicle_entity.click()

    def select_ticket_type_dropdown_value_vehicle (self):
        self.page.wait_for_selector(xpath_ticket_type_dropdown_Regeneration_and_Braking).click()

    def click_vehicle_licence_plate_number_dropdown(self):
        self.page.wait_for_selector(xpath_vehicle_licence_plate_number_dropdown).click()

    def select_vehicle_licence_plate_number_value(self):
        self.page.wait_for_selector(xpath_vehicle_licence_plate_number_HTM5FF2B3).click()

    def click_assignee_to_dropdown_vehicle(self):
        self.page.wait_for_selector(xpath_assignee_to_dropdown_vehicle).click()

    def select_assignee_to_dropdown_value_vehicle(self):
        self.page.wait_for_selector(xpath_assignee_to_dropdown_values_Mr_AnanndR_vehicle).click()

    def click_submit_button_vehicle (self):
        try:
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
        except Exception as e:
            self.page.screenshot(path="Screenshots/ticket_vehicle.png")
            print(f"An error occurred: {str(e)}")  # This will now execute
            raise AssertionError(f"{str(e)}. Screenshot captured.")

    # driver entity functions

    def total_ticket_for_driver_count_initial(self):
        ticket_driver_count = int(self.page.inner_text(xpath_total_driver_count_widget).split("/")[-1].strip())
        self.total_ticket_count_drivers = ticket_driver_count
        print("Tickets initial count for driver  :", self.total_ticket_count_drivers)
        return self.total_ticket_count_drivers

    def click_add_ticket_button_driver(self):
        self.page.wait_for_selector(xpath_add_ticket_button).click()
    def select_entity_type_dropdown_value_driver(self):
        vehicle_entity = self.page.locator(xpath_entity_type_dropdown_value_driver)
        vehicle_entity.click()
    def select_ticket_type_dropdown_value_driver(self):
        self.page.wait_for_selector(xpath_ticket_type_dropdown_Route_and_Schedule_Adherence).click()

    def click_driver_name_dropdown(self):
        self.page.wait_for_selector(xpath_driver_name_dropdown).click()

    def select_driver_name_value_dropdown_index_one(self):
        self.page.wait_for_selector(xpath_assignee_to_dropdown_values_index_one).click()

    def click_assignee_to_dropdown_driver(self):
        self.page.wait_for_selector(xpath_assignee_to_dropdown_driver).click()

    def select_assignee_to_dropdown_value_driver(self):
        self.page.wait_for_selector(xpath_assignee_to_dropdown_values_index_one).click()

    def click_submit_button_driver(self):
        try:
            self.page.wait_for_selector(xpath_submit_button).click()
            self.page.wait_for_timeout(1000)
            total_ticket_update_count = int(
            self.page.inner_text(xpath_total_update_tickets_count).split("/")[-1].strip())
            print("Total tickets update count is:", total_ticket_update_count)
            # Using the stored value of initial ticket count
            if total_ticket_update_count == self.initial_count_after_split + 1:
                print(
                f"The total ticket initial count {self.initial_count_after_split + 1} is matched with the total ticket update count {total_ticket_update_count}")
            else:
                print(
                f"The count is not matched. Initial count: {self.initial_count_after_split}, Updated count: {total_ticket_update_count}")
            total_ticket_update_count_driver = int(
            self.page.inner_text(xpath_total_driver_count_widget).split("/")[-1].strip())
            print("Total tickets driver update count is:", total_ticket_update_count_driver)
            if total_ticket_update_count_driver == self.total_ticket_count_drivers + 1:
                print(
                f"The driver initial count {self.total_ticket_count_drivers + 1} is matched with the total ticket driver update count {total_ticket_update_count_driver}")
            else:
                print(
                f"The count is not matched. Initial count: {self.initial_count_after_split}, Updated count: {total_ticket_update_count}")
        except Exception as e:
            self.page.screenshot(path="Screenshots/ticket_driver.png")
            print(f"An error occurred: {str(e)}")  # This will now execute
            raise AssertionError(f"{str(e)}. Screenshot captured.")

    #Journey entity functions

    def total_ticket_for_journey_count_initial(self):
        ticket_journey_count = int(self.page.inner_text(xpath_total_journey_count_widget).split("/")[-1].strip())
        self.total_ticket_count_journeys = ticket_journey_count
        print("Tickets initial count for journey  :", self.total_ticket_count_journeys)
        return self.total_ticket_count_journeys

    def click_add_ticket_button_journey (self):
        self.page.wait_for_selector(xpath_add_ticket_button).click()
    def select_entity_type_dropdown_value_journey(self):
        vehicle_entity = self.page.locator(xpath_entity_type_dropdown_value_journey)
        vehicle_entity.click()
    def click_journey_name_dropdown(self):
        self.page.wait_for_selector(xpath_journey_name_dropdown).click()
    def select_journey_name_dropdown_value(self):
        self.page.wait_for_selector(xpath_journey_name_dropdown_value_index_one).click()
    def click_ticket_type_dropdown_journey(self):
        self.page.wait_for_selector(xpath_ticket_type_dropdown_journey).click()
    def select_ticket_type_dropdown_value_journey(self):
        self.page.wait_for_selector(xpath_ticket_type_dropdown_Vehicle_issue).click()
    def click_ticket_priority_dropdown_journey(self):
        self.page.wait_for_selector(xpath_ticket_priority_journey).click()
    def click_depot_name_dropdown_journey(self):
        self.page.wait_for_selector(xpath_depot_name_dropdown_journey).click()
    def select_depot_name_dropdown_value_journey(self):
        self.page.wait_for_selector(xpath_depot_Name_Singhania_DP_001_journey).click()
    def click_assignee_to_dropdown_journey(self):
        self.page.wait_for_selector(xpath_assignee_to_dropdown_journey).click()
    def select_assignee_to_dropdown_value_journey(self):
        self.page.wait_for_selector(xpath_assignee_to_dropdown_values_index_one_journey).click()

    def click_submit_button_journey(self):
        try:
            self.page.wait_for_selector(xpath_submit_button).click()
            self.page.wait_for_timeout(1000)
            total_ticket_update_count = int(self.page.inner_text(xpath_total_update_tickets_count).split("/")[-1].strip())
            print("Total tickets update count is:", total_ticket_update_count)
            # Using the stored value of initial ticket count
            if total_ticket_update_count == self.initial_count_after_split + 1:
                print(f"The total ticket initial count {self.initial_count_after_split+1} is matched with the total ticket update count {total_ticket_update_count}")
            else:
                print(f"The count is not matched. Initial count: {self.initial_count_after_split}, Updated count: {total_ticket_update_count}")
            total_ticket_update_count_journey = int(self.page.inner_text(xpath_total_journey_count_widget).split("/")[-1].strip())
            print("Total tickets journey update count is:", total_ticket_update_count_journey)
            if total_ticket_update_count_journey== self.total_ticket_count_journeys +1:
                print(f"The journey initial count {self.total_ticket_count_journeys+1} is matched with the total ticket journey update count {total_ticket_update_count_journey}")
            else:
                print(
                f"The count is not matched. Initial count: {self.initial_count_after_split}, Updated count: {total_ticket_update_count}")
        except Exception as e:
            self.page.screenshot(path="Screenshots/ticket_journey.png")
            print(f"An error occurred: {str(e)}")  # This will now execute
            raise AssertionError(f"{str(e)}. Screenshot captured.")






