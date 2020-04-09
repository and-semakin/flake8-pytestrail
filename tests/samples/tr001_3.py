from pytest_testrail.plugin import testrail


@testrail("C1")
def test_with_testrail_decorator() -> None:
    assert True


class TestTR001:
    @testrail("C1")
    def test_method_with_testrail_decorator(self) -> None:
        assert True
