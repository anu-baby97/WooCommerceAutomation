from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage


class DashboardPage(BasePage):
    # web elements
    welcome_message = (By.XPATH, "//div[@class='woocommerce-MyAccount-content']")

    # constructor
    def __init__(self, driver):
        super().__init__(driver)

    # page actions

    def is_welcome_message_displayed(self):
        return self.is_element_displayed(self.welcome_message)


