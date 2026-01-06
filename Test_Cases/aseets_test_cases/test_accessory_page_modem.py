from pageObjects.assets_page.accessory_page_modem import AccessoryPageModel
from Test_Cases.conftest import login, setup
from Utilities.CustomLoggers import LogGen

class TestAccessoryModel:
    logger = LogGen.loggen()

    def test_accessory(self, setup, login):
        """""
        'Test case to verify the add accessory functionality'
        """""

        self.page = login
        self.logger.info("****Login successfully Completed*******")
        self.acm = AccessoryPageModel(self.page)
        self.logger.info("*****Redirect on the accessory page****")
        self.acm.click_assets()
        self.logger.info("******Click on the assets menu successfully*******")
        self.acm.click_accessory_tab()
        self.logger.info("****Click on the accessory tab successfully***")
        self.acm.verify_accessory_count()
        self.logger.info("******Initial count****")
        self.acm.verify_accessory_modem_count()
        self.logger.info("******Modem Initial count****")
        self.acm.click_add_accessory_button()
        self.logger.info("****The user redirected on the add accessory page***")
        self.acm.click_fleet_name_dropdown_and_select_value()
        self.logger.info("****Select the fleet name successfully***")
        self.acm.click_depot_name_dropdown_and_select_value()
        self.logger.info("***Select the depot name successfully ***")
        self.acm.click_accessory_dropdown_and_select_value()
        self.logger.info("****Select the accessory category value modem****")
        self.acm.click_fill_serial_number()
        self.logger.info("****Fill serial number successfully****")
        self.acm.click_fill_device_id()
        self.logger.info("***Fill device id successfully***")
        self.acm.click_status_dropdown_and_select_value()
        self.logger.info("***Select the status successfully ***")
        self.acm.click_fill_carrier_name()
        self.logger.info("*******Fill carrier name*******")
        self.acm.click_fill_imei_number()
        self.logger.info("******Fill imei number*****")
        self.acm.click_fill_ip_address()
        self.logger.info("******Fill id address *****")
        self.acm.click_make_id_dropdown_and_select_value()
        self.logger.info("***Select the make name successfully ***")
        self.acm.click_model_id_dropdown_and_select_value()
        self.logger.info("***Select the model successfully ***")
        self.acm.click_fill_sim_number()
        self.logger.info("*****Fill sim number ****")
        self.acm.click_select_fill_modem_type()
        self.logger.info("*****Select the modem type value******")
        self.acm.click_warranty_start_date()
        self.logger.info("***Select the warranty start date successfully ***")
        self.acm.click_warranty_end_date()
        self.logger.info("***Select the warranty end date successfully ***")
        self.acm.click_select_installation_date()
        self.logger.info("*****Select installation date ******")
        self.acm.click_submit_button_verify_updated_count()
        self.logger.info("*****Accessory count updated successfully*****")

