import time
# from Demos.mmapfile_demo import page_size
from playwright.sync_api import sync_playwright, Page
from Test_Cases.conftest import db_connection, elaam_prod
from Utilities.ReadProperties import ReadConfig
from tabulate import tabulate
import re
import random
import allure

# url = ReadConfig.getBackEndUrl()


xpath_dashboard_menu = "//li/a[normalize-space(text())='Mumin Dashboard']"
xpath_dashboard_heading = "//h1[normalize-space(text())='Mumin Dashboard']"
xpath_Total_Niyat_tile = "(//div[@class='box1 ng-star-inserted'])[1]"
xpath_Active_Niyat_tile = "(//div[@class='box1 ng-star-inserted'])[2]"
xpath_Approval_pending_Niyat_tile = "(//div[@class='box1 ng-star-inserted'])[3]"
xpath_Completed_Niyat_tile = "(//div[@class='box1 ng-star-inserted'])[4]"
xpath_duration_dropdown = "#mat-select-value-1"
xpath_1_month = "//span[normalize-space(text())='Last 1 Month']"
xpath_3_month = "//span[normalize-space(text())='Last 3 Months']"
xpath_6_month = "//span[normalize-space(text())='Last 6 Months']"
xpath_1_year = "//span[normalize-space(text())='1 year']"
xpath_total_trophy_count = "(//p[contains(text(),'')])[11]"
xpath_trophies_redeemed= "//p[contains(text(),'Trophies Redeemed')]"
xpath_pagination_text= "//div[@class='mat-paginator-range-actions']"
xpath_umoor_column = "//tbody[@role='rowgroup']//tr//td[8]"
xpath_search_field = "(//div[contains(@class,'mat-form-field-infix')])[2]"
xpath_search_dropdown="//mat-option//span"
DROPDOWN_UMOOR_OPTION_XPATH = "//mat-option//span[normalize-space()='{value}']"
xpath_row_after_search = "//tbody[@role='rowgroup']//tr//td[8][normalize-space() = '{value}']"
xpath_niyat_question = "//tbody/tr[1]/td[3]"
xpath_view_icon = "//tbody/tr[1]/td[9]//mat-icon[@title='Info']"
xpath_niyat_question_info_page = "//div[@class='info_txt']"
xpath_back_button = "//button[normalize-space(text())='Back']"

xpath_approval_pending_widget = "//p[normalize-space()='approval pending']"
xpath_send_message_button = "(//button[normalize-space()='Send Message'])[1]"
xpath_subject_field  = "//input[@formcontrolname='subject']"
xpath_message_text_field = "//textarea[@formcontrolname='messageText']"
xpath_send_button = "//button[normalize-space()='Send']"
xpath_send_message_success_message = "//div[contains(@class,'toast') or contains(@class,'mat-snack-bar')]"

xpath_item_per_page_drop_down = "(//div[starts-with(@id,'mat-select-value-')])[2]"
xpath_options = "//mat-option[@role='option']//span"
xpath_random_value = "//mat-option[@role='option']//span[normalize-space()="
xpath_row_count = "//tbody/tr"

xpath_request_for_update = "//button[contains(normalize-space(),'Request For Update')]"
xpath_mubarak_text = "//button[contains(normalize-space(), 'MUBARAK')]"
xpath_niyat_info_pending_status = "(//span[contains(normalize-space(),'Pending')])[1]"

# List of adjectives, nouns, verbs to create natural-looking sentences
adjectives = ["Amazing", "Creative", "Brilliant", "Innovative", "Smart", "Quick", "Elegant"]
nouns = ["Project", "Task", "Message", "Report", "Feature", "Idea", "Update"]
verbs = ["delivered", "created", "completed", "sent", "processed", "reviewed", "approved"]
objects = ["successfully", "with excellence", "smoothly", "with precision", "effectively"]

def generate_unique_subject():
    return f"{random.choice(adjectives)} {random.choice(nouns)}"

