from playwright.sync_api import sync_playwright, Page
from Test_Cases.conftest import db_connection, elaam_prod
from Utilities.ReadProperties import ReadConfig
from tabulate import tabulate

url = ReadConfig.get_back_end_url()

xpath_dashboard_menu = "//li/a[normalize-space(text())='Mumin Dashboard']"
xpath_dashboard_heading = "//h1[normalize-space(text())='Mumin Dashboard']"
xpath_Total_Niyat_tile = "(//div[@class='box1 ng-star-inserted'])[1]"
xpath_Active_Niyat_tile = "(//div[@class='box1 ng-star-inserted'])[2]"
xpath_Approval_pending_Niyat_tile = "(//div[@class='box1 ng-star-inserted'])[3]"
xpath_Completed_Niyat_tile = "(//div[@class='box1 ng-star-inserted'])[4]"

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







