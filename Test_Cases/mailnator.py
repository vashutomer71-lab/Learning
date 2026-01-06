from playwright.sync_api import sync_playwright
import uuid
import time


class TestMailinator:
    def __init__(self):
        # self.email = f"decentford{uuid.uuid4().hex[:3]}@mailinator.com"
        self.email = f"deepak@mailinator.com"
        print("email is: ", self.email)

    def open_mailinator_and_read_email(self):
        with sync_playwright() as p:
            # Launch browser
            browser = p.chromium.launch(headless=False)  # Set headless=True to run without UI
            page = browser.new_page()

            # Navigate to Mailinator
            page.goto("https://www.mailinator.com/v4/public/inboxes.jsp")

            # Fill in the email ID
            page.fill("//input[@id='inbox_field']", self.email)

            # Click the 'GO' button to open the Mailinator inbox
            page.click("//button[@class='primary-btn']")
            time.sleep(5)  # Wait for the inbox to load
            print(f"Opened Mailinator inbox for email: {self.email}")

            # Wait for and click the first email in the inbox list
            page.wait_for_selector("(//table[@class='table-striped jambo_table']//tbody//tr)[1]").click()
            time.sleep(5)  # Wait for the email content to load

            # Click the 'HTML' tab if necessary to view the email content
            page.wait_for_selector("//a[@id='pills-textbuthtml-tab']").click()
            time.sleep(5)

            # Switch to the iframe to read the email content
            iframe = page.frame(name="texthtml_msg_body")
            email_content = iframe.inner_text("body")  # Adjust this selector if necessary
            print("Email content is:", email_content)

            # Close the browser
            browser.close()


# Run the test
if __name__ == "__main__":
    test = TestMailinator()
    test.open_mailinator_and_read_email()
