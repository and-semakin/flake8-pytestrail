from pytest_testrail.plugin import pytestrail, testrail


@pytestrail.case("C1")
@pytestrail.case("C1")
def test_with_multiple_pytestrail_decorator() -> None:
    assert True


@testrail("C1")
@testrail("C1")
def test_with_multiple_testrail_decorator() -> None:
    assert True


@testrail("C1")
@pytestrail.case("C1")
def test_with_testrail_and_pytestrail_decorators() -> None:
    assert True
