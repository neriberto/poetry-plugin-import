import shutil
import subprocess
from pathlib import Path
from subprocess import CompletedProcess
from typing import List

testing_assets = Path(__file__).parent / "assets"
plugin_source_dir = Path(__file__).parent.parent / "poetry_plugin_import"


def copy_assets(source_name: str, testing_dir: Path) -> None:
    package_path = testing_assets / source_name
    shutil.copytree(package_path, testing_dir)


def run_audit(testing_dir: Path, args: List[str] = []) -> CompletedProcess:
    result = subprocess.run(
        [
            "poetry",
            "import",
        ]
        + args,
        cwd=testing_dir,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        encoding="utf-8",
    )
    return result


def test_case_one(tmp_path: Path) -> None:
    testing_dir = tmp_path / "testing_package"
    copy_assets("test_one", testing_dir)
    result = run_audit(testing_dir=testing_dir)

    assert "poetry import requirements.txt" in result.stdout
    assert "project saved with 9 new dependencies" in result.stdout
    assert result.returncode == 0


def test_case_two(tmp_path: Path) -> None:
    testing_dir = tmp_path / "testing_package"
    copy_assets("test_two", testing_dir)
    result = run_audit(testing_dir=testing_dir)

    assert "poetry import requirements.txt" in result.stdout
    assert "The default requirements.txt does not exists in" in result.stdout
    assert result.returncode != 0
