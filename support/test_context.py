from behave.runner import Context
from dataclasses import dataclass


@dataclass
class ScenarioData:
    example_var: str = None
    login_succeeded: bool = None


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
        self.scenario_data: ScenarioData = ScenarioData()
