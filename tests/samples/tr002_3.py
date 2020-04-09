from pytest_testrail.plugin import pytestrail, testrail


@testrail("C1")
@pytestrail.case("C1")
def test_with_testrail_and_pytestrail_decorators() -> None:
    assert True
