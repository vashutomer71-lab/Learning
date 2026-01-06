from Test_Cases.conftest import login, setup
from Utilities.CustomLoggers import LogGen
from pageObjects.assets_page.route_landing_page import RouteLandingPage

class TestRouteLandingPage:

    logger = LogGen.loggen()

    def test_route(self, setup, login):
        self.page = login
        self.route = RouteLandingPage(self.page)
        self.logger.info("*****User logged in successfully*****")
        self.route.click_assets_menu()
        self.logger.info("****Click on the assets menu successfully****")
        self.route.click_route_setup_sub_menu()
        self.logger.info("****Click on the route setup sub menu successfully****")
        self.route.verify_landing_page_heading()
        self.logger.info("****The route listing page heading is matched with the expected heading***")
        self.route.verify_route_tile_text()
        self.logger.info("****The route widget text are matched with the expected texts.****")
        self.route.verify_tile_total_count_with_some_of_sub_count()
        self.logger.info("*****The tile total is the sum of the sub status total*****")
        self.route.verify_table_header()
        self.logger.info("****The route table header column are matched with the expected columns****")
        self.route.verify_the_search_functionality()
        self.logger.info("****The search functionality and matched the count with the search record****")
        self.route.verify_item_per_page()
        self.logger.info("****The item per page functionality and matched the pagination count with the selected item per page****")
        self.route.verify_add_route_button()
        self.logger.info("***After click on the add route button, user is redirected on the add route page***")
        self.route.click_select_fleet_name()










