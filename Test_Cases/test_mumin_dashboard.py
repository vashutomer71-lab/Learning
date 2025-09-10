from Test_Cases.conftest import login, setup, db_connection, elaam_prod
from pageObjects.mumin_dashboard_page import MuminDashboardPage
import allure
from Utilities.CustomLoggers import LogGen


class TestMuminDashboard:
    logger = LogGen.loggen()
    # @allure.step("Click on the dashboard menu and open the dashboard page")
    # def test_click_mumin_dashboard_menu(self, setup, login):
    #     self.page = login
    #     self.m_tile = MuminDashboardPage(self.page)
    #     self.m_tile.click_dashboard_menu()
    #     self.logger.info("******Click on the Dashboard menu****")

    # @allure.step("Verify the mumin dashboard heading")
    # def test_dashboard_heading(self, setup, login):
    #     self.page = login
    #     self.m_tile = MuminDashboardPage(self.page)
    #     self.m_tile.verify_mumin_dashboard_heading()
    #     self.logger.info("******Verify the mumin dashboard heading****")

    # @allure.step("Verify the all widgets count with the database count for the total niyat, active, pending, completed")
    # def test_dashboard_tile(self, setup, login, elaam_prod):
    #     self.page = login
    #     self.niyats_tile = MuminDashboardPage(self.page)
    #     self.niyats_tile.verify_dashboard_tile_all_filter(elaam_prod)
    #     self.logger.info("********Verify the all widgets count with the database count for the total niyat, active, pending, completed**********")
    #
    # def test_duration_drop_down_opened(self, setup, login):
    #     self.page=login
    #     self.duration_dropdown = MuminDashboardPage(self.page)
    #     self.duration_dropdown.click_duration_drop_down_and_select_1_month_filter()
    #     self.logger.info("*******Duration dropdown opened successfully and select 1 month filter successfully**********")
    #
    # def test_dashboard_widget_for_1_month(self, setup,login,elaam_prod):
    #     self.page=login
    #     self.month_1_filter = MuminDashboardPage(self.page)
    #     self.month_1_filter.verify_dashboard_tile_1_month_filter(elaam_prod)
    #     self.logger.info("*****Verify all widget count for 1 month filter successfully.******")
    #
    # def test_duration_drop_down_opened_and_select_3_months_option(self, setup, login):
    #     self.page=login
    #     self.duration_dropdown = MuminDashboardPage(self.page)
    #     self.duration_dropdown.click_duration_drop_down_and_select_3_month_filter()
    #     self.logger.info("*******Duration dropdown opened successfully and select 3 months filter successfully**********")
    #
    # def test_dashboard_widget_for_3_months(self, setup, login, elaam_prod):
    #     self.page = login
    #     self.month_3_filter = MuminDashboardPage(self.page)
    #     self.month_3_filter.verify_dashboard_tile_3_month_filter(elaam_prod)
    #     self.logger.info("*****Verify all widget count for 3 month filter successfully.******")
    #
    # def test_duration_drop_down_opened_and_select_6_months_option(self, setup, login):
    #     self.page = login
    #     self.duration_dropdown = MuminDashboardPage(self.page)
    #     self.duration_dropdown.click_duration_drop_down_and_select_6_months_filter()
    #     self.logger.info("*******Duration dropdown opened successfully and select 6 months filter successfully**********")
    #
    # def test_dashboard_widget_for_6_months(self, setup, login, elaam_prod):
    #     self.page = login
    #     self.month_6_filter = MuminDashboardPage(self.page)
    #     self.month_6_filter.verify_dashboard_tile_6_month_filter(elaam_prod)
    #     self.logger.info("*****Verify all widget count for 6 months filter successfully.******")
    #
    # def test_duration_drop_down_opened_and_select_1_year_option(self, setup, login):
    #     self.page = login
    #     self.duration_dropdown = MuminDashboardPage(self.page)
    #     self.duration_dropdown.click_duration_drop_down_and_select_1_year_filter()
    #     self.logger.info("*******Duration dropdown opened successfully and select 1 year filter successfully**********")
    #
    # def test_dashboard_widget_for_1_year(self, setup, login, elaam_prod):
    #     self.page = login
    #     self.month_1_year = MuminDashboardPage(self.page)
    #     self.month_1_year.verify_dashboard_tile_1_year_filter(elaam_prod)
    #     self.logger.info("*****Verify all widget count for 1 year filter successfully.******")

    def test_total_trophy_count(self,setup,login):
        self.page=login
        self.TC= MuminDashboardPage(self.page)
        self.TC.verify_total_trophy_count()



