from behave import use_step_matcher, when, then, given
from support.test_context import TestContext
from support.driver import go_to

use_step_matcher('re')


@given('I access my Demo App')
def open_app(context: TestContext):
    go_to("http://127.0.0.1:7272")
