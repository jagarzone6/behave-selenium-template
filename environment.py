from behave.runner import Context
from support.driver import Driver
from support.test_context import TestContext, ScenarioData
from selenium.webdriver.remote.webdriver import WebDriver
from support.driver import Driver
import pages


def before_all(context: Context):
    print("before_all activated")
    context = TestContext(context)
    pages.with_driver(Driver.get_driver())


def after_all(context: TestContext):
    print("after_all activated")
    Driver.quit_driver()


def before_scenario(context: TestContext, scenario):
    print("before_scenario activated")
    context.scenario_data = ScenarioData()
    print(str(context.scenario_data))


def after_scenario(context: TestContext, step):
    print("after_scenario activated")
    print(str(context.scenario_data))
