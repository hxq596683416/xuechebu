"""
po基类
"""
from selenium.webdriver.support.wait import WebDriverWait


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    def find_element_func(self, location, timeout=10, poll=1):
        element = WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(*location))
        return element

    def click_func(self, location):
        self.find_element_func(location).click()

    def input_func(self, location, text):
        element = self.find_element_func(location)
        element.clear()
        element.send_keys(text)
