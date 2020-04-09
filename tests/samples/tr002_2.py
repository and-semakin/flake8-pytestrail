from pytest_testrail.plugin import testrail


@testrail("C1")
@testrail("C1")
def test_with_multiple_testrail_decorator() -> None:
    assert True
