import time

from playwright.sync_api import Page
from playwright.sync_api import sync_playwright

class Login:
    textbox_username_id = "email"
    textbox_password_id = "password"
    button_login_xpath = "//button[@type='submit']"



    def __init__(self,page:Page):
        self.page = page


    def setUserName(self, username):
        self.page.fill(f'#{self.textbox_username_id}', username)

    def setPassword(self, password):
        self.page.fill(f'#{self.textbox_password_id}', password)

    def login(self):
        self.page.click(self.button_login_xpath)






