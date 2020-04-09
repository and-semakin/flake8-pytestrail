from pytest_testrail.plugin import pytestrail, testrail


@pytestrail.case()
def test_with_empty_pytestrail_decorator() -> None:
    assert True


@testrail()
def test_with_empty_testrail_decorator() -> None:
    assert True
