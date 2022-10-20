from typing import Iterable, Tuple

from poetry.core.version.requirements import Requirement


def parse_requirements(file_path: str) -> Iterable[Tuple]:
    print(file_path)
    with open(file_path) as reader:
        lines = reader.read()
        for line in lines.split('\n'):
            if line and not line.startswith("#") and not line.startswith("git"):
                requirement = Requirement(line)
                yield requirement.name, requirement.pretty_constraint
