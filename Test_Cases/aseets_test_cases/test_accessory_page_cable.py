from pageObjects.assets_page.accessory_page_cable import AccessoryPageCable
from Test_Cases.conftest import login, setup
from Utilities.CustomLoggers import LogGen

class TestAccessory:
    logger = LogGen.loggen()

    def test_accessory(self, setup, login):
        """""
        'Test case to verify the add accessory functionality'
        """""

        self.page = login
        self.logger.info("****Login successfully Completed*******")
        self.acc = AccessoryPageCable(self.page)
        self.logger.info("*****Redirect on the accessory page****")
        self.acc.click_assets()
        self.logger.info("******Click on the assets menu successfully*******")
        self.acc.click_accessory_tab()
        self.logger.info("****Click on the accessory tab successfully***")
        self.acc.verify_accessory_total_count()
        self.logger.info("******Accessory total Initial count****")
        self.acc.verify_accessory_cable_initial_count()
        self.logger.info("******Accessory cable total Initial count*******")
        self.acc.click_add_accessory_button()
        self.logger.info("****The user redirected on the add accessory page***")
        self.acc.click_fleet_name_dropdown_and_select_value()
        self.logger.info("****Select the fleet name successfully***")
        self.acc.click_depot_name_dropdown_and_select_value()
        self.logger.info("***Select the depot name successfully ***")
        self.acc.click_accessory_dropdown_and_select_value()
        self.logger.info("****Select the accessory category value****")
        self.acc.click_fill_serial_number()
        self.logger.info("****Fill serial number successfully****")
        self.acc.click_fill_device_id()
        self.logger.info("***Fill device id successfully***")
        self.acc.click_status_dropdown_and_select_value()
        self.logger.info("***Select the status successfully ***")
        self.acc.click_make_id_dropdown_and_select_value()
        self.logger.info("***Select the make name successfully ***")
        self.acc.click_model_id_dropdown_and_select_value()
        self.logger.info("***Select the model successfully ***")
        self.acc.click_warranty_start_date()
        self.logger.info("***Select the warranty start date successfully ***")
        self.acc.click_warranty_end_date()
        self.logger.info("***Select the warranty end date successfully ***")
        self.acc.click_submit_button_verify_updated_count()
        self.logger.info("*****Accessory count updated successfully*****")


