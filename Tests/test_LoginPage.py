import time

import pytest

from Config.config import TestData
from Pages.LoginPage import LoginPage


@pytest.mark.usefixtures("init_driver")
class TestLoginPage:

    def test_valid_login(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.enter_username(TestData.USER_NAME)
        self.loginPage.enter_password(TestData.PASSWORD)
        presence = self.loginPage.click_login_button()
        assert presence, "Error message not displayed"


