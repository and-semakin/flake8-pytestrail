from pytest_testrail.plugin import pytestrail, testrail


@pytestrail.case("C123", "")
def test_with_two_str_pytestrail_decorator() -> None:
    assert True


@testrail("C123", "")
def test_with_two_str_testrail_decorator() -> None:
    assert True
