import pytest

from flake8_pytestrail import PyTestRailChecker

sample_name = "tr001_1.py"


class TestTR001:
    @pytest.mark.parametrize("checker", ["tr001_1.py"], indirect=["checker"])
    def test_it_finds_tr001_errors(self, checker: PyTestRailChecker) -> None:
        r = checker.run()
        errors = list(r)
        assert len(errors) == 2
        assert all(e[2].startswith("TR001") for e in errors)

    @pytest.mark.parametrize(
        "checker",
        ["tr001_2.py", "tr001_3.py", "tr001_4.py"],
        ids=["pytestrail", "testrail", "other_decorators_dont_affect"],
        indirect=["checker"],
    )
    def test_it_works_with_valid_files(self, checker: PyTestRailChecker) -> None:
        r = checker.run()
        errors = list(r)
        assert not errors
