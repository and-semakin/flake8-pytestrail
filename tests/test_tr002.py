import pytest

from flake8_pytestrail import PyTestRailChecker

sample_name = "tr002_3.py"


class TestTR002:
    @pytest.mark.parametrize(
        "checker",
        ["tr002_1.py", "tr002_2.py", "tr002_3.py"],
        ids=["pytestrail", "testrail", "mixed"],
        indirect=["checker"],
    )
    def test_it_checks_file_for_tr002(self, checker: PyTestRailChecker) -> None:
        r = checker.run()
        errors = list(r)
        assert len(errors) == 1
        assert all(e[2].startswith("TR002") for e in errors)
