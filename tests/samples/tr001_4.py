import pytest

from pytest_testrail.plugin import pytestrail


@pytestrail.case("C1")
@pytest.mark.parametrize()
@pytest.mark.skip()
def test_with_pytestrail_decorator_with_another_decorators() -> None:
    assert True


class TestTR001:
    @pytestrail.case("C1")
    @pytest.mark.parametrize()
    @pytest.mark.skip()
    def test_method_with_pytestrail_decorator_with_another_decorators(self) -> None:
        assert True
