from behave import use_step_matcher, when, then, given
from support.test_context import TestContext
import support.pages as pages

use_step_matcher('re')


@when('I log in with user "(.*)" and password "(.*)"')
def login_step(context: TestContext, user_name, password):
    pages.login.set_username(user_name)
    pages.login.set_password(password)
    pages.login.click_login()


@then('welcome page should display')
def step_impl_3(context: TestContext):
    assert pages.welcome.is_logout_visible() is True
    context.scenario_data.login_succeeded = 1


@then('error page should display')
def error_diplayed(context: TestContext):
    assert pages.login.is_error_visible() is True
    context.scenario_data.login_succeeded = 0
