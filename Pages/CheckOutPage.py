from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage


class CheckOutPage(BasePage):
    # web elements
    billing_first_name = (By.ID, "billing_first_name")
    billing_last_name = (By.ID, "billing_last_name")
    billing_country = (By.ID, "billing_country")
    billing_address_1 = (By.ID, "billing_address_1")
    billing_city = (By.ID, "billing_city")
    billing_state = (By.ID, "billing_state")
    billing_postcode = (By.ID, "billing_postcode")
    billing_phone = (By.ID, "billing_phone")
    billing_email = (By.ID, "billing_email")
    need_delivery_yes = (By.ID, "need_delivery_yes")
    delivery_fee = (By.XPATH, "//tr[@class='fee']")
    delivery_date_field = (By.ID, "delivery_date")
    delivery_date_select = (By.XPATH, "//a[text()='27']")
    delivery_time_field = (By.ID, "delivery_time")
    delivery_time = (By.XPATH, "//ul[@class='ui-timepicker-list']//li[2]")
    delivery_addons_packing = (By.ID, "delivery_addons_packing")
    delivery_addons_wooden_box = (By.ID, "delivery_addons_wooden_box")
    payment_method_cod = (By.XPATH, "//label[contains(text(),'Cash on delivery')]")
    place_order = (By.ID, "place_order")
    order_placed_success_message = (
        By.XPATH, "//p[@class='woocommerce-notice woocommerce-notice--success woocommerce-thankyou-order-received']")

    # constructor
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get("https://woocommerce-850415-2933260.cloudwaysapps.com/checkout")

    # page actions

    def enter_billing_first_name(self, fname):
        self.do_sendkeys(self.billing_first_name, fname)

    def enter_billing_last_name(self, lname):
        self.do_sendkeys(self.billing_last_name, lname)

    def select_billing_country(self, country):
        self.select_element_from_dropdown_by_visible_text(self.billing_country, country)

    def enter_billing_address_1(self, address):
        self.do_sendkeys(self.billing_address_1, address)

    def enter_billing_city(self, city):
        self.do_sendkeys(self.billing_city, city)

    def select_billing_state(self, state):
        self.select_element_from_dropdown_by_visible_text(self.billing_state, state)

    def enter_billing_postcode(self, postcode):
        self.do_sendkeys(self.billing_postcode, postcode)

    def enter_billing_phone(self, phno):
        self.do_sendkeys(self.billing_phone, phno)

    def enter_billing_email(self, email):
        self.do_sendkeys(self.billing_email, email)

    def select_need_delivery_yes(self):
        self.do_click(self.need_delivery_yes)

    def check_delivery_price(self):
        return self.is_element_displayed(self.delivery_fee)

    def select_delivery_date(self):
        self.do_click(self.delivery_date_field)
        self.do_click(self.delivery_date_select)

    def select_delivery_time(self):
        self.do_click(self.delivery_time_field)
        self.do_click(self.delivery_time)

    def select_delivery_addons_packing(self):
        self.do_click(self.delivery_addons_packing)

    def select_delivery_addons_wooden_box(self):
        self.do_click(self.delivery_addons_wooden_box)

    def select_payment_method_cod(self):
        self.do_click(self.payment_method_cod)

    def select_place_order(self):
        self.do_click(self.place_order)

    def is_order_success_message_displayed(self):
        return self.is_element_displayed(self.order_placed_success_message)