def generate_unique_message_text():
    sentence = f"The {random.choice(nouns)} was {random.choice(verbs)} {random.choice(objects)}."
    return sentence




class MuminDashboardPage:

    def __init__(self, page:Page):
        self.page = page
        self.expected_path = "/catalogue"

    def click_dashboard_menu(self):
        self.page.wait_for_selector(xpath_dashboard_menu).click()

    def verify_mumin_dashboard_heading(self):
        dashboard_text_frontend = self.page.inner_text(xpath_dashboard_heading)
        return dashboard_text_frontend


    def verify_dashboard_tile_all_filter(self, elaam_prod, its_id):
        self.page.wait_for_timeout(2000)
        total_niyat_count_widget = int(next(line for line in self.page.inner_text(xpath_Total_Niyat_tile).splitlines() if line.strip()))
        active_niyat_count_widget = int(next(line for line in self.page.inner_text(xpath_Active_Niyat_tile).splitlines() if line.strip()))
        approval_pending_niyat_count_widget = int(next(line for line in self.page.inner_text(xpath_Approval_pending_Niyat_tile).splitlines() if line.strip()))
        completed_niyat_count_widget = int(next(line for line in self.page.inner_text(xpath_Completed_Niyat_tile).splitlines() if line.strip()))
        # Execute SQL query to fetch data from the database
        # total_niyat_query = "all_niyat_tile_count_query"
        headers, result = elaam_prod("all_niyat_tile_count_query", its_id)
        print("total niya query:", result)
        db_table_view= tabulate(result, headers=headers, tablefmt="grid")   # Display the database results in a tabular format
        # Process database results to store counts by status
        total_niyat_count_db = result[0][headers.index('total_count')]
        active_count_db = result[0][headers.index('active_count')]
        completed_count_db = result[0][headers.index('completed_count')]
        approval_pending_db = result[0][headers.index('approval_pending_count')]
        deactivated_db = result[0][headers.index('deactivated_count')]
        total_niyat_count_add_all_status = active_count_db + completed_count_db + approval_pending_db + deactivated_db
        
        return total_niyat_count_widget, total_niyat_count_db,active_niyat_count_widget,active_count_db,approval_pending_niyat_count_widget,approval_pending_db,completed_niyat_count_widget,completed_count_db,total_niyat_count_add_all_status,total_niyat_count_db 

    def click_duration_drop_down_and_select_1_month_filter(self):
        self.page.locator(xpath_duration_dropdown).click()
        self.page.wait_for_selector("body").press("ControlOrMeta+Shift+I")       
        # self.page.get_by_role("option", name="Last 1 Month").click()
        self.page.locator(xpath_1_month).click()
    #     self.page.keyboard.press("Escape")
    

    def verify_dashboard_tile_1_month_filter(self, elaam_prod, its_id):
        self.page.wait_for_timeout(3000)
        total_niyat_count_widget_for_1_month = int(next(line for line in self.page.inner_text(xpath_Total_Niyat_tile).splitlines() if line.strip()))
        active_niyat_count_widget_for_1_month  = int(next(line for line in self.page.inner_text(xpath_Active_Niyat_tile).splitlines() if line.strip()))
        approval_pending_niyat_count_widget_for_1_month = int(next(line for line in self.page.inner_text(xpath_Approval_pending_Niyat_tile).splitlines() if line.strip()))
        completed_niyat_count_widget_for_1_month = int(next(line for line in self.page.inner_text(xpath_Completed_Niyat_tile).splitlines() if line.strip()))
        # Execute SQL query to fetch data from the database
        # total_niyat_query_for_1_month= "1_month_niyat_tile_count_query"
        headers, result = elaam_prod("1_month_niyat_tile_count_query", its_id)
        print("total niya query for 1 month:", result)
        db_table_view= tabulate(result, headers=headers, tablefmt="grid")   # Display the database results in a tabular format
        # Process database results to store counts by status
        total_niyat_count_db_for_1_month = result[0][headers.index('total_count')]
        active_count_db = result[0][headers.index('active_count')]
        completed_count_db = result[0][headers.index('completed_count')]
        approval_pending_db = result[0][headers.index('approval_pending_count')]
        deactivated_db = result[0][headers.index('deactivated_count')]
        total_niyat_count_add_all_status = active_count_db + completed_count_db + approval_pending_db + deactivated_db
        return total_niyat_count_widget_for_1_month,total_niyat_count_db_for_1_month,active_niyat_count_widget_for_1_month,active_count_db,approval_pending_niyat_count_widget_for_1_month,approval_pending_db,completed_niyat_count_widget_for_1_month,completed_count_db,total_niyat_count_add_all_status


    def click_duration_drop_down_and_select_3_month_filter(self):
        self.page.locator(xpath_duration_dropdown).click()
        self.page.locator("body").press("ControlOrMeta+Shift+I")
        # self.page.get_by_role("option", name="Last 1 Month").click()
        self.page.locator(xpath_3_month).click()
        self.page.keyboard.press("Escape")

    def verify_dashboard_tile_3_month_filter(self, elaam_prod, its_id):
        self.page.wait_for_timeout(3000)
        total_niyat_count_widget_for_3_month = int(next(line for line in self.page.inner_text(xpath_Total_Niyat_tile).splitlines() if line.strip()))
        active_niyat_count_widget_for_3_month  = int(next(line for line in self.page.inner_text(xpath_Active_Niyat_tile).splitlines() if line.strip()))
        approval_pending_niyat_count_widget_for_3_month = int(next(line for line in self.page.inner_text(xpath_Approval_pending_Niyat_tile).splitlines() if line.strip()))
        completed_niyat_count_widget_for_3_month = int(next(line for line in self.page.inner_text(xpath_Completed_Niyat_tile).splitlines() if line.strip()))
        # Execute SQL query to fetch data from the database        
        headers, result = elaam_prod("3_month_niyat_tile_count_query", its_id)
        print("total niya query for 3 months:", result)
        db_table_view= tabulate(result, headers=headers, tablefmt="grid")   # Display the database results in a tabular format
        # Process database results to store counts by status
        total_niyat_count_db_for_3_month = result[0][headers.index('total_count')]
        active_count_db = result[0][headers.index('active_count')]
        completed_count_db = result[0][headers.index('completed_count')]
        approval_pending_db = result[0][headers.index('approval_pending_count')]
        deactivated_db = result[0][headers.index('deactivated_count')]
        total_niyat_count_add_all_status = active_count_db + completed_count_db + approval_pending_db + deactivated_db
        return total_niyat_count_widget_for_3_month,total_niyat_count_db_for_3_month,active_niyat_count_widget_for_3_month,active_count_db, approval_pending_niyat_count_widget_for_3_month,approval_pending_db,completed_niyat_count_widget_for_3_month,completed_count_db,total_niyat_count_add_all_status,total_niyat_count_db_for_3_month

    def click_duration_drop_down_and_select_6_months_filter(self):
        self.page.locator(xpath_duration_dropdown).click()
        self.page.locator("body").press("ControlOrMeta+Shift+I")
        # self.page.get_by_role("option", name="Last 1 Month").click()
        self.page.locator(xpath_6_month).click()
        self.page.keyboard.press("Escape")

    def verify_dashboard_tile_6_month_filter(self, elaam_prod, its_id):
        self.page.wait_for_timeout(3000)
        total_niyat_count_widget_for_6_month = int(next(line for line in self.page.inner_text(xpath_Total_Niyat_tile).splitlines() if line.strip()))
        active_niyat_count_widget_for_6_month  = int(next(line for line in self.page.inner_text(xpath_Active_Niyat_tile).splitlines() if line.strip()))
        approval_pending_niyat_count_widget_for_6_month = int(next(line for line in self.page.inner_text(xpath_Approval_pending_Niyat_tile).splitlines() if line.strip()))
        completed_niyat_count_widget_for_6_month = int(next(line for line in self.page.inner_text(xpath_Completed_Niyat_tile).splitlines() if line.strip()))
        # Execute SQL query to fetch data from the database
        
        headers, result = elaam_prod("6_month_niyat_tile_count_query", its_id)
        db_table_view= tabulate(result, headers=headers, tablefmt="grid")   # Display the database results in a tabular format
        # Process database results to store counts by status
        total_niyat_count_db_for_6_month = result[0][headers.index('total_count')]
        active_count_db = result[0][headers.index('active_count')]
        completed_count_db = result[0][headers.index('completed_count')]
        approval_pending_db = result[0][headers.index('approval_pending_count')]
        deactivated_db = result[0][headers.index('deactivated_count')]
        total_niyat_count_add_all_status = active_count_db + completed_count_db + approval_pending_db + deactivated_db
        return total_niyat_count_widget_for_6_month, total_niyat_count_db_for_6_month,active_niyat_count_widget_for_6_month,active_count_db,approval_pending_niyat_count_widget_for_6_month,approval_pending_db,completed_niyat_count_widget_for_6_month,completed_count_db,total_niyat_count_add_all_status,total_niyat_count_db_for_6_month


    def click_duration_drop_down_and_select_1_year_filter(self):
        self.page.locator(xpath_duration_dropdown).click()
        self.page.locator("body").press("ControlOrMeta+Shift+I")
        self.page.locator(xpath_1_year).click()
        self.page.keyboard.press("Escape")

    def verify_dashboard_tile_1_year_filter(self, elaam_prod, its_id):
        self.page.wait_for_timeout(5000)
        total_niyat_count_widget_for_1_year = int(next(line for line in self.page.inner_text(xpath_Total_Niyat_tile).splitlines() if line.strip()))
        active_niyat_count_widget_for_1_year  = int(next(line for line in self.page.inner_text(xpath_Active_Niyat_tile).splitlines() if line.strip()))
        approval_pending_niyat_count_widget_for_1_year = int(next(line for line in self.page.inner_text(xpath_Approval_pending_Niyat_tile).splitlines() if line.strip()))
        completed_niyat_count_widget_for_1_year = int(next(line for line in self.page.inner_text(xpath_Completed_Niyat_tile).splitlines() if line.strip()))
        # Execute SQL query to fetch data from the database
        
        headers, result = elaam_prod("1_year_niyat_tile_count_query", its_id)
        db_table_view= tabulate(result, headers=headers, tablefmt="grid")   # Display the database results in a tabular format
        # Process database results to store counts by status
        total_niyat_count_db_for_1_year = result[0][headers.index('total_count')]
        active_count_db = result[0][headers.index('active_count')]
        completed_count_db = result[0][headers.index('completed_count')]
        approval_pending_db = result[0][headers.index('approval_pending_count')]
        deactivated_db = result[0][headers.index('deactivated_count')]
        total_niyat_count_add_all_status = active_count_db + completed_count_db + approval_pending_db + deactivated_db
        return total_niyat_count_widget_for_1_year, total_niyat_count_db_for_1_year,active_niyat_count_widget_for_1_year,active_count_db, approval_pending_niyat_count_widget_for_1_year,approval_pending_db,completed_niyat_count_widget_for_1_year,completed_count_db,total_niyat_count_add_all_status,total_niyat_count_db_for_1_year


    def get_total_trophies_counts(self, elaam_prod, its_id):
        """Fetch trophy counts from two locators and return as separate variables."""

        def get_number(loc):
            # Wait until element has a number
            while not (match := re.search(r"\d+", self.page.locator(loc).inner_text())):
                self.page.wait_for_timeout(200)
            return int(match.group())
        # Fetch counts
        total_trophys_count_from_ui = get_number(xpath_total_trophy_count)
        # return main_count,extra_count
        headers, result = elaam_prod("mumin_total_trophy_reward", its_id)
        db_table_format = tabulate(result, headers=headers, tablefmt="grid")
        total_trophy_count_from_db = result[0][0]
        return total_trophy_count_from_db, total_trophys_count_from_ui


    def get_trophies_redeemed_counts(self, elaam_prod, its_id):
        """Fetch trophy counts from two locators and return as separate variables."""
        def get_number(loc):
            # Wait until element has a number
            while not (match := re.search(r"\d+", self.page.locator(loc).inner_text())):
                self.page.wait_for_timeout(200)
            return int(match.group())
        # Fetch counts
        troghies_reedeemd_count_from_ui = get_number(xpath_trophies_redeemed)
        # return main_count,extra_count
        total_trophies_redeemed_count_query= "mumin_trophies_redeemed"
        headers, result = elaam_prod(total_trophies_redeemed_count_query, its_id)
        db_table_format = tabulate(result, headers=headers, tablefmt="grid")
        total_trophies_redeemed_count_from_db = result[0][0]
        return total_trophies_redeemed_count_from_db,troghies_reedeemd_count_from_ui


    def click_redeem_now_and_verify_navigation(self):
        """Click Redeem Now, capture URL, and validate it contains expected path"""
        self.page.get_by_role("button", name="Redeem Now").click()
        # Wait until URL contains expected path
        self.page.wait_for_url(f"**{self.expected_path}")
        current_url = self.page.url
        return current_url


    def get_total_niyat_count_and_match_pagination_count(self):
        total_niyat_count_widget = int(next(line for line in self.page.inner_text(xpath_Total_Niyat_tile).splitlines() if line.strip()))
        pagination_text = self.page.wait_for_selector(xpath_pagination_text).inner_text()
        # Split by 'of' and take the last part, strip spaces, convert to int
        total_count_pagination = int(pagination_text.split("of")[-1].strip())
        return total_count_pagination, total_niyat_count_widget

    def search_by_dynamic_umoor_name_and_validate_with_pagination_count_after_search_UI_DB(self,elaam_prod, its_id):
        """Pick ITS ID from first row, search it, and validate results"""
        umoor_elements = self.page.locator(xpath_umoor_column) # --- 1) collect all UMOOR values ---
        umoor_list = [v.strip() for v in umoor_elements.all_inner_texts() if v.strip()]
        print("Collected UMOOR values:", umoor_list)
        if not umoor_list:
            print("No UMOOR values found!")
            return
        chosen = random.choice(umoor_list)   # --- 2) pick dynamically (example: random) ---
        print("Chosen UMOOR to search:", chosen)
        search_field = self.page.locator(xpath_search_field)   # --- 3) perform search ---
        search_field.click()         
        self.page.wait_for_selector(xpath_search_dropdown)   # wait for dropdown options    
        option_xpath = DROPDOWN_UMOOR_OPTION_XPATH.format(value=chosen)   # --- 4) click the same chosen UMOOR from dropdown ---
        dropdown_option = self.page.locator(option_xpath)
        dropdown_option.click()
        # optional: wait for results and verify at least one row contains chosen value
        self.page.wait_for_timeout(5000)  # or better: wait_for_selector with result row
        try:
            option_xpath_after_search = xpath_row_after_search.format(value=chosen)      # check if any cell in same UMOOR column equals chosen
            row_after_search= self.page.locator(option_xpath_after_search)
            print("Search result contains the searched UMOOR.")
        except:
            print("No matching result found after search.")

        header, result = elaam_prod("get_umoor_id_by_name", chosen)
        umoortable = tabulate(result, headers=header, tablefmt="grid")
        print("Umoor name: ", umoortable)
        if not result:                                            # result example: [(10, 'FMB')]
            raise Exception(f"No DB record found for UMOOR: {chosen}")
        umoor_id = result[0][0]
        db_umoor_name = result[0][1]
        print(f"DB UMOOR ID: {umoor_id}, DB UMOOR NAME: {db_umoor_name}")
        header, result = elaam_prod("mumin_total_niyat_fmb_umoor_after_search", its_id, umoor_id)
        search_result = tabulate(result, headers=header, tablefmt="grid")
        print("search result: ", search_result)
        total_niyat_count_fmb_umoor_after_search_db = result[0][header.index("total_niyats")]
        self.page.wait_for_timeout(1000)
        pagination_text = self.page.wait_for_selector(xpath_pagination_text).inner_text()
        # Split by 'of' and take the last part, strip spaces, convert to int
        total_count_pagination_fmb_umoor_search = int(pagination_text.split("of")[-1].strip())
        return total_niyat_count_fmb_umoor_after_search_db, total_count_pagination_fmb_umoor_search, db_umoor_name

    def test_verify_niyat_question(self):
        niyat_question = self.page.locator(xpath_niyat_question).inner_text()
        self.page.locator(xpath_view_icon).click()
        niyat_question_information_page = self.page.locator(xpath_niyat_question_info_page).inner_text().split('(')[0].strip()
        return niyat_question,niyat_question_information_page

    def click_back_button_niyat_information_page_navigation_mumin_dashboard_page(self):
        self.page.locator(xpath_back_button).click()

    def click_item_per_page_drop_down_and_compare_data_with_rows_and_select_value(self):

        self.page.locator(xpath_item_per_page_drop_down).click()
        option_locators = self.page.locator(xpath_options)
        count = option_locators.count()
        options = [option_locators.nth(i).inner_text() for i in range(count)]
        random_value = random.choice(options)
        self.page.locator(f"{xpath_random_value}'{random_value}']").click()
        # Wait for rows to reload
        self.page.wait_for_selector(xpath_row_count)
        row_count = self.page.locator(xpath_row_count).count()
        pagination_text = self.page.wait_for_selector(xpath_pagination_text).inner_text()
        # Split by 'of' and take the last part, strip spaces, convert to int
        total_count_pagination = int(pagination_text.split('–')[-1].strip().split('of')[0].strip())
        return total_count_pagination, row_count, random_value

    def send_message_functionality(self):

        subject = generate_unique_subject()  # e.g., "Brilliant Report"
        message_text = generate_unique_message_text()  # e.g., "The Task was completed with excellence."
        self.page.locator(xpath_approval_pending_widget).click()
        self.page.locator(xpath_view_icon).click()
        self.page.locator(xpath_send_message_button).click()
        self.page.wait_for_selector(xpath_subject_field).fill(subject)
        self.page.wait_for_selector(xpath_message_text_field).fill(message_text)
        self.page.locator(xpath_send_button).click()
        success_message= self.page.wait_for_selector(xpath_send_message_success_message).inner_text()
        return success_message
            
    def click_request_for_update(self):
        self.page.locator(xpath_Active_Niyat_tile).click()
        self.page.locator(xpath_view_icon).click()
        self.page.locator(xpath_request_for_update).click()
        self.page.wait_for_timeout(200)
        # Alert message capture (Accessible role = alert, name = "Niyat Details Has Been")
        # alert_message = self.page.get_by_role("alert", name="Niyat Details Has Been Update.")

        success_message_request_for_update  = self.page.wait_for_selector(xpath_send_message_success_message).inner_text()
        print("hjfgdhsfgdjf:", success_message_request_for_update)
        return success_message_request_for_update

    # def get_outcome_message(self):
    #     try:
    #         # Outcome 1: Mubarak
    #         if self.page.locator(xpath_mubarak_text).is_visible(timeout=4000):
    #             text = self.page.locator(xpath_mubarak_text).inner_text()
    #             print("✅ Mubarak text is displayed:", text)
    #             return "MUBARAK"
    #
    #         # Outcome 2: Pending
    #         if self.page.locator(xpath_niyat_info_pending_status).is_visible(timeout=4000):
    #             pending = self.page.locator(xpath_niyat_info_pending_status).inner_text()
    #             print("✅ Niyat status is:", pending)
    #             return "PENDING"
    #
    #         # Agar dono nahi mile
    #         print("❌ Neither Mubarak nor Pending found")
    #         return "UNKNOWN"
    #
    #     except Exception as e:
    #         print("❌ Error while getting outcome:", e)
    #         return "ERROR"






























