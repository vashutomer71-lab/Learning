import pytest
from playwright.async_api import expect
from Test_Cases.conftest import login, setup, db_connection, elaam_prod
from pageObjects.mumin_dashboard_page import MuminDashboardPage
import allure
from Utilities.CustomLoggers import LogGen

expected_path = "/catalogue"
expected = "Mumin Dashboard"
expected_text = "Notification Sent Successfully."

@pytest.mark.sanity
@pytest.mark.regression
class TestMuminDashboard:

    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_click_mumin_dashboard_menu(self, setup, login):
        self.page = login
        self.m_tile = MuminDashboardPage(self.page)
        with allure.step("Click on Dashboard menu"):
            self.m_tile.click_dashboard_menu()
            self.logger.info("******Click on the Dashboard menu****")

    @pytest.mark.regression
    @pytest.mark.sanity
    @allure.feature("Dashboard")
    @allure.story("Verify Mumin Dashboard Heading")
    def test_dashboard_heading(self, setup, login):
        self.page = login
        self.m_tile = MuminDashboardPage(self.page)
        # expected = "Mumin Dashboards"
        with allure.step("Verify Mumin Dashboard Heading is displayed correctly"):
            dashboard_text_frontend = self.m_tile.verify_mumin_dashboard_heading()
            try:
                assert dashboard_text_frontend == expected, \
                    f"Test failed: Expected '{expected}', but got '{dashboard_text_frontend}'."
                self.logger.info(f"✅ Verified heading successfully. Expected & Actual: {dashboard_text_frontend}")
                allure.attach(dashboard_text_frontend, name="Dashboard Heading",
                              attachment_type=allure.attachment_type.TEXT)
            except AssertionError as e:
                screenshot_path = "Screenshots/dashboard_heading.png"
                self.page.screenshot(path=screenshot_path)
                allure.attach.file(screenshot_path, name="Heading Mismatch Screenshot",
                                   attachment_type=allure.attachment_type.PNG)
                self.logger.error(f"❌ Heading mismatch! Expected: '{expected}', Actual: '{dashboard_text_frontend}'")
                raise e  # Test fail hoga aur Allure me visible hoga
        self.page.wait_for_timeout(1000)

    @pytest.mark.sanity
    @allure.feature("Dashboard")
    @allure.story("Verify the dashboard tile count with db all filter")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_dashboard_tile(self, setup, login, elaam_prod):
        self.page = login
        self.niyats_tile = MuminDashboardPage(self.page)
        total_niyat_count_widget, total_niyat_count_db,active_niyat_count_widget,active_count_db,approval_pending_niyat_count_widget,approval_pending_db,completed_niyat_count_widget,completed_count_db,total_niyat_count_add_all_status,total_niyat_count_db= self.niyats_tile.verify_dashboard_tile_all_filter(elaam_prod)
        with allure.step("Match all widgets count with the database count for the total niyat, active, pending, completed"):
            try:
                assert total_niyat_count_widget == total_niyat_count_db, f"Expected  total niyats count  in db '{total_niyat_count_db}', but got on widget '{total_niyat_count_widget}'"
                assert active_niyat_count_widget == active_count_db, f"Expected active niyat count in bd {active_count_db}, but got on widget {active_niyat_count_widget}"
                assert approval_pending_niyat_count_widget == approval_pending_db, f"Expected approval pending niyat count in db {approval_pending_db}, but got on widget ' {approval_pending_niyat_count_widget}"
                assert completed_niyat_count_widget == completed_count_db, f"Expected completed niyat count {completed_count_db}, but got on widget {completed_niyat_count_widget}"
                assert total_niyat_count_add_all_status == total_niyat_count_db, f"Expected total niyat count in db {total_niyat_count_db}, but got total niyat count after adding all status{total_niyat_count_add_all_status}"
                self.logger.info(f"*********Expected  total niyats count  in db: {total_niyat_count_db}, but got on widget: {total_niyat_count_widget}*****")
                self.logger.info(f"*********Expected active niyat count in bd: {active_count_db}, but got on widget: {active_niyat_count_widget}*****")
                self.logger.info(f"*********Expected approval pending niyat count in db: {approval_pending_db}, but got on widget: {approval_pending_niyat_count_widget}*****")
                self.logger.info(f"*********Expected completed niyat count: {completed_count_db}, but got on widget: {completed_niyat_count_widget}*****")
                self.logger.info(f"*********Expected total niyat count in db: {total_niyat_count_db}, but got total niyat count after adding all status: {total_niyat_count_add_all_status}*****")
                self.logger.info(f"********Verify the all widgets count with the database count for the total niyat, active, pending, completed**********")
            except AssertionError as e:
                self.page.screenshot(path="Screenshots/widget_count.png")
                allure.attach.file("Screenshots/widget_count.png", name="Widget count match failed", attachment_type=allure.attachment_type.PNG)
                raise e

    @pytest.mark.regression
    @pytest.mark.sanity
    @allure.feature("Dashboard")
    @allure.story("Verify the dashboard tile count with db for 1 month filter")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_dashboard_widget_for_1_month(self, setup,login,elaam_prod):
        self.page=login
        self.month_1_filter = MuminDashboardPage(self.page)
        self.month_1_filter.click_duration_drop_down_and_select_1_month_filter()
        total_niyat_count_widget_for_1_month,total_niyat_count_db_for_1_month,active_niyat_count_widget_for_1_month,active_count_db,approval_pending_niyat_count_widget_for_1_month,approval_pending_db,completed_niyat_count_widget_for_1_month,completed_count_db,total_niyat_count_add_all_status= self.month_1_filter.verify_dashboard_tile_1_month_filter(elaam_prod)
        with allure.step("Match all widgets count with the database count for the total niyat, active, pending, completed for 1 month data"):
            try:
                assert total_niyat_count_widget_for_1_month == total_niyat_count_db_for_1_month, f"Expected  total niyats count  in db '{total_niyat_count_db_for_1_month}', but got on widget '{total_niyat_count_widget_for_1_month}'"
                assert active_niyat_count_widget_for_1_month == active_count_db, f"Expected active niyat count in bd {active_count_db}, but got on widget {active_niyat_count_widget_for_1_month}"
                assert approval_pending_niyat_count_widget_for_1_month == approval_pending_db, f"Expected approval pending niyat count in db {approval_pending_db}, but got on widget ' {approval_pending_niyat_count_widget_for_1_month}"
                assert completed_niyat_count_widget_for_1_month == completed_count_db, f"Expected completed niyat count {completed_count_db}, but got on widget {completed_niyat_count_widget_for_1_month}"
                assert total_niyat_count_add_all_status == total_niyat_count_db_for_1_month, f"Expected total niyat count in db {total_niyat_count_db_for_1_month}, but got total niyat count after adding all status{total_niyat_count_add_all_status}"
                self.logger.info(f"****Expected  total niyats count  in db '{total_niyat_count_db_for_1_month}', but got on widget '{total_niyat_count_widget_for_1_month}'*****")
                self.logger.info(f"****Expected active niyat count in bd {active_count_db}, but got on widget {active_niyat_count_widget_for_1_month}*****")
                self.logger.info(f"****Expected approval pending niyat count in db {approval_pending_db}, but got on widget ' {approval_pending_niyat_count_widget_for_1_month}*****")
                self.logger.info(f"****Expected completed niyat count {completed_count_db}, but got on widget {completed_niyat_count_widget_for_1_month}*****")
                self.logger.info(f"****Expected total niyat count in db {total_niyat_count_db_for_1_month}, but got total niyat count after adding all status{total_niyat_count_add_all_status}*****")
                self.logger.info("*****Verify all widget count for 1 month filter successfully.******")
            except AssertionError as e:
                self.page.screenshot(path="Screenshots/widget_count_for_1_month.png")
                allure.attach.file("Screenshots/widget_count_for_1_month.png", name="Widget count match failed  for 1 month",
                                   attachment_type=allure.attachment_type.PNG)
                raise e

    @pytest.mark.regression
    @pytest.mark.sanity
    @allure.feature("Dashboard")
    @allure.story("Verify the dashboard tile count with db for 3 months filter")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_dashboard_widget_for_3_months(self, setup, login, elaam_prod):
        self.page = login
        self.month_3_filter = MuminDashboardPage(self.page)
        self.month_3_filter.click_duration_drop_down_and_select_3_month_filter()
        total_niyat_count_widget_for_3_month,total_niyat_count_db_for_3_month,active_niyat_count_widget_for_3_month,active_count_db, approval_pending_niyat_count_widget_for_3_month,approval_pending_db,completed_niyat_count_widget_for_3_month,completed_count_db,total_niyat_count_add_all_status,total_niyat_count_db_for_3_month = self.month_3_filter.verify_dashboard_tile_3_month_filter(elaam_prod)
        with allure.step(
                "Match all widgets count with the database count for the total niyat, active, pending, completed for 3 months data"):
            try:
                assert total_niyat_count_widget_for_3_month == total_niyat_count_db_for_3_month, f"Expected  total niyats count  in db '{total_niyat_count_db_for_3_month}', but got on widget '{total_niyat_count_widget_for_3_month}'"
                assert active_niyat_count_widget_for_3_month == active_count_db, f"Expected active niyat count in bd {active_count_db}, but got on widget {active_niyat_count_widget_for_3_month}"
                assert approval_pending_niyat_count_widget_for_3_month == approval_pending_db, f"Expected approval pending niyat count in db {approval_pending_db}, but got on widget ' {approval_pending_niyat_count_widget_for_3_month}"
                assert completed_niyat_count_widget_for_3_month == completed_count_db, f"Expected completed niyat count {completed_count_db}, but got on widget {completed_niyat_count_widget_for_3_month}"
                assert total_niyat_count_add_all_status == total_niyat_count_db_for_3_month, f"Expected total niyat count in db {total_niyat_count_db_for_3_month}, but got total niyat count after adding all status{total_niyat_count_add_all_status}"
                self.logger.info(f"***Expected  total niyats count  in db '{total_niyat_count_db_for_3_month}', but got on widget '{total_niyat_count_widget_for_3_month}'*****")
                self.logger.info(f"***Expected active niyat count in bd {active_count_db}, but got on widget {active_niyat_count_widget_for_3_month}*****")
                self.logger.info(f"***Expected approval pending niyat count in db {approval_pending_db}, but got on widget ' {approval_pending_niyat_count_widget_for_3_month}*****")
                self.logger.info(f"***Expected completed niyat count {completed_count_db}, but got on widget {completed_niyat_count_widget_for_3_month}*****")
                self.logger.info(f"***Expected total niyat count in db {total_niyat_count_db_for_3_month}, but got total niyat count after adding all status{total_niyat_count_add_all_status}*****")
                self.logger.info("*****Verify all widget count for 3 month filter successfully.******")
            except AssertionError as e:
                self.page.screenshot(path="Screenshots/widget_count_for_3_months.png")
                allure.attach.file("Screenshots/widget_count_for_3_months.png", name="widget count is not match for 3 month", attachment_type=allure.attachment_type.PNG)

    @pytest.mark.regression
    @pytest.mark.sanity
    @allure.feature("Dashboard")
    @allure.story("Verify the dashboard tile count with db for 6 months filter")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_dashboard_widget_for_6_months(self, setup, login, elaam_prod):
        self.page = login
        self.month_6_filter = MuminDashboardPage(self.page)
        self.month_6_filter.click_duration_drop_down_and_select_6_months_filter()
        total_niyat_count_widget_for_6_month, total_niyat_count_db_for_6_month,active_niyat_count_widget_for_6_month,active_count_db,approval_pending_niyat_count_widget_for_6_month,approval_pending_db,completed_niyat_count_widget_for_6_month,completed_count_db,total_niyat_count_add_all_status,total_niyat_count_db_for_6_month= self.month_6_filter.verify_dashboard_tile_6_month_filter(elaam_prod)
        with allure.step(
                "Match all widgets count with the database count for the total niyat, active, pending, completed for 6 months data"):
            try:
                assert total_niyat_count_widget_for_6_month == total_niyat_count_db_for_6_month, f"Expected  total niyats count  in db '{total_niyat_count_db_for_6_month}', but got on widget '{total_niyat_count_widget_for_6_month}'"
                assert active_niyat_count_widget_for_6_month == active_count_db, f"Expected active niyat count in bd {active_count_db}, but got on widget {active_niyat_count_widget_for_6_month}"
                assert approval_pending_niyat_count_widget_for_6_month == approval_pending_db, f"Expected approval pending niyat count in db {approval_pending_db}, but got on widget ' {approval_pending_niyat_count_widget_for_6_month}"
                assert completed_niyat_count_widget_for_6_month == completed_count_db, f"Expected completed niyat count {completed_count_db}, but got on widget {completed_niyat_count_widget_for_6_month}"
                assert total_niyat_count_add_all_status == total_niyat_count_db_for_6_month, f"Expected total niyat count in db {total_niyat_count_db_for_6_month}, but got total niyat count after adding all status{total_niyat_count_add_all_status}"
                self.logger.info(f"******Expected  total niyats count  in db: '{total_niyat_count_db_for_6_month}, but got on widget: {total_niyat_count_widget_for_6_month}********")
                self.logger.info(f"*****Expected active niyat count in bd: {active_count_db}, but got on widget: {active_niyat_count_widget_for_6_month}********")
                self.logger.info(f"***Expected approval pending niyat count in db: {approval_pending_db}, but got on widget : {approval_pending_niyat_count_widget_for_6_month}********")
                self.logger.info(f"*****Expected completed niyat count: {completed_count_db}, but got on widget: {completed_niyat_count_widget_for_6_month}********")
                self.logger.info(f"***********Expected total niyat count in db: {total_niyat_count_db_for_6_month}, but got total niyat count after adding all status: {total_niyat_count_add_all_status}********")
                self.logger.info("*****Verify all widget count for 6 months filter successfully.******")
            except AssertionError as e:
                self.page.screenshot(path="Screenshots/widget_count_for_6_months.png")
                allure.attach.file("Screenshots/widget_count_for_6_months.png", name="widget count is not match for 6 months",
                                   attachment_type=allure.attachment_type.PNG)

    @pytest.mark.regression
    @pytest.mark.sanity
    @allure.feature("Dashboard")
    @allure.story("Verify the dashboard tile count with db for 1 year filter")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_dashboard_widget_for_1_year(self, setup, login, elaam_prod):
            self.page = login
            self.year_1_filter = MuminDashboardPage(self.page)
            self.year_1_filter.click_duration_drop_down_and_select_1_year_filter()
            total_niyat_count_widget_for_1_year, total_niyat_count_db_for_1_year,active_niyat_count_widget_for_1_year,active_count_db, approval_pending_niyat_count_widget_for_1_year,approval_pending_db,completed_niyat_count_widget_for_1_year,completed_count_db,total_niyat_count_add_all_status,total_niyat_count_db_for_1_year= self.year_1_filter.verify_dashboard_tile_1_year_filter(elaam_prod)
            with allure.step(
                    "Match all widgets count with the database count for the total niyat, active, pending, completed for 6 months data"):
                try:
                    assert total_niyat_count_widget_for_1_year == total_niyat_count_db_for_1_year, f"Expected  total niyats count  in db '{total_niyat_count_db_for_1_year}', but got on widget: '{total_niyat_count_widget_for_1_year}'"
                    assert active_niyat_count_widget_for_1_year == active_count_db, f"Expected active niyat count in bd {active_count_db}, but got on widget {active_niyat_count_widget_for_1_year}"
                    assert approval_pending_niyat_count_widget_for_1_year == approval_pending_db, f"Expected approval pending niyat count in db {approval_pending_db}, but got on widget : {approval_pending_niyat_count_widget_for_1_year}"
                    assert completed_niyat_count_widget_for_1_year == completed_count_db, f"Expected completed niyat count {completed_count_db}, but got on widget {completed_niyat_count_widget_for_1_year}"
                    assert total_niyat_count_add_all_status == total_niyat_count_db_for_1_year, f"Expected total niyat count in db '{total_niyat_count_db_for_1_year}', but got total niyat count after adding all status: {total_niyat_count_add_all_status}'"
                    self.logger.info(f"********Expected  total niyats count  in db: '{total_niyat_count_db_for_1_year}', but got on widget : {total_niyat_count_widget_for_1_year}*********")
                    self.logger.info(f"******Expected active niyat count in bd: {active_count_db}, but got on widget: {active_niyat_count_widget_for_1_year}****")
                    self.logger.info(f"*****Expected approval pending niyat count in db : {approval_pending_db}, but got on widget : {approval_pending_niyat_count_widget_for_1_year}*****")
                    self.logger.info(f"********Expected completed niyat count: {completed_count_db}, but got on widget: {completed_niyat_count_widget_for_1_year}***********")
                    self.logger.info(f"********Expected total niyat count in db: {total_niyat_count_db_for_1_year}, but got total niyat count after adding all status: {total_niyat_count_add_all_status}'**********")
                    self.logger.info("*****Verify all widget count for 1 year filter successfully.******")
                except AssertionError as e:
                    self.page.screenshot(path="Screenshots/widget_count_for_1_year.png")
                    allure.attach.file("Screenshots/widget_count_for_1_year.png", name="widget count is not match for 1 year",
                                       attachment_type=allure.attachment_type.PNG)

    @pytest.mark.regression
    @allure.feature("Dashboard")
    @allure.story("Verify the total trophy count with db")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_total_trophy_count(self, setup, login, elaam_prod):
        self.page = login
        self.TC = MuminDashboardPage(self.page)
        total_trophy_count_from_db, total_trophys_count_from_ui = self.TC.get_total_trophies_counts(elaam_prod)
        with allure.step("Match trophy count with the database count for the trophy"):
            try:
                assert total_trophy_count_from_db == total_trophys_count_from_ui, f"Expected total trophy count form db:{total_trophy_count_from_db} but got form UI {total_trophys_count_from_ui}"
                self.logger.info(f"Expected total trophy count form db:{total_trophy_count_from_db} but got form UI {total_trophys_count_from_ui}")
                self.logger.info("******The total trophy count are matched with DB count*******")
            except AssertionError as e:
                self.page.screenshot(path="Screenshots/total_trophy_count.png")
                allure.attach.file("Screenshots/total_trophy_count.png", name="Total Trophy count is not match with db",
                                   attachment_type=allure.attachment_type.PNG)

    @pytest.mark.regression
    @pytest.mark.sanity
    @allure.feature("Dashboard")
    @allure.story("Verify the trophies redeemed count with db")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_trophies_redeemed_count(self,setup,login, elaam_prod):
        self.page=login
        self.TC= MuminDashboardPage(self.page)
        total_trophies_redeemed_count_from_db,troghies_reedeemd_count_from_ui = self.TC.get_trophies_redeemed_counts(elaam_prod)
        with allure.step("Match trophies redeemed count with the database count for the trophies redeemed"):
            try:
                assert total_trophies_redeemed_count_from_db == troghies_reedeemd_count_from_ui, f"Expected total trophies redeemed count form db:{total_trophies_redeemed_count_from_db} but got form UI {troghies_reedeemd_count_from_ui}"
                self.logger.info(f"********Expected total trophies redeemed count form db:{total_trophies_redeemed_count_from_db} but got form UI {troghies_reedeemd_count_from_ui}***********")
                self.logger.info("******The total trophies redeemed count are matched with DB count*******")
            except AssertionError as e:
                self.page.screenshot(path="Screenshots/trophies_redeemed_count.png")
                allure.attach.file("Screenshots/trophies_redeemed_count.png", name="total trophies redeemed count are not matched with DB count",
                                   attachment_type=allure.attachment_type.PNG)

    @pytest.mark.regression
    @pytest.mark.sanity
    @allure.feature("Dashboard")
    @allure.story("Verify the redeemed now and it's navigation")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_redeem_now_and_verify_navigation(self,setup,login):
        self.page=login
        self.RD = MuminDashboardPage(self.page)
        current_url = self.RD.click_redeem_now_and_verify_navigation()
        with allure.step("CLick on the redeemed now button and verify it's navigation"):
            try:
                assert expected_path in current_url, (
                    f"Expected path '{expected_path}' not found in URL: {current_url}")
                self.logger.info(f"*****Expected path: {expected_path}, current path:  {current_url}******")
                self.logger.info("******The redeemed Now button is clicked successfully and the user is redirected to the catalogue page*******")
            except AssertionError as e:
                self.page.screenshot(path="Screenshots/redeem_now_navigation.png")
                allure.attach.file("Screenshots/redeem_now_navigation.png", name="Click redeem now button and check the navigation",
                                   attachment_type=allure.attachment_type.PNG)

    @pytest.mark.regression
    @allure.feature("Dashboard")
    @allure.story("Verify the total niyat count with the total pagination count")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_total_niyat_count_with_pagination_niyat_count(self,setup,login):
        self.page=login
        self.TP_count = MuminDashboardPage(self.page)
        self.TP_count.click_dashboard_menu()
        total_count_pagination, total_niyat_count_widget= self.TP_count.get_total_niyat_count_and_match_pagination_count()
        with allure.step("Verify the total niyat count with the total niyats in pagination count"):
            try:
                assert total_count_pagination==total_niyat_count_widget,(f"Mismatch Found ❌: widget Count = {total_niyat_count_widget}, pagination Count = {total_count_pagination}")
                self.logger.info(f"******widget count: {total_niyat_count_widget}, pagination count:{total_count_pagination}**********")
                self.logger.info("**** Total Niyat widget count are matched with pagination count**")
            except AssertionError as e:
                self.page.screenshot(path="Screenshots/total_niyat_pagination.png")
                allure.attach.file("Screenshots/total_niyat_pagination.png", name="Total niyat count is not match with total niyat count in pagination",
                                   attachment_type=allure.attachment_type.PNG)

    @pytest.mark.regression
    @pytest.mark.sanity
    @allure.feature("Dashboard")
    @allure.story("Verify the search is working with FMB and match the total pagination count")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_search_by_first_fmb_umoor_name_and_validate_with_pagination_count_after_search(self, setup, login, elaam_prod):
        self.page = login
        self.search = MuminDashboardPage(self.page)
        db_count, ui_count = self.search.search_by_first_fmb_umoor_name_and_validate_with_pagination_count_after_search(elaam_prod)
        with allure.step("The search is working with FMB and match the total pagination count"):
            try:
                assert db_count == ui_count,(f"Mismatch Found ❌: DB Count = {db_count}, UI Count = {ui_count}")
                self.logger.info(f"******DB count: {db_count}, UI count {ui_count}**********")
                self.logger.info("********Search is working fine*******")
            except AssertionError as e:
                self.page.screenshot(path="Screenshots/search_pagination.png")
                allure.attach.file("Screenshots/search_pagination.png", name="After search data count is not match with pagination count",
                                   attachment_type=allure.attachment_type.PNG)

    @pytest.mark.regression
    @pytest.mark.sanity
    @allure.feature("Dashboard")
    @allure.story("Verify the niyat information page")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_niyat_information(self,setup,login):
        self.page = login
        self.niyat_info = MuminDashboardPage(self.page)
        niyat_question,niyat_question_information_page =self.niyat_info.test_verify_niyat_question()
        with allure.step("The niyat information page opened and the compare with the niyat question form list"):
            try:
                assert niyat_question== niyat_question_information_page, f"Expected niyat question on info page{niyat_question}, but got {niyat_question_information_page}"
                self.logger.info(f"*********Expected niyat question on info page: {niyat_question}, but got {niyat_question_information_page}******")
                self.logger.info("****niyat question and nitay question on information page are matched****")
            except AssertionError as e:
                self.page.screenshot(path="Screenshots/niyat_information.png")
                allure.attach.file("Screenshots/niyat_information.png", name="Niyat information question is not matched with the list question",
                                   attachment_type=allure.attachment_type.PNG)

    @pytest.mark.regression
    @pytest.mark.sanity
    @allure.feature("Dashboard")
    @allure.story("Back button functionality on niyat information page")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_click_back_button_niyat_information_page_navigation_mumin_dashboard_page(self,setup,login):
        self.page = login
        self.niyat_back_button = MuminDashboardPage(self.page)
        self.niyat_back_button.click_back_button_niyat_information_page_navigation_mumin_dashboard_page()
        dashboard_text_frontend =self.niyat_back_button.verify_mumin_dashboard_heading()
        with allure.step("Verify the user is redirected to the mumin dashboard after click on the back button"):
            try:
                assert dashboard_text_frontend == expected,f"Test failed: Expected '{expected}', but the actual text was '{dashboard_text_frontend}'."
                self.logger.info(f"*****Expected Heading: {expected}, but got in actual: {dashboard_text_frontend} ")
                self.logger.info("******Verify the mumin dashboard heading****")
            except AssertionError as e:
                self.page.screenshot(path="Screenshots/back_button_niyat_information.png")
                allure.attach.file("Screenshots/back_button_niyat_information.png",
                                   name="back button functionality on Niyat information is not working and screenshot capture",
                                   attachment_type=allure.attachment_type.PNG)

    @pytest.mark.regression
    @allure.title("Dashboard")
    @allure.description("The item per page and pagination and row count matched")
    def test_click_item_per_page_drop_down_and_compare_data_with_rows_and_select_value(self,setup,login):
        self.page= login
        self.item_per_page = MuminDashboardPage(self.page)
        try:
            total_count_pagination, row_count, random_value= self.item_per_page.click_item_per_page_drop_down_and_compare_data_with_rows_and_select_value()
            self.logger.info("***click_item_per_page_drop_down_and_compare_data_with_rows_and_select_value****")
            assert total_count_pagination == row_count, f" rows count displayed: {row_count},and pagination count : {total_count_pagination}"
            self.logger.info(f"***The item per page count:{random_value} and pagination count : {total_count_pagination}, matched with row count is displayed: {row_count}***")
        except AssertionError as e:
            self.page.screenshot(path="Screenshots/item_per_page_pagination_count.png")
    #         allure.attach.file("Screenshots/item_per_page_pagination_count.png", name="item per page and pagination count", attachment_type=allure.attachment_type.PNG)


    ##-------IT is not working till now need to complete this because the send messgae page going blank----------####
    @pytest.mark.regression
    @pytest.mark.sanity
    @allure.title("Send Message")
    @allure.description("Verify the send message functionality is working")
    def test_send_message_functionality(self,setup,login):
        self.page=login
        self.send_message = MuminDashboardPage(self.page)
        success_message = self.send_message.send_message_functionality()
        try:
            assert success_message.strip() == expected_text, f"Expected : {expected_text}, but got: {success_message}"
            self.logger.info(f"******The success message : {success_message} and the expected text: {expected_text}*****")
        except AssertionError as e:
            self.page.screenshot(path="Screenshots/send_message.png")
            allure.attach(success_message, name="Success Message", attachment_type=allure.attachment_type.TEXT)

        ## below test case is in-progress
    def test_request_for_update(self,setup,login):
        self.page = login
        self.req_update = MuminDashboardPage(self.page)
        self.req_update.request_for_update()


    @pytest.mark.regression
    @pytest.mark.sanity
    @allure.title("Request For Update Functionality")
    @allure.description("Verify that after clicking 'Request For Update', either Mubarak with trophy is displayed or request goes to Pending state.")
    def test_request_for_update(self, setup, login):
        expect_success_message = "Niyat Details Has Been Update."
        self.page = login
        self.request_update = MuminDashboardPage(self.page)
        # Step 1: Click on button
        success_message_request_for_update =self.request_update.click_request_for_update()
        assert success_message_request_for_update == expect_success_message, f"Expected message : {expect_success_message}, but get success message: {success_message_request_for_update}"
        self.logger.info(f"********Expected message : {expect_success_message}, but get success message: {success_message_request_for_update}*******")



        # Step 2: Get actual outcome
        actual_outcome = self.request_update.get_outcome_message()
        print("Actual out come:", actual_outcome)

        # Step 3: Validate outcomes
        expected_outcomes = ["MUBARAK", "PENDING"]

        try:
            expected_outcomes = ["MUBARAK", "PENDING"]
            assert actual_outcome in expected_outcomes, f"Expected {expected_outcomes}, but got: {actual_outcome}"
            self.logger.info(f"****** Test Passed with outcome: {actual_outcome} *****")
        except AssertionError as e:
            # Screenshot on failure
            screenshot_path = "Screenshots/request_for_update.png"
            self.page.screenshot(path=screenshot_path)

            # Attach evidence to Allure report
            allure.attach.file(screenshot_path, name="Failure Screenshot", attachment_type=allure.attachment_type.PNG)
            allure.attach(actual_outcome, name="Actual Outcome", attachment_type=allure.attachment_type.TEXT)

            raise e
















