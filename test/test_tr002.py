from flake8_pytestrail import PyTestRailChecker

sample_name = "tr002.py"


class TestTR002:
    def test_it_checks_file_for_tr002(self, checker: PyTestRailChecker) -> None:
        r = checker.run()
        errors = list(r)
        assert len(errors) == 3
        assert all(e[2].startswith("TR002") for e in errors)
        assert errors[0][0] == 6
        assert errors[1][0] == 12
        assert errors[2][0] == 18
