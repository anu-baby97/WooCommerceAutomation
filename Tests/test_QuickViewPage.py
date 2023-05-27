import time

import pytest

from Config.config import TestData
from Pages.CartPage import CartPage
from Pages.QuickViewPage import QuickViewPage
from Pages.ProductPage import ProductPage


@pytest.mark.usefixtures("init_driver")
@pytest.mark.order("third")
class TestProductListPage:

    def test_product_quickview_add_cart(self):
        self.productpage = ProductPage(self.driver, "https://woocommerce-850415-2933260.cloudwaysapps.com/shop")
        self.productlistpage = QuickViewPage(self.driver)
        self.productlistpage.click_quick_view_link()
        time.sleep(3)
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
        time.sleep(2)
