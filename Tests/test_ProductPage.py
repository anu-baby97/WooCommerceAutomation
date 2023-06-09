import time

import pytest

from Config.config import TestData
from Pages.CartPage import CartPage
from Pages.ProductPage import ProductPage


@pytest.mark.usefixtures("init_driver")
@pytest.mark.order("second")
class TestProductPage:
    URL = "https://woocommerce-850415-2933260.cloudwaysapps.com/product/rf-id-card"

    # @pytest.mark.skip
    # @pytest.mark.order("second")
    def test_add_product_to_cart(self):
        self.productpage = ProductPage(self.driver, self.URL)
        self.productpage.select_color("Red")
        self.productpage.select_orientation("Landscape")
        self.productpage.enter_profile_description("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus")
        self.productpage.click_need_phone_checkbox()
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        self.productpage.enter_phone_number("9876543210")
        self.productpage.select_additional_elements("logo")
        self.productpage.select_additional_elements("border")
        self.productpage.do_upload_file(TestData.FILE_UPLOAD)
        self.productpage.click_add_to_cart_button()
        self.productpage.click_view_cart_link()
        self.cartpage = CartPage(self.driver)
        assert self.cartpage.is_product_in_cart_displayed(), "Product is not available in cart"
        time.sleep(1)

    # @pytest.mark.order("first")
    def test_required_fields_validation(self):
        self.productpage = ProductPage(self.driver, self.URL)
        self.productpage.select_color("Red")
        self.productpage.select_orientation("Landscape")
        self.productpage.click_add_to_cart_button()
        assert self.productpage.is_error_message_displayed() == "Please fill out this field.", "Error not displayed"
        time.sleep(1)

    def test_minimum_selection_multi_select_field(self):
        self.productpage = ProductPage(self.driver, self.URL)
        self.productpage.select_color("Red")
        self.productpage.select_orientation("Landscape")
        self.productpage.enter_profile_description("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus")
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        self.productpage.select_additional_elements("border")
        self.productpage.click_add_to_cart_button()
        assert self.productpage.is_minimum_selection_error_displayed(), "Exception for minimum selection in multiselect field not displayed"
        time.sleep(1)
