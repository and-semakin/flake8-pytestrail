from pytest_testrail.plugin import pytestrail, testrail


@pytestrail.case()
def test_with_empty_pytestrail_decorator() -> None:
    assert True


@testrail()
def test_with_empty_testrail_decorator() -> None:
    assert True


@pytestrail.case(123)
def test_with_int_pytestrail_decorator() -> None:
    assert True


@testrail(123)
def test_with_int_testrail_decorator() -> None:
    assert True


@pytestrail.case("")
def test_with_empty_str_pytestrail_decorator() -> None:
    assert True


@testrail("")
def test_with_empty_str_testrail_decorator() -> None:
    assert True


@pytestrail.case("123")
def test_with_numeric_str_pytestrail_decorator() -> None:
    assert True


@testrail("123")
def test_with_numeric_str_testrail_decorator() -> None:
    assert True


@pytestrail.case("C123", "")
def test_with_two_str_pytestrail_decorator() -> None:
    assert True


@testrail("C123", "")
def test_with_two_str_testrail_decorator() -> None:
    assert True
