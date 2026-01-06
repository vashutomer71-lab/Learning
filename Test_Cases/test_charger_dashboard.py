from Test_Cases.conftest import login, setup, fetch_data, access_token, fetch_data_transform_db
from pageObjects.charger_dashboard_page import ChargerDashboardPage


class TestChargerDashboard:

    def test_click_charger_menu(self,setup,login):
        self.page = login
        self.c_tile = ChargerDashboardPage(self.page)
        self.c_tile.click_charger_menu()

    def test_charger_dashboard_tile(self,setup,login):
        self.page = login
        self.c_tile = ChargerDashboardPage(self.page)
        self.c_tile.verify_charger_dashboard_heading()


    def test_charger_tile(self, setup, login, fetch_data):
        self.page= login
        self.fd_tile=ChargerDashboardPage(self.page)
        self.fd_tile.verify_chargers_tile(fetch_data)

    # def test_fleet_list_heading(self, setup, login):
    #     self.page = login
    #     self.flh= FleetDashboardPage(self.page)
    #     self.flh.verify_fleet_list_heading()
    #
    # def test_fleet_list_data(self,setup,login):
    #     self.page = login
    #     self.fl =FleetDashboardPage(self.page)
    #     self.fl.verify_fleet_list_data()
    #
    # def test_fleet_count_in_pagination(self, setup, login, fetch_data):
    #     self.page = login
    #     self.fp = FleetDashboardPage(self.page)
    #     # Call the method, passing the fetch_data function to retrieve data
    #     self.fp.verify_fleet_count_in_pagination(fetch_data)
    #
    # def test_search_functionality(self,setup,login):
    #     self.page = login
    #     self.fl =FleetDashboardPage(self.page)
    #     self.fl.verify_search_functionality()

    # def test_verify_energy_point_bottom_tile(self,setup, login, fetch_data ):
    #     self.page = login
    #     self.epb = FleetDashboardPage(self.page)
    #     self.epb.verify_energy_points(fetch_data)
    #
    # def test_verify_energy_used_bottom_tile(self,setup, login, fetch_data ):
    #     self.page = login
    #     self.eub = FleetDashboardPage(self.page)
    #     self.eub.Energy_used(fetch_data)

    # def test_charging_infrastructure_bottom_card(self,setup, login, fetch_data ):
    #     self.page = login
    #     self.CI = FleetDashboardPage(self.page)
    #     self.CI.verify_charging_infrastructure_bottom_card(fetch_data)






