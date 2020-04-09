from flake8_pytestrail import PyTestRailChecker

sample_name = "tr001.py"


class TestTR001:
    def test_it_checks_file_for_tr001(self, checker: PyTestRailChecker) -> None:
        r = checker.run()
        errors = list(r)
        assert len(errors) == 2
        assert all(e[2].startswith("TR001") for e in errors)
        assert errors[0][0] == 6
        assert errors[1][0] == 28
