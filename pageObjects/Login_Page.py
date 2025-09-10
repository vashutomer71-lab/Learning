from playwright.sync_api import Page

class Login:
    textbox_its_id = "//input[@formcontrolname='itsId']"
    textbox_password_id = "//input[@formcontrolname='password']"
    button_login_xpath = "//button[@type='submit']"
    role_xpath= "//li[normalize-space(text())='Mumin']"


    def __init__(self, page: Page):
        self.page = page

    def setUserName(self, username):
        self.page.fill(f"xpath={self.textbox_its_id}", username)

    def setPassword(self, password):
        self.page.fill(f"xpath={self.textbox_password_id}", password)

    def login(self):
        self.page.click(f"xpath={self.button_login_xpath}")
    def click_mumin_role(self):
        self.page.click(f"xpath={self.role_xpath}")


