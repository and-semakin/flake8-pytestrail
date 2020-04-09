import tempfile
from pathlib import Path
from typing import Iterator

import pytest

from flake8_pytestrail import PyTestRailChecker


@pytest.fixture(scope="module")
def checker(request) -> Iterator[PyTestRailChecker]:
    with tempfile.TemporaryDirectory() as d:
        sample_name = request.module.sample_name
        source_file = Path("tests/samples") / sample_name
        test_file = Path(d) / f"test_{sample_name}"

        with source_file.open("r") as src:
            with test_file.open("w") as dst:
                dst.write(src.read())

        c = PyTestRailChecker(filename=str(test_file))
        yield c
