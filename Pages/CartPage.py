from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage


class CartPage(BasePage):
    product_in_cart = (By.XPATH, "//a[contains(text(),'RF ID Card')]")
    proceed_to_checkout_link = (By.XPATH, "//a[contains(text(),'Proceed to checkout')]")

    def __init__(self, driver):
        super().__init__(driver)

    def is_product_in_cart_displayed(self):
        return self.is_element_displayed(self.product_in_cart)

    def click_proceed_to_checkout_link(self):
        self.do_click(self.proceed_to_checkout_link)