import random
import time
import uuid
import re
from Utilities.CustomLoggers import LogGen
from Utilities.ReadProperties import ReadConfig
from pageObjects.add_depot_admin import CreateDepotAdmin


class TestAddDepotAdmin:
    application_url = ReadConfig.getApplicationURL()
    network_owner_email = ReadConfig.getUserName()
    network_owner_password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def generate_mobile_number(self):
        prefix = random.choice([7, 8, 9])
        random_digits = ''.join(random.choices('0123456789', k=9))
        mobile_number = f"+91{prefix}{random_digits}"
        return mobile_number

    def test_add_depot_admin(self, setup, login):
        self.page = setup
        self.cc = CreateDepotAdmin(self.page)

        self.logger.info("Clicking 'Add Depot Admin' button.")
        self.cc.click_add_depot_admin()

        self.logger.info("Selecting Depot Name.")
        self.cc.click_depot_name()

        self.logger.info("Entering First Name.")
        self.cc.first_name()

        self.logger.info("Entering Last Name.")
        self.cc.last_name()

        unique_email = f"decentford{uuid.uuid4().hex[:3]}@mailinator.com"
        print("email", unique_email)
        self.logger.info(f"Entering Email: {unique_email}.")
        self.cc.email(email=unique_email)

        mobile_number = self.generate_mobile_number()
        self.logger.info(f"Entering Mobile Number: {mobile_number}.")
        self.cc.mobile(number=mobile_number)

        address = "NPX Tower"
        address2 = "Sector 153"
        city = "New Delhi"
        self.logger.info(f"Entering Address: {address}, {address2}, {city}.")
        self.cc.address(address=address, address2=address2, city=city)

        self.logger.info("Depot Admin Added Successfully")

        mailinator_address = unique_email
        self.check_mailinator_inbox_for_reset_link(mailinator_address)

    def check_mailinator_inbox_for_reset_link(self, mailinator_address):
        self.page.goto("https://www.mailinator.com/v4/public/inboxes.jsp")

        # Ensure the input field is present and then fill it
        self.page.fill("//input[@id='inbox_field']", mailinator_address)
        self.page.wait_for_selector("//button[@class='primary-btn']").click()

        # Click the 'GO' button to open the Mailinator inbox
        self.page.click("//button[@class='primary-btn']")
        time.sleep(5)  # Add a delay to allow Mailinator to load the inbox
        print(f"Opened Mailinator inbox for email: {mailinator_address}")

        # Wait for and click the first email in the inbox list
        self.page.wait_for_selector("(//table[@class='table-striped jambo_table']//tbody//tr)[1]").click()
        # Click the 'HTML' tab if necessary to view the email content
        self.page.wait_for_selector("//iframe[@id='html_msg_body']").click()
        # Switch to the iframe and read the email content
        iframe = self.page.frame_locator("//iframe[@id='html_msg_body']").locator("body").inner_text()
        print("Email content is:", iframe)
        # Extract the temporary password using a regular expression
        temp_password_dot = re.search(r"temporary password is (\S+)", iframe).group(1)   #Extract the Password: A regular expression (r"temporary password is (\S+)") is used to capture the temporary password from the email content. The \S+ matches the password assuming it contains no whitespace.
        temp_password = temp_password_dot.replace(".", "")  # Remove dot characters
        print("Temporary password is:", temp_password)

        with self.page.expect_popup() as page1_info:
            self.page.frame_locator("iframe[name=\"html_msg_body\"]").get_by_role("link", name="Click here").click()
        page1 = page1_info.value
        new_email = page1.goto(f"https://fleete-qa-dashboard.demoapplication.net/resetpassword/{mailinator_address}")
        print("New email is:", new_email)

        page1.wait_for_selector("//input[@name='currentPassword']").click()
        page1.wait_for_selector("//input[@id='currentPassword']").fill(temp_password)
        time.sleep(3)

        # Set the new password and confirm it
        new_password = "Password@123"
        confirm_password = "Password@123"

        # Fill in the new password and confirm password fields
        page1.wait_for_selector("//input[@id='newPassword']").click()
        page1.wait_for_selector("//input[@id='newPassword']").fill(new_password)
        page1.wait_for_selector("//input[@id='confirmPassword']").click()
        page1.wait_for_selector("//input[@id='confirmPassword']").fill(confirm_password)
        time.sleep(3)
        page1.get_by_role("button", name="Submit").click()
        page1.wait_for_timeout(5000)

        # Define expected success message
        expected_success_message = "Success"  # Update this with the actual expected text

        # Wait for the toast message and print it
        toast_selector = "//div[@class='Toastify__toast-body']"  # Update the selector based on the actual toast element
        page1.wait_for_selector(toast_selector, timeout=5000)  # Adjust timeout if needed

        toast_message = page1.locator(toast_selector).inner_text()
        print("Toast message:", toast_message)

        # Assertion to check if the success message is as expected
        assert toast_message == expected_success_message, f"Expected success message '{expected_success_message}', but got '{toast_message}'"

        assert page1.url == "https://fleete-qa-dashboard.demoapplication.net/login"




