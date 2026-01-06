from Test_Cases.conftest import login, setup, fetch_data, access_token, fetch_data_transform_db
from pageObjects.fleet_dashboard_page import FleetDashboardPage

class TestFleetDashboard:

    def test_fleet_dashboard_tile(self,setup,login, fetch_data, access_token):
        self.page = login
        self.fd_tile = FleetDashboardPage(self.page)
        self.fd_tile.verify_fleet_dashboard_heading()
        self.fd_tile.verify_fleet_tiles_text()
        self.fd_tile.verify_fleet_counts_on_tile(fetch_data)
    #
    # def test_vehicle_tile(self, setup,login, fetch_data_transform_db):
    #     self.page = login
    #     self.vd_tile = FleetDashboardPage(self.page)
    #     self.vd_tile.verify_vehicle_tile(fetch_data_transform_db)

    # def test_depot_tile(self, setup, login, fetch_data):
    #     self.page= login
    #     self.fd_tile=FleetDashboardPage(self.page)
    #     self.fd_tile.verify_depot_tile(fetch_data)

    # def test_charger_tile(self, setup, login, fetch_data):
    #     self.page= login
    #     self.fd_tile=FleetDashboardPage(self.page)
    #     self.fd_tile.verify_chargers_tile(fetch_data)
    #
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

    def test_charging_infrastructure_bottom_card(self,setup, login, fetch_data ):
        self.page = login
        self.CI = FleetDashboardPage(self.page)
        self.CI.verify_charging_infrastructure_bottom_card(fetch_data)






