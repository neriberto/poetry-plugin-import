"""Module that implements the Command to the plugin."""

import os
from typing import Any, Dict, Optional

from poetry.console.application import Application
from poetry.console.commands.command import Command
from poetry.plugins.application_plugin import ApplicationPlugin

from poetry_plugin_import.utils import parse_requirements


class CustomCommand(Command):
    """Implements a Command to the plugin."""

    name = "import"

    def handle(self) -> int:
        """Implement the handle method from Command."""
        self.line("<b># poetry import requirements.txt</b>")

        current_dir = os.path.realpath(os.getcwd())
        file_path = os.path.join(current_dir, "requirements.txt")
        if not os.path.exists(file_path):
            self.line(f"The default requirements.txt does not exists in {current_dir}")
            return -1

        pyproject_config = self.poetry.pyproject.data
        config: Optional[Dict[str, Any]] = pyproject_config.get("tool", {}).get(
            "poetry"
        )
        if not config:
            self.line("Failure to get dependencies")
            return -1

        dependencies: Optional[Dict[str, Any]] = config.get("dependencies")
        if not dependencies:
            self.line("Failure to get dependencies")
            return -1

        counter = 0
        for name, pretty_constraint in parse_requirements(file_path):
            dependencies.update({name: pretty_constraint})
            counter += 1

        self.poetry.pyproject.save()
        self.line(f"<b># project saved with {counter} new dependencies</b>")

        return 0


def factory() -> CustomCommand:
    """A factory method to the CustomCommand."""
    return CustomCommand()


class ImportApplicationPlugin(ApplicationPlugin):
    """Implements the ApplicationPlugin."""

    def activate(self, application: Application) -> None:
        """Implement the activate method from ApplicationPlugin."""
        application.command_loader.register_factory("import", factory)
