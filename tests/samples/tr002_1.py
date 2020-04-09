from pytest_testrail.plugin import pytestrail


@pytestrail.case("C1")
@pytestrail.case("C1")
def test_with_multiple_pytestrail_decorator() -> None:
    assert True
