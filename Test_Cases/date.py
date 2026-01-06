import time

from playwright.sync_api import sync_playwright
import random



def run(playwright):
    global page, browser
    try:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()

        # Navigate to your web application
        page.goto('https://www.google.com/maps')

    except AssertionError as e:
        # If assertion fails, capture a screenshot
        page.screenshot(path="../Screenshots/menu_tab.png")
        raise AssertionError(str(e) + " Screenshot captured.")

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        raise  # This raises the current exception again
    finally:
        # It's a good practice to close the browser if it was successfully opened
        if 'browser' in locals():
            browser.close()


# def login():
#     try:
#         # Fill the username and password fields
#         page.fill('//input[@name="email"]',
#                   'superadmin@levelupenergy.com')  # Replace with the actual username field selector and value
#         page.fill('//input[@name="password"]', 'Super@123')  # Replace with the actual password field selector and value
#     except Exception as e:
#         print("Unable to login:", e)
#
# # Click the login button
# page.click(
#     '//*[@id="root"]/div[1]/div/div/div[2]/div/div[5]/button/span')  # Replace with the actual login button selector
#
# page.click('//h5[contains(text(), "Management")]')
# page.click('//h5[contains(text(), "Assets")]')
# page.click('//h5[contains(text(), "Charger")]')
# # page.click('//div[contains(text(), "ADD CHARGER")]')
# # page.wait_for_selector('//button[@type="button"]').click()
# time.sleep(10)
# count = page.inner_text('//h1[@class="widgetNew1_big_title__59l+D widgetNew1_topCardLink__AXr2h"]').strip()
# initial_count = int(count)
# print('ggggggggggggg',initial_count)
# update_count = page.inner_text('//h1[@class="widgetNew1_big_title__59l+D widgetNew1_topCardLink__AXr2h"]').strip()
# updated_count = int(update_count)
# print('hhhhhhhhhhhhhhhh',updated_count)
# if update_count == initial_count + 1:
#     print("The updated count is correct (+1).")
# else:
#     print(f"Counts do not match. Initial count: {initial_count}, Updated count: {updated_count}")

    def check_mailinator_inbox_for_reset_link(self, mailinator_address):
        self.page.goto("https://www.mailinator.com/v4/public/inboxes.jsp")

        # Ensure the input field is present and then fill it
        self.page.fill("//input[@id='inbox_field']", mailinator_address)
        self.page.wait_for_selector("//button[@class='primary-btn']").click()

        # Click the 'GO' button to open the Mailinator inbox
        self.page.click("button#go_inbox")

        time.sleep(5)  # Add a delay to allow Mailinator to load the inbox

        self.logger.info(f"Checking Mailinator inbox for {mailinator_address}.")
        # Additional steps can be added here to verify or access the email content



with sync_playwright() as playwright:
    run(playwright)
