from playwright.sync_api import Page, sync_playwright
from Test_Cases.conftest import db_connection, elaam_prod
from Utilities.ReadProperties import ReadConfig
from tabulate import tabulate
import re

xpath_catalogue_menu = "//a[normalize-space()='Catalogue']"
xpath_total_trophy_count = "(//p[contains(text(),'')])[1]"
xpath_trophies_redeemed= "//p[contains(text(),'Trophies Redeemed')]"
xpath_trophy_balance = "//p[contains(text(),'Trophies Balance')]"

class CataloguePage:

    def __init__(self, page:Page):
        self.page = page

    def click_catalogue_menu(self):
        self.page.locator(xpath_catalogue_menu).click()

    def get_total_trophies_counts_catalogue(self, elaam_prod, its_id):
        """Fetch trophy counts from two locators and return as separate variables."""

        def get_number(loc):
            # Wait until element has a number
            while not (match := re.search(r"\d+", self.page.locator(loc).inner_text())):
                self.page.wait_for_timeout(200)
            return int(match.group())
        # Fetch counts
        total_trophy_count_from_ui = get_number(xpath_total_trophy_count)
        trophies_redeemed_count_from_ui = get_number(xpath_trophies_redeemed)
        trophies_balance_count_from_ui = get_number(xpath_trophy_balance)
        print(f"Total count on ui: {total_trophy_count_from_ui}, redeemed count of ui: {trophies_redeemed_count_from_ui}, balance count: {trophies_balance_count_from_ui}")
        headers, result = elaam_prod("mumin_trophies_count", its_id, its_id)
        db_table_format = tabulate(result, headers=headers, tablefmt="grid")
        print("Trophies count : ",db_table_format)
        total_trophy_count_from_db = result[0][headers.index("total_awarded")]
        total_redeemed_trophy_count_from_db = result[0][headers.index("total_redeemed")]
        total_balance_trophies_count_form_db = result[0][headers.index("balance_trophies")]
        print(f"Total count: {total_trophy_count_from_db}, redeemed count: {total_redeemed_trophy_count_from_db}, balance: {total_balance_trophies_count_form_db}")
        return total_trophy_count_from_ui, trophies_redeemed_count_from_ui, trophies_balance_count_from_ui, total_trophy_count_from_db, total_redeemed_trophy_count_from_db, total_balance_trophies_count_form_db





