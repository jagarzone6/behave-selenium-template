from behave import use_step_matcher, when, then, given
from support.test_context import TestContext
from pages import login, welcome

use_step_matcher('re')


@when('I log in with user "(.*)" and password "(.*)"')
def login_step(context: TestContext, user_name, password):
    login().set_username(user_name)
    login().set_password(password)
    login().click_login()


@then('welcome page should display')
def step_impl_3(context: TestContext):
    assert welcome().is_logout_visible() is True


@then('error page should display')
def error_diplayed(context: TestContext):
    assert login().is_error_visible() is True
