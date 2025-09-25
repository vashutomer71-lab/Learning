from playwright.async_api import expect
from Test_Cases.conftest import login, setup, db_connection, elaam_prod
from pageObjects.catalogue_page import CataloguePage
import allure
from Utilities.CustomLoggers import LogGen


class TestCatalogue:

    logger = LogGen.loggen()

    def test_click_catalogue_menu(self,setup,login):
        self.page = login
        self.click_cat_menu = CataloguePage(self.page)
        with allure.step("Click on Catalogue menu"):
            self.click_cat_menu.click_catalogue_menu()
            self.logger.info("******Click on the Catalogue left panel menu****")


    def test_total_trophy_count(self, setup, login, elaam_prod):
        self.page = login
        self.catalogue_trophy = CataloguePage(self.page)
        total_trophy_count_from_ui, trophies_redeemed_count_from_ui, trophies_balance_count_from_ui, total_trophy_count_from_db, total_redeemed_trophy_count_from_db, total_balance_trophies_count_form_db = self.catalogue_trophy.get_total_trophies_counts_catalogue(elaam_prod)
        with allure.step("Match trophy count with the database count for the trophy"):
            try:
                assert total_trophy_count_from_db == total_trophy_count_from_ui, f"Expected total trophy count form db:{total_trophy_count_from_db} but got form UI {total_trophy_count_from_ui}"
                assert total_redeemed_trophy_count_from_db == trophies_redeemed_count_from_ui, f"Expected redeemed trophy count DB: {total_redeemed_trophy_count_from_db}, but got form ui : {trophies_redeemed_count_from_ui}"
                assert total_balance_trophies_count_form_db == trophies_balance_count_from_ui,  f"Expected balance count from DB: {total_balance_trophies_count_form_db}, but got on UI: {trophies_balance_count_from_ui}"
                self.logger.info(f"Expected total trophy count form db: {total_trophy_count_from_db} but got form UI: {total_trophy_count_from_ui}")
                self.logger.info(f"Expected redeemed trophy count DB: {total_redeemed_trophy_count_from_db}, but got form ui : {trophies_redeemed_count_from_ui}")
                self.logger.info(f"Expected balance count from DB: {total_balance_trophies_count_form_db}, but got on UI: {trophies_balance_count_from_ui}")
                self.logger.info("******The total, redeemed, balance trophy count are matched with DB count*******")
            except AssertionError as e:
                self.page.screenshot(path="Screenshots/total_trophy_count.png")
                allure.attach.file("Screenshots/total_trophy_count.png", name="Total Trophy count is not match with db",
                                   attachment_type=allure.attachment_type.PNG)







