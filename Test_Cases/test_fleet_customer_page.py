import pytest
from Utilities.CustomLoggers import LogGen
from pageObjects.FleetCustomer_Page import FleetCustomerPage
from Test_Cases.conftest import login




class TestFleetCustomer:

    def test_fleet(self, setup, login):

        self.page = login
        self.fc = FleetCustomerPage(self.page)
        self.fc.click_user_management()
        self.fc.add_Fleet_customer()






