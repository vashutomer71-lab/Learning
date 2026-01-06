from pageObjects.Dashboard_Page import FleetDashboardPage
from Utilities.CustomLoggers import LogGen


import pytest


class TestDashboard:
    logger = LogGen.loggen()
    @pytest.mark.sanity("Sanity Test")
    @pytest.mark.smoke("Smoke")
    def test_dashboard_verifications(self, login):
        """
        Test case to verify the functionality of the dashboard page.
        """
        self.logger.info("****** Test Dashboard Page Verifications Started *********")
        self.page = login
        self.logger.info("****** Login Completed*********")

        # Dashboard Page
        self.db = FleetDashboardPage(self.page)
        self.logger.info("****** Navigate to Dashboard Page *********")
        self.db.verify_left_menu_tabs()
        self.logger.info("****** Left Menu Tabs are Verified *********")
        self.db.verify_fleet_tile()
        self.logger.info("****** Verified All the Four Tiles at Top Left of the Page *********")




