import time

from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage
from Pages.ProductPage import ProductPage


class QuickViewPage(BasePage):
    # web elements
    quick_view_link = (By.XPATH, "//h2[text()='RF ID Card']//parent::a//following-sibling::a[text()='Quick View']")

    # constructor
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get("https://woocommerce-850415-2933260.cloudwaysapps.com/shop")

    # page actions

    def click_quick_view_link(self):
        self.do_click(self.quick_view_link)




