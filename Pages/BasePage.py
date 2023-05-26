import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

"""This class is the parent of all pages"""
"""It contains all generic methods and utilities for all pages"""


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def do_click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def do_sendkeys(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_element_text(self, by_locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).text

    def select_element_from_dropdown(self, by_locator_dropdown, valueSelect):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by_locator_dropdown))
        select = Select(element)
        # self.driver.implicitly_wait(3)
        select.select_by_value(valueSelect)

    def is_element_displayed(self, by_locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))

        # return self.driver.find_element(*by_locator).is_displayed()

    def validation_message_displayed(self, by_locator):
        text= self.driver.find_element(*by_locator).get_attribute("validationMessage")
        return text