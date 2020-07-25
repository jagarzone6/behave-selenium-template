from selenium.webdriver.remote.webdriver import WebDriver
from pages.login_page import init_login, login
from pages.welcome_page import init_welcome, welcome


def with_driver(driver: WebDriver):
    init_login(driver)
    init_welcome(driver)
