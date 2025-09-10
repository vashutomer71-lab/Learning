from playwright.sync_api import sync_playwright, Page
from Test_Cases.conftest import db_connection, elaam_prod
from Utilities.ReadProperties import ReadConfig
from tabulate import tabulate
import re

url = ReadConfig.get_back_end_url()

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
xpath_total_trophy_count = "//div[@class='txt_overlay txt_top']"
xpah_trophies_redeemed= "//p[contains(text(),'Trophies Redeemed')]"

class MuminDashboardPage:

    total_fleet_tiles = None

    def __init__(self, page:Page):
        self.page = page

    def click_dashboard_menu(self):
        self.page.wait_for_selector(xpath_dashboard_menu).click()

    def verify_mumin_dashboard_heading(self):
        expected = "Mumin Dashboard"
        dashboard_text_frontend = self.page.inner_text(xpath_dashboard_heading)
        # Improved print message for clarity
        print(f"Verifying mumin Dashboard Heading...\nExpected: '{expected}'\nActual: '{dashboard_text_frontend}'")
        assert dashboard_text_frontend == expected, \
            f"Test failed: Expected '{expected}', but the actual text was '{dashboard_text_frontend}'."
        self.page.wait_for_timeout(1000)

    def verify_dashboard_tile_all_filter(self, elaam_prod):
        self.page.wait_for_timeout(3000)
        total_niyat_count_widget = int(next(line for line in self.page.inner_text(xpath_Total_Niyat_tile).splitlines() if line.strip()))
        print("Total Niyat Count:", total_niyat_count_widget)
        active_niyat_count_widget = int(next(line for line in self.page.inner_text(xpath_Active_Niyat_tile).splitlines() if line.strip()))
        print("Active Niyat Count:", active_niyat_count_widget)
        approval_pending_niyat_count_widget = int(next(line for line in self.page.inner_text(xpath_Approval_pending_Niyat_tile).splitlines() if line.strip()))
        print("Approval Pending Niyat Count:", approval_pending_niyat_count_widget)
        completed_niyat_count_widget = int(next(line for line in self.page.inner_text(xpath_Completed_Niyat_tile).splitlines() if line.strip()))
        print("Approval Pending Niyat Count:", completed_niyat_count_widget)

        # Execute SQL query to fetch data from the database
        total_niyat_query = "all_niyat_tile_count_query"
        headers, result = elaam_prod(total_niyat_query)
        db_table_view= tabulate(result, headers=headers, tablefmt="grid")   # Display the database results in a tabular format
        print("DB table view: ", db_table_view)
        # Process database results to store counts by status
        total_niyat_count_db = result[0][headers.index('total_count')]
        active_count_db = result[0][headers.index('active_count')]
        completed_count_db = result[0][headers.index('completed_count')]
        approval_pending_db = result[0][headers.index('approval_pending_count')]
        deactivated_db = result[0][headers.index('deactivated_count')]
        print("DB Total Niyat:", total_niyat_count_db)
        print("DB Active:", active_count_db)
        print("DB Completed:", completed_count_db)
        print("DB Approval Pending:", approval_pending_db)
        print("DB Deactivated:", deactivated_db)
        total_niyat_count_add_all_status = active_count_db + completed_count_db + approval_pending_db + deactivated_db

        assert total_niyat_count_widget == total_niyat_count_db, f"Expected  total niyats count  in db '{total_niyat_count_db}', but got on widget '{total_niyat_count_widget}'"
        assert active_niyat_count_widget == active_count_db, f"Expected active niyat count in bd {active_count_db}, but got on widget {active_niyat_count_widget}"
        assert approval_pending_niyat_count_widget == approval_pending_db, f"Expected approval pending niyat count in db {approval_pending_db}, but got on widget ' {approval_pending_niyat_count_widget}"
        assert completed_niyat_count_widget == completed_count_db, f"Expected completed niyat count {completed_count_db}, but got on widget {completed_niyat_count_widget}"
        assert total_niyat_count_add_all_status == total_niyat_count_db, f"Expected total niyat count in db {total_niyat_count_db}, but got total niyat count after adding all status{total_niyat_count_add_all_status}"
        print("All assertions passed successfully for mumin dashboard tiles")

    def click_duration_drop_down_and_select_1_month_filter(self):
        self.page.locator(xpath_duration_dropdown).click()
        self.page.locator("body").press("ControlOrMeta+Shift+I")
        # self.page.get_by_role("option", name="Last 1 Month").click()
        self.page.locator(xpath_1_month).click()

    def verify_dashboard_tile_1_month_filter(self, elaam_prod):
        self.page.wait_for_timeout(3000)
        total_niyat_count_widget_for_1_month = int(next(line for line in self.page.inner_text(xpath_Total_Niyat_tile).splitlines() if line.strip()))
        print("Total Niyat Count for 1 month:", total_niyat_count_widget_for_1_month)
        active_niyat_count_widget_for_1_month  = int(next(line for line in self.page.inner_text(xpath_Active_Niyat_tile).splitlines() if line.strip()))
        print("Active Niyat Count for 1 month:", active_niyat_count_widget_for_1_month)
        approval_pending_niyat_count_widget_for_1_month = int(next(line for line in self.page.inner_text(xpath_Approval_pending_Niyat_tile).splitlines() if line.strip()))
        print("Approval Pending Niyat Count for 1 month:", approval_pending_niyat_count_widget_for_1_month)
        completed_niyat_count_widget_for_1_month = int(next(line for line in self.page.inner_text(xpath_Completed_Niyat_tile).splitlines() if line.strip()))
        print("Approval Pending Niyat Count for 1 month:", completed_niyat_count_widget_for_1_month)

        # Execute SQL query to fetch data from the database
        total_niyat_query_for_1_month= "1_month_niyat_tile_count_query"
        headers, result = elaam_prod(total_niyat_query_for_1_month)
        db_table_view= tabulate(result, headers=headers, tablefmt="grid")   # Display the database results in a tabular format
        print("DB table view for 1 month: ", db_table_view)
        # Process database results to store counts by status
        total_niyat_count_db_for_1_month = result[0][headers.index('total_count')]
        active_count_db = result[0][headers.index('active_count')]
        completed_count_db = result[0][headers.index('completed_count')]
        approval_pending_db = result[0][headers.index('approval_pending_count')]
        deactivated_db = result[0][headers.index('deactivated_count')]
        print("DB Total Niyat:", total_niyat_count_db_for_1_month)
        print("DB Active:", active_count_db)
        print("DB Completed:", completed_count_db)
        print("DB Approval Pending:", approval_pending_db)
        print("DB Deactivated:", deactivated_db)
        total_niyat_count_add_all_status = active_count_db + completed_count_db + approval_pending_db + deactivated_db

        assert total_niyat_count_widget_for_1_month == total_niyat_count_db_for_1_month, f"Expected  total niyats count  in db '{total_niyat_count_db_for_1_month}', but got on widget '{total_niyat_count_widget_for_1_month}'"
        assert active_niyat_count_widget_for_1_month == active_count_db, f"Expected active niyat count in bd {active_count_db}, but got on widget {active_niyat_count_widget_for_1_month}"
        assert approval_pending_niyat_count_widget_for_1_month == approval_pending_db, f"Expected approval pending niyat count in db {approval_pending_db}, but got on widget ' {approval_pending_niyat_count_widget_for_1_month}"
        assert completed_niyat_count_widget_for_1_month == completed_count_db, f"Expected completed niyat count {completed_count_db}, but got on widget {completed_niyat_count_widget_for_1_month}"
        assert total_niyat_count_add_all_status == total_niyat_count_db_for_1_month, f"Expected total niyat count in db {total_niyat_query_for_1_month}, but got total niyat count after adding all status{total_niyat_count_add_all_status}"
        print("All assertions passed successfully for mumin dashboard tiles for 1 month filter")

    def click_duration_drop_down_and_select_3_month_filter(self):
        self.page.locator(xpath_duration_dropdown).click()
        self.page.locator("body").press("ControlOrMeta+Shift+I")
        # self.page.get_by_role("option", name="Last 1 Month").click()
        self.page.locator(xpath_3_month).click()

    def verify_dashboard_tile_3_month_filter(self, elaam_prod):
        self.page.wait_for_timeout(3000)
        total_niyat_count_widget_for_3_month = int(next(line for line in self.page.inner_text(xpath_Total_Niyat_tile).splitlines() if line.strip()))
        print("Total Niyat Count for 3 month:", total_niyat_count_widget_for_3_month)
        active_niyat_count_widget_for_3_month  = int(next(line for line in self.page.inner_text(xpath_Active_Niyat_tile).splitlines() if line.strip()))
        print("Active Niyat Count for 3 month:", active_niyat_count_widget_for_3_month)
        approval_pending_niyat_count_widget_for_3_month = int(next(line for line in self.page.inner_text(xpath_Approval_pending_Niyat_tile).splitlines() if line.strip()))
        print("Approval Pending Niyat Count for 3 month:", approval_pending_niyat_count_widget_for_3_month)
        completed_niyat_count_widget_for_3_month = int(next(line for line in self.page.inner_text(xpath_Completed_Niyat_tile).splitlines() if line.strip()))
        print("Approval Pending Niyat Count for 3 month:", completed_niyat_count_widget_for_3_month)

        # Execute SQL query to fetch data from the database
        total_niyat_query_for_3_month= "3_month_niyat_tile_count_query"
        headers, result = elaam_prod(total_niyat_query_for_3_month)
        db_table_view= tabulate(result, headers=headers, tablefmt="grid")   # Display the database results in a tabular format
        print("DB table view for 3 month: ", db_table_view)
        # Process database results to store counts by status
        total_niyat_count_db_for_3_month = result[0][headers.index('total_count')]
        active_count_db = result[0][headers.index('active_count')]
        completed_count_db = result[0][headers.index('completed_count')]
        approval_pending_db = result[0][headers.index('approval_pending_count')]
        deactivated_db = result[0][headers.index('deactivated_count')]
        print("DB Total Niyat:", total_niyat_count_db_for_3_month)
        print("DB Active:", active_count_db)
        print("DB Completed:", completed_count_db)
        print("DB Approval Pending:", approval_pending_db)
        print("DB Deactivated:", deactivated_db)
        total_niyat_count_add_all_status = active_count_db + completed_count_db + approval_pending_db + deactivated_db

        assert total_niyat_count_widget_for_3_month == total_niyat_count_db_for_3_month, f"Expected  total niyats count  in db '{total_niyat_count_db_for_3_month}', but got on widget '{total_niyat_count_widget_for_3_month}'"
        assert active_niyat_count_widget_for_3_month == active_count_db, f"Expected active niyat count in bd {active_count_db}, but got on widget {active_niyat_count_widget_for_3_month}"
        assert approval_pending_niyat_count_widget_for_3_month == approval_pending_db, f"Expected approval pending niyat count in db {approval_pending_db}, but got on widget ' {approval_pending_niyat_count_widget_for_3_month}"
        assert completed_niyat_count_widget_for_3_month == completed_count_db, f"Expected completed niyat count {completed_count_db}, but got on widget {completed_niyat_count_widget_for_3_month}"
        assert total_niyat_count_add_all_status == total_niyat_count_db_for_3_month, f"Expected total niyat count in db {total_niyat_query_for_3_month}, but got total niyat count after adding all status{total_niyat_count_add_all_status}"
        print("All assertions passed successfully for mumin dashboard tiles for 3 month filter")

    def click_duration_drop_down_and_select_6_months_filter(self):
        self.page.locator(xpath_duration_dropdown).click()
        self.page.locator("body").press("ControlOrMeta+Shift+I")
        # self.page.get_by_role("option", name="Last 1 Month").click()
        self.page.locator(xpath_6_month).click()

    def verify_dashboard_tile_6_month_filter(self, elaam_prod):
        self.page.wait_for_timeout(3000)
        total_niyat_count_widget_for_6_month = int(next(line for line in self.page.inner_text(xpath_Total_Niyat_tile).splitlines() if line.strip()))
        print("Total Niyat Count for 6 month:", total_niyat_count_widget_for_6_month)
        active_niyat_count_widget_for_6_month  = int(next(line for line in self.page.inner_text(xpath_Active_Niyat_tile).splitlines() if line.strip()))
        print("Active Niyat Count for 6 month:", active_niyat_count_widget_for_6_month)
        approval_pending_niyat_count_widget_for_6_month = int(next(line for line in self.page.inner_text(xpath_Approval_pending_Niyat_tile).splitlines() if line.strip()))
        print("Approval Pending Niyat Count for 6 month:", approval_pending_niyat_count_widget_for_6_month)
        completed_niyat_count_widget_for_6_month = int(next(line for line in self.page.inner_text(xpath_Completed_Niyat_tile).splitlines() if line.strip()))
        print("Approval Pending Niyat Count for 6 month:", completed_niyat_count_widget_for_6_month)

        # Execute SQL query to fetch data from the database
        total_niyat_query_for_6_month= "6_month_niyat_tile_count_query"
        headers, result = elaam_prod(total_niyat_query_for_6_month)
        db_table_view= tabulate(result, headers=headers, tablefmt="grid")   # Display the database results in a tabular format
        print("DB table view for 6 month: ", db_table_view)
        # Process database results to store counts by status
        total_niyat_count_db_for_6_month = result[0][headers.index('total_count')]
        active_count_db = result[0][headers.index('active_count')]
        completed_count_db = result[0][headers.index('completed_count')]
        approval_pending_db = result[0][headers.index('approval_pending_count')]
        deactivated_db = result[0][headers.index('deactivated_count')]
        print("DB Total Niyat:", total_niyat_count_db_for_6_month)
        print("DB Active:", active_count_db)
        print("DB Completed:", completed_count_db)
        print("DB Approval Pending:", approval_pending_db)
        print("DB Deactivated:", deactivated_db)
        total_niyat_count_add_all_status = active_count_db + completed_count_db + approval_pending_db + deactivated_db

        assert total_niyat_count_widget_for_6_month == total_niyat_count_db_for_6_month, f"Expected  total niyats count  in db '{total_niyat_count_db_for_6_month}', but got on widget '{total_niyat_count_widget_for_6_month}'"
        assert active_niyat_count_widget_for_6_month == active_count_db, f"Expected active niyat count in bd {active_count_db}, but got on widget {active_niyat_count_widget_for_6_month}"
        assert approval_pending_niyat_count_widget_for_6_month == approval_pending_db, f"Expected approval pending niyat count in db {approval_pending_db}, but got on widget ' {approval_pending_niyat_count_widget_for_6_month}"
        assert completed_niyat_count_widget_for_6_month == completed_count_db, f"Expected completed niyat count {completed_count_db}, but got on widget {completed_niyat_count_widget_for_6_month}"
        assert total_niyat_count_add_all_status == total_niyat_count_db_for_6_month, f"Expected total niyat count in db {total_niyat_query_for_6_month}, but got total niyat count after adding all status{total_niyat_count_add_all_status}"
        print("All assertions passed successfully for mumin dashboard tiles for 6 months filter")
        self.page.wait_for_timeout(5000)

    def click_duration_drop_down_and_select_1_year_filter(self):
        self.page.locator(xpath_duration_dropdown).click()
        self.page.locator("body").press("ControlOrMeta+Shift+I")
        # self.page.get_by_role("option", name="Last 1 Month").click()
        self.page.locator(xpath_1_year).click()

    def verify_dashboard_tile_1_year_filter(self, elaam_prod):
        self.page.wait_for_timeout(5000)
        total_niyat_count_widget_for_1_year = int(next(line for line in self.page.inner_text(xpath_Total_Niyat_tile).splitlines() if line.strip()))
        print("Total Niyat Count for 1 year:", total_niyat_count_widget_for_1_year)
        active_niyat_count_widget_for_1_year  = int(next(line for line in self.page.inner_text(xpath_Active_Niyat_tile).splitlines() if line.strip()))
        print("Active Niyat Count for 1 year:", active_niyat_count_widget_for_1_year)
        approval_pending_niyat_count_widget_for_1_year = int(next(line for line in self.page.inner_text(xpath_Approval_pending_Niyat_tile).splitlines() if line.strip()))
        print("Approval Pending Niyat Count for 1 year:", approval_pending_niyat_count_widget_for_1_year)
        completed_niyat_count_widget_for_1_year = int(next(line for line in self.page.inner_text(xpath_Completed_Niyat_tile).splitlines() if line.strip()))
        print("Approval Pending Niyat Count for 1 year:", completed_niyat_count_widget_for_1_year)

        # Execute SQL query to fetch data from the database
        total_niyat_query_for_1_year= "1_year_niyat_tile_count_query"
        headers, result = elaam_prod(total_niyat_query_for_1_year)
        db_table_view= tabulate(result, headers=headers, tablefmt="grid")   # Display the database results in a tabular format
        print("DB table view for 1 year: ", db_table_view)
        # Process database results to store counts by status
        total_niyat_count_db_for_1_year = result[0][headers.index('total_count')]
        active_count_db = result[0][headers.index('active_count')]
        completed_count_db = result[0][headers.index('completed_count')]
        approval_pending_db = result[0][headers.index('approval_pending_count')]
        deactivated_db = result[0][headers.index('deactivated_count')]
        print("DB Total Niyat:", total_niyat_count_db_for_1_year)
        print("DB Active:", active_count_db)
        print("DB Completed:", completed_count_db)
        print("DB Approval Pending:", approval_pending_db)
        print("DB Deactivated:", deactivated_db)
        total_niyat_count_add_all_status = active_count_db + completed_count_db + approval_pending_db + deactivated_db

        assert total_niyat_count_widget_for_1_year == total_niyat_count_db_for_1_year, f"Expected  total niyats count  in db '{total_niyat_count_db_for_1_year}', but got on widget '{total_niyat_count_widget_for_1_year}'"
        assert active_niyat_count_widget_for_1_year == active_count_db, f"Expected active niyat count in bd {active_count_db}, but got on widget {active_niyat_count_widget_for_1_year}"
        assert approval_pending_niyat_count_widget_for_1_year == approval_pending_db, f"Expected approval pending niyat count in db {approval_pending_db}, but got on widget ' {approval_pending_niyat_count_widget_for_1_year}"
        assert completed_niyat_count_widget_for_1_year == completed_count_db, f"Expected completed niyat count {completed_count_db}, but got on widget {completed_niyat_count_widget_for_1_year}"
        assert total_niyat_count_add_all_status == total_niyat_count_db_for_1_year, f"Expected total niyat count in db {total_niyat_query_for_1_year}, but got total niyat count after adding all status{total_niyat_count_add_all_status}"
        print("All assertions passed successfully for mumin dashboard tiles for 1 year filter")

    def verify_total_trophy_count(self):
        trophy_text = self.page.locator("//div[@class='mumnin_reward']").all_inner_texts()
        print("Raw trophy text:", trophy_text)


















