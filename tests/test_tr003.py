from flake8_pytestrail import PyTestRailChecker

sample_name = "tr003.py"


class TestTR003:
    def test_it_checks_file_for_tr003(self, checker: PyTestRailChecker) -> None:
        r = checker.run()
        errors = list(r)
        assert len(errors) == 10
        assert all(e[2].startswith("TR003") for e in errors)
        assert errors[0][0] == 5
        assert errors[1][0] == 10
        assert errors[2][0] == 15
        assert errors[3][0] == 20
        assert errors[4][0] == 25
        assert errors[5][0] == 30
        assert errors[6][0] == 35
        assert errors[7][0] == 40
        assert errors[8][0] == 45
        assert errors[9][0] == 50
