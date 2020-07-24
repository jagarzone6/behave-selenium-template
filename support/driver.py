from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


def get_driver():
    if _Driver.driver is None:
        _Driver.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME)
    return _Driver.driver


def quit_driver():
    _Driver.driver.quit()


class _Driver:
    driver: WebDriver = None


class Locator:
    def __init__(self, by: By, locator: str):
        self.by: By = by
        self.locator: str = locator
