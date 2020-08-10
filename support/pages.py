from selenium.webdriver.remote.webdriver import WebDriver
from pages.login_page import LoginPage
from pages.welcome_page import WelcomePage

login:LoginPage = None
welcome:WelcomePage = None

def with_driver(driver: WebDriver):
    global login, welcome
    login = LoginPage(driver)
    welcome = WelcomePage(driver)
