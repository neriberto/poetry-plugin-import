import os
import re
from typing import Optional, Dict, Any

from poetry.console.commands.command import Command
from poetry.plugins.application_plugin import ApplicationPlugin


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

        with open(file_path) as reader:
            lines = reader.read()
            regex = r"(.[^=~<>]+)([=~<>]+)(.*)"
            matches = re.finditer(regex, lines, re.MULTILINE)
            for _, match in enumerate(matches, start=1):
                library = match.group(1)
                condition = match.group(2)
                version = match.group(3)

                if condition != '==':
                    version = f'{condition}{version}'

                dependencies.update({library: version})

        self.poetry.pyproject.save()

        return 0


def factory():
    return CustomCommand()


class ImportApplicationPlugin(ApplicationPlugin):
    def activate(self, application):
        application.command_loader.register_factory("import", factory)
