from Test_Cases.conftest import setup, login
from Utilities.CustomLoggers import LogGen
from pageObjects.tickets_page.Ticket_Add_Depot_Entity import AddTicketDepotEntity


class TestAddTicket:
     logger = LogGen.loggen()

     def test_add_ticket(self, setup, login):
         self.page = login
         self.ticket = AddTicketDepotEntity(self.page)
         self.ticket.click_ticket_module()
         self.logger.info("****The user is redirected on the ticket listing page****")
         self.ticket.total_ticket_initial_count()
         self.logger.info("******The total tickets initial count store successfully*****")
         self.ticket.total_ticket_for_depot_count_initial()
         self.logger.info("******The total tickets depots initial count store successfully*****")
         self.ticket.click_add_ticket_button()
         self.logger.info("****The user is redirected on the add ticket page***")
         self.ticket.click_entity_type_dropdown()
         self.logger.info("****Successfully click on the entity type dropdown***")
         self.ticket.select_entity_type_dropdown_value()
         self.logger.info("****The entity type dropdown value successfully***")
         self.ticket.click_ticket_type_dropdown()
         self.logger.info("****Successfully click on the ticket type dropdown***")
         self.ticket.select_ticket_type_dropdown_value()
         self.logger.info("****select the ticket type dropdown value successfully***")
         self.ticket.fill_description_field()
         self.logger.info("***Input the description successfully***")
         self.ticket.click_ticket_priority_dropdown()
         self.logger.info("****Successfully click on the ticket priority dropdown****")
         self.ticket.select_ticket_priority_dropdown_value_urgent()
         self.logger.info("*******Select the ticket priority value urgent successfully******")
         self.ticket.click_fleet_name_dropdown()
         self.logger.info("****Successfully click on the fleet name dropdown****")
         self.ticket.select_fleet_dropdown_value()
         self.logger.info("*******Select the fleet name value successfully******")
         self.ticket.click_depot_name_dropdown()
         self.logger.info("****Successfully click on the depot name dropdown****")
         self.ticket.select_depot_dropdown_value()
         self.logger.info("*******Select the depot name value successfully******")
         self.ticket.click_assignee_to_dropdown()
         self.logger.info("****Successfully click on the assignee to dropdown****")
         self.ticket.select_assignee_to_dropdown_value()
         self.logger.info("*******Select the assignee to name value successfully******")
         self.ticket.click_submit_button()
         self.logger.info("*****The ticket is created successfully and count are matched with is increased ****")














