from behave.runner import Context
from selenium.webdriver.remote.webdriver import WebDriver
from pages.login_page import LoginPage
from support.driver import get_driver


class TestContext(Context):

    def __init__(self, context: Context):
        self._runner = context._runner
        self._config = context._runner.config
        self._root = context._root
        self._stack = context._stack
        self._record = context._record
        self._origin = context._origin
        self._mode = context._mode
        self.feature = context.feature
        # -- RECHECK: If needed
        self.text = context.text
        self.table = context.table
        self.stdout_capture = context.stdout_capture
        self.stderr_capture = context.stderr_capture
        self.log_capture = context.log_capture
        self.fail_on_cleanup_errors = context.fail_on_cleanup_errors
        self.app: App = App(get_driver())


class App:

    def __init__(self, driver: WebDriver):
        self.login_page = LoginPage(driver)
        self.driver = driver

    def go_to(self, url: str):
        self.driver.get(url)
