import pytest

from pytest_testrail.plugin import pytestrail, testrail


def test_without_pytestrail_decorator() -> None:
    assert True


@pytestrail.case("C1")
def test_with_pytestrail_decorator() -> None:
    assert True


@testrail("C1")
def test_with_testrail_decorator() -> None:
    assert True


@pytestrail.case("C1")
@pytest.mark.parametrize()
@pytest.mark.skip()
def test_with_pytestrail_decorator_with_another_decorators() -> None:
    assert True


class TestTR001:
    def test_method_without_pytestrail_decorator(self) -> None:
        assert True

    @pytestrail.case("C1")
    def test_method_with_pytestrail_decorator(self) -> None:
        assert True

    @testrail("C1")
    def test_method_with_testrail_decorator(self) -> None:
        assert True

    @pytestrail.case("C1")
    @pytest.mark.parametrize()
    @pytest.mark.skip()
    def test_method_with_pytestrail_decorator_with_another_decorators(self) -> None:
        assert True
