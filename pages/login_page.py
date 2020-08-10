from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from pages.base_page import BasePage, Locator


class LoginPage(BasePage):
    __username_field: Locator = Locator(By.ID, 'username_field')
    __password_field: Locator = Locator(By.ID, 'password_field')
    __login_button: Locator = Locator(By.ID, 'login_button')
    __error_header: Locator = Locator(By.XPATH, '//h1[text()="Error Page"]')

    def __init__(self, driver: WebDriver):
        self.driver = driver
        super().__init__(driver)

    def set_username(self, username: str):
        self._send_keys(LoginPage.__username_field, username)

    def set_password(self, password: str):
        self._send_keys(LoginPage.__password_field, password)

    def click_login(self):
        self._click(LoginPage.__login_button)

    def is_error_visible(self) -> bool:
        return self._is_element_visible(LoginPage.__error_header)
