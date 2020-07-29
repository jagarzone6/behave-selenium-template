from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


class Driver:
    driver: WebDriver = None

    @staticmethod
    def get_driver():
        if Driver.driver is None:
            Driver.driver = webdriver.Remote(
                command_executor='http://127.0.0.1:4444/wd/hub',
                desired_capabilities=DesiredCapabilities.CHROME)
        return Driver.driver

    @staticmethod
    def quit_driver():
        Driver.driver.quit()


def go_to(url: str):
    Driver.driver.get(url)
