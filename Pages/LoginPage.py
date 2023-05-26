from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage


class LoginPage(BasePage):
    # web elements
    username = (By.ID, "username")
    password = (By.ID, "password")
    loginButton = (By.NAME, "login")

    # constructor
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    # page actions

    def enter_username(self, uname):
        self.do_sendkeys(self.username, uname)

    def enter_password(self, pwd):
        self.do_sendkeys(self.password, pwd)

    def click_login_button(self):
        self.do_click(self.loginButton)
