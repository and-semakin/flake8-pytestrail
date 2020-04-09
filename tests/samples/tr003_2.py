from pytest_testrail.plugin import pytestrail, testrail


@pytestrail.case(123)
def test_with_int_pytestrail_decorator() -> None:
    assert True


@testrail(123)
def test_with_int_testrail_decorator() -> None:
    assert True
