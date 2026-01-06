from Test_Cases.conftest import login, setup, fetch_data, fetch_data_transform_db
from pageObjects.depot_dashboard_page import DepotDashboardPage


class TestFleetDashboard:

    def test_fleet_dashboard_tile(self, setup, login, fetch_data,fetch_data_transform_db):
        self.page = login
        self.Dd_tile = DepotDashboardPage(self.page)
        self.Dd_tile.depot_click()
        self.Dd_tile.Depot_chart(fetch_data)
        self.Dd_tile.click_vehicle_breadcrumb()
        self.Dd_tile.verify_vehicle_chart(fetch_data_transform_db)
        self.Dd_tile.verify_Energy_points(fetch_data)
        self.Dd_tile.Energy_used(fetch_data)


