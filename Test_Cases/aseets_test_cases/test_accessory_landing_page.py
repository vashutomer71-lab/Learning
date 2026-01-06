from pageObjects.assets_page.accessory_landing_page import AccessoryPageHeader
from Test_Cases.conftest import login, setup
from Utilities.CustomLoggers import LogGen

class TestAccessoryModel:
    logger = LogGen.loggen()

    def test_accessory(self, setup, login):
        """""
        'Test case to verify the  accessory landing page functionality'
        """""

        self.page = login
        self.logger.info("****Login successfully Completed*******")
        self.acm = AccessoryPageHeader(self.page)
        self.logger.info("*****Redirect on the accessory page****")
        self.acm.click_assets()
        self.logger.info("******Click on the assets menu successfully*******")
        self.acm.click_accessory_tab()
        self.logger.info("****Click on the accessory tab successfully***")
        self.acm.verify_landing_page_heading()
        self.logger.info("*******The hading is matched successfully******")
        self.acm.verify_table_header()
        self.logger.info("******Accessory page header verify successfully******")
        self.acm.verify_widget_total_count_with_sum_sub_count()
        self.logger.info("******Accessory total count matched with the sum of the sub status*****")
        self.acm.verify_table_header()
        self.logger.info("******Table header are successfully matched******")
        self.acm.click_enter_search_key()
        self.logger.info("********The search key enter successfully and verify the value in table with count******")
        self.acm.verify_item_per_page()
        self.logger.info("******Click on the item per page dropdown*****")
        self.acm.verify_item_per_page1()
        self.logger.info("******Click on the item per page dropdown1*****")





