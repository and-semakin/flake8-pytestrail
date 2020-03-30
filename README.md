# flake8-pytestrail

A companion Flake8 plugin for [pytest-testrail](https://github.com/allankp/pytest-testrail) package.

## Installation

```
pip install flake8-pytestrail
```

or if you use [poetry](https://python-poetry.org/):

```
poetry add --dev flake8-pytestrail
```

## Usage

> ⚠️ At the moment plugin assumes that you use
> default `pytest` configuration (test files
> are all can be matched by `**/test_*.py` glob).
> It also assumes that you want all test cases to have
> been registered inside of TestRail and have ID.

```
flake8 .
```

## Error list

* TR001 Missing `@pytestrail.case()` decorator
* TR002 Multiple `@pytestrail.case()` decorators
* TR003 Test case ID should match `"^C\d+$"` pattern

## Configuration

There is no way to configure the plugin at the moment.
