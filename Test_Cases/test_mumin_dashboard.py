from Test_Cases.conftest import login, setup, db_connection, elaam_prod
from pageObjects.mumin_dashboard_page import MuminDashboardPage
import allure
from Utilities.CustomLoggers import LogGen


class TestMuminDashboard:
    logger = LogGen.loggen()
    @allure.step("Click on the dashboard menu and open the dashboard page")
    def test_click_mumin_dashboard_menu(self, setup, login):
        self.page = login
        self.c_tile = MuminDashboardPage(self.page)
        self.c_tile.click_dashboard_menu()
        self.logger.info("******Click on the Dashboard menu****")

    @allure.step("Verify the mumin dashboard heading")
    def test_dashboard_heading(self, setup, login):
        self.page = login
        self.c_tile = MuminDashboardPage(self.page)
        self.c_tile.verify_mumin_dashboard_heading()
        self.logger.info("******Verify the mumin dashboard heading****")

    @allure.step("Verify the all widgets count with the data base count for the total niyat, active, pending, completed")
    def test_dashboard_tile(self, setup, login, elaam_prod):
        self.page = login
        self.fd_tile = MuminDashboardPage(self.page)
        self.fd_tile.verify_dashboard_tile_all_filter(elaam_prod)
        self.logger.info("********Verify the all widgets count with the data base count for the total niyat, active, pending, completed**********")
