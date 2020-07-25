from behave.runner import Context
from support.driver import Driver
from support.test_context import TestContext
from selenium.webdriver.remote.webdriver import WebDriver
from support.driver import Driver
from pages import with_driver


def before_all(context: Context):
    print("before_all activated")
    context = TestContext(context)
    with_driver(Driver.get_driver())


def after_all(context: TestContext):
    print("after_all activated")
    Driver.quit_driver()


def before_scenario(context: TestContext, scenario):
    print("before_scenario activated")


def after_scenario(context: TestContext, step):
    print("after_scenario activated")
