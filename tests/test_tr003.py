import pytest

from flake8_pytestrail import PyTestRailChecker

sample_name = "tr003_1.py"


class TestTR003:
    @pytest.mark.parametrize(
        "checker",
        ["tr003_1.py", "tr003_2.py", "tr003_3.py", "tr003_4.py", "tr003_5.py"],
        ids=[
            "empty_decorator",
            "int_decorator",
            "empty_str_decorator",
            "numeric_str_decorator",
            "one_case_id_is_broken",
        ],
        indirect=["checker"],
    )
    def test_it_checks_file_for_tr003(self, checker: PyTestRailChecker) -> None:
        r = checker.run()
        errors = list(r)
        assert len(errors) == 2
        assert all(e[2].startswith("TR003") for e in errors)
