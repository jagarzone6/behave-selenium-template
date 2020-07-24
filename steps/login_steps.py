from behave import use_step_matcher, when, then, given
from support.test_context import TestContext

use_step_matcher('re')


@given('I access my Demo App')
def open_app(context: TestContext):
    context.app.go_to("http://127.0.0.1:7272")


@when('I "(.*)" log in with password "(.*)"')
def login(context: TestContext, user_name, password):
    context.app.login_page.set_username(user_name)
    context.app.login_page.set_password(password)
    context.app.login_page.click_login()


@then('welcome page should display')
def step_impl_3(context: TestContext):
    assert context.app.login_page.is_logout_visible() is True


@then('error page should display')
def error_diplayed(context: TestContext):
    assert context.app.login_page.is_error_visible() is True
