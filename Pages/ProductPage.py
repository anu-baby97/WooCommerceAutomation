import time

from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage


class ProductPage(BasePage):
    # web elements
    color_dropdown = (By.ID, "color")
    orientation_dropdown = (By.ID, "orientation")
    profile_description = (By.ID, "profile_description")
    need_phone_checkbox = (By.ID, "need_phone")
    phone_number = (By.ID, "phone_number")
    additional_elements = (By.NAME, "additional_elements[]")
    upload_file = (By.XPATH, "//input[@type='file']")
    add_to_cart_button = (By.XPATH, "//button[text()='Add to cart']")
    view_cart_link = (By.XPATH, "//a[text()='View cart']")
    product_in_cart = (By.XPATH, "//a[contains(text(),'RF ID Card')]")
    minimum_selection_error_message = (By.XPATH, "//ul[@class='woocommerce-error']/li/strong")

    # constructor
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get("https://woocommerce-850415-2933260.cloudwaysapps.com/product/rf-id-card")

    # page actions

    def select_color(self,color):
        self.select_element_from_dropdown(self.color_dropdown, color)

    def select_orientation(self, orientation):
        self.select_element_from_dropdown(self.orientation_dropdown, orientation)

    def enter_profile_description(self,profile_desc):
        self.do_sendkeys(self.profile_description, profile_desc)

    def click_need_phone_checkbox(self):
        self.do_click(self.need_phone_checkbox)

    def enter_phone_number(self,phno):
        self.do_sendkeys(self.phone_number, phno)
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(1)

    def select_additional_elements(self, element):
        self.select_element_from_dropdown(self.additional_elements, element)

    def do_upload_file(self, file):
        self.do_sendkeys(self.upload_file, file)

    def click_add_to_cart_button(self):
        self.do_click(self.add_to_cart_button)

    def click_view_cart_link(self):
        self.do_click(self.view_cart_link)

    def is_product_in_cart_displayed(self):
        return self.is_element_displayed(self.product_in_cart)

    def is_error_message_displayed(self):
        return self.validation_message_displayed(self.profile_description)

    def is_minimum_selection_error_displayed(self):
        return  self.is_element_displayed(self.minimum_selection_error_message)