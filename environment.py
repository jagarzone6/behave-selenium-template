from behave.runner import Context
from support.driver import quit_driver
from support.test_context import TestContext


def before_all(context: Context):
    print("before_all activated")
    context = TestContext(context)


def after_all(context: TestContext):
    print("after_all activated")
    quit_driver()


def before_scenario(context: TestContext, scenario):
    print("before_scenario activated")


def after_scenario(context: TestContext, step):
    print("after_scenario activated")
