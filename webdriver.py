import os
from selenium import webdriver
from selenium.webdriver.common.by import By


class WebDriverBase:
    driver = None

    def init_driver(self):
        self.driver = webdriver.Chrome(executable_path=os.getcwd() + "/chromedriver")
        return self.driver

    def get_element(self, locator):
        return self.driver.find_element(*locator)
