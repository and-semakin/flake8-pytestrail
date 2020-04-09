from pytest_testrail.plugin import pytestrail


@pytestrail.case("C1")
def test_with_pytestrail_decorator() -> None:
    assert True


class TestTR001:
    @pytestrail.case("C1")
    def test_method_with_pytestrail_decorator(self) -> None:
        assert True
