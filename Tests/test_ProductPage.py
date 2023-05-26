import time

import pytest

from Config.config import TestData
from Pages.ProductPage import ProductPage


@pytest.mark.usefixtures("init_driver")
class TestLoginPage:

    # def test_product_page_fields(self):
    #     self.productpage = ProductPage(self.driver)
    #     self.productpage.select_color()
    #     self.productpage.select_orientation()
    #     self.productpage.enter_profile_description()
    #     self.productpage.click_need_phone_checkbox()
    #     self.productpage.enter_phone_number()
    #     self.productpage.select_additional_elements()
    #     self.productpage.do_upload_file(TestData.FILE_UPLOAD)
    #     self.productpage.click_add_to_cart_button()
    #     self.productpage.click_view_cart_link()
    #     assert self.productpage.is_product_in_cart_displayed(), "Product is not available in cart"
    #     time.sleep(2)

    def test_required_fields_validation(self):
        self.productpage = ProductPage(self.driver)
        self.productpage.select_color()
        self.productpage.select_orientation()
        self.productpage.click_add_to_cart_button()
        assert self.productpage.is_error_message_displayed() == "Please fill out this field.", "Error not displayed"
