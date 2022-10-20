import os
from typing import Optional, Dict, Any

from poetry.console.commands.command import Command
from poetry.plugins.application_plugin import ApplicationPlugin

from poetry_plugin_import.utils import parse_requirements


class CustomCommand(Command):
    name = "import"

    def handle(self) -> int:
        current_dir = os.path.realpath(os.getcwd())
        file_path = os.path.join(current_dir, 'requirements.txt')
        if not os.path.exists(file_path):
            self.line(f'The default requirements.txt does not exists in {current_dir}')
            return -1

        pyproject_config = self.poetry.pyproject.data
        config: Optional[Dict[str, Any]] = pyproject_config.get("tool", dict()).get("poetry")
        dependencies = config.get('dependencies')

        for name, pretty_constraint in parse_requirements(file_path):
            dependencies.update({name: pretty_constraint})

        self.poetry.pyproject.save()

        return 0


def factory():
    return CustomCommand()


class ImportApplicationPlugin(ApplicationPlugin):
    def activate(self, application):
        application.command_loader.register_factory("import", factory)
