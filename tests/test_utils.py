"""A module to test the methods from utils."""

import os
from pathlib import Path

from poetry_plugin_import.utils import parse_requirements

testing_assets = Path(__file__).parent / "assets" / "test_one"
plugin_source_dir = Path(__file__).parent.parent / "poetry_plugin_import"


def test_parse_requirements() -> None:
    """Test the method parse_requirements."""
    req_txt = os.path.join(testing_assets, 'requirements.txt')
    for item in parse_requirements(req_txt):
        assert isinstance(item, tuple)
