from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from support.driver import Locator


class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def _send_keys(self, locator: Locator, keys: str):
        elem = self.driver.find_element(locator.by, locator.locator)
        elem.clear()
        elem.send_keys(keys)

    def _click(self, locator: Locator):
        elem = self.driver.find_element(locator.by, locator.locator)
        elem.click()

    def _is_element_visible(self, locator: Locator):
        elem = self.driver.find_element(locator.by, locator.locator)
        return elem.is_displayed()
