import time

import pytest

from Config.config import TestData
from Pages.DashboardPage import DashboardPage
from Pages.LoginPage import LoginPage


@pytest.mark.usefixtures("init_driver")
@pytest.mark.order("first")
class TestLoginPage:

    def test_valid_login(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.enter_username(TestData.USER_NAME)
        self.loginPage.enter_password(TestData.PASSWORD)
        self.loginPage.click_login_button()
        self.dashboardpage = DashboardPage(self.driver)
        assert self.dashboardpage.is_welcome_message_displayed(), "Welcome message is not displayed"
        time.sleep(2)
