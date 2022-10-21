"""Module that implements utils methods to the plugin."""

from typing import Iterable, Tuple

from poetry.core.version.requirements import Requirement


def parse_requirements(file_path: str) -> Iterable[Tuple[str, str]]:
    """Parse the requirements.txt and extact all package."""
    with open(file_path, encoding="utf-8") as reader:
        lines = reader.read()
        for line in lines.split("\n"):
            if line and not line.startswith("#") and not line.startswith("git"):
                requirement = Requirement(line)
                yield requirement.name, requirement.pretty_constraint
