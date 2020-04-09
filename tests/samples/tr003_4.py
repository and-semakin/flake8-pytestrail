from pytest_testrail.plugin import pytestrail, testrail


@pytestrail.case("123")
def test_with_numeric_str_pytestrail_decorator() -> None:
    assert True


@testrail("123")
def test_with_numeric_str_testrail_decorator() -> None:
    assert True
