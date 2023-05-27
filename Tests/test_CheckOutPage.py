import time

import pytest

from Pages.CartPage import CartPage
from Pages.CheckOutPage import CheckOutPage
from Pages.ProductPage import ProductPage


@pytest.mark.usefixtures("init_driver")
class TestCheckOutPage:

    def test_checkout_page_fields(self):
        self.productpage = ProductPage(self.driver, "https://woocommerce-850415-2933260.cloudwaysapps.com/product/cap")
        time.sleep(2)
        self.productpage.click_add_to_cart_button()
        self.productpage.click_view_cart_link()
        self.cartpage = CartPage(self.driver)
        self.cartpage.click_proceed_to_checkout_link()
        time.sleep(2)
        self.checkoutpage = CheckOutPage(self.driver)
        self.checkoutpage.enter_billing_first_name("Anu")
        self.checkoutpage.enter_billing_last_name("Baby")
        self.checkoutpage.select_billing_country("India")
        self.checkoutpage.enter_billing_address_1("123 abc")
        self.checkoutpage.enter_billing_city("Calicut")
        self.checkoutpage.select_billing_state("Kerala")
        self.checkoutpage.enter_billing_postcode("673016")
        self.checkoutpage.enter_billing_phone("9876543210")
        self.checkoutpage.enter_billing_email("anu@gmail.com")
        self.checkoutpage.select_need_delivery_yes()
        assert self.checkoutpage.check_delivery_price(), "Delivery fee is not added"
        self.checkoutpage.select_delivery_date()
        self.driver.execute_script("window.scrollTo(0,1500)")
        self.checkoutpage.select_delivery_time()
        self.checkoutpage.select_delivery_addons_packing()
        self.checkoutpage.select_delivery_addons_wooden_box()
        self.driver.execute_script("window.scrollTo(0,1300)")
        time.sleep(2)
        self.checkoutpage.select_payment_method_cod()
        self.checkoutpage.select_place_order()
        assert self.checkoutpage.is_order_success_message_displayed(), "Order is not successfully placed"
        time.sleep(2)
