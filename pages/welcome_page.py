from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from pages.base_page import BasePage, Locator


class WelcomePage(BasePage):
    __logout_link: Locator = Locator(By.XPATH, '//a[text()="logout"]')

    def __init__(self, driver: WebDriver):
        self.driver = driver
        super().__init__(driver)

    def is_logout_visible(self) -> bool:
        return self._is_element_visible(WelcomePage.__logout_link)


__welcome_instance: WelcomePage = None


def init_welcome(driver: WebDriver):
    global __welcome_instance
    __welcome_instance = WelcomePage(driver)


def welcome():
    return __welcome_instance
