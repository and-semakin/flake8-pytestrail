import ast
import re
from functools import partial
from typing import Any, Iterable, Iterator, NamedTuple, Tuple, cast

import attr
import pycodestyle

TEST_FILE_PATTERN = "test_[A-z0-9_]*.py$"
TEST_FUNCTION_PATTERN = "test_"
TEST_CASE_PATTERN = r"^C\d+$"
EXPECTED_DECORATORS = {"pytestrail.case", "testrail"}


__version__ = "0.2.1"


Flake8Error = Tuple[int, int, str, Any]


@attr.s(hash=False)
class PyTestRailChecker:
    name = "flake8-pytestrail"
    version = __version__

    tree = attr.ib(default=None)
    filename = attr.ib(default="(none)")
    lines = attr.ib(default=None)
    visitor = attr.ib(init=False, default=attr.Factory(lambda: PyTestRailVisitor))

    def run(self) -> Iterator[Flake8Error]:
        if not re.search(TEST_FILE_PATTERN, self.filename):
            return

        if not (self.tree and self.lines):
            self.load_file()
        visitor = self.visitor(filename=self.filename, lines=self.lines)
        visitor.visit(self.tree)
        for e in visitor.errors:
            if pycodestyle.noqa(self.lines[e.lineno - 1]):
                continue

            yield self.adapt_error(e)

    @classmethod
    def adapt_error(cls, e: "ExtendedError") -> Flake8Error:
        """Adapts the extended error namedtuple to be compatible with Flake8."""
        return e._replace(message=e.message.format(*e.vars))[:4]

    def load_file(self) -> None:
        """Loads the file in a way that auto-detects source encoding and deals
        with broken terminal encodings for stdin.

        Stolen from flake8_import_order because it's good.
        """

        if self.filename in ("stdin", "-", None):
            self.filename = "stdin"
            self.lines = pycodestyle.stdin_get_value().splitlines(True)
        else:
            self.lines = pycodestyle.readlines(self.filename)

        if not self.tree:
            self.tree = ast.parse("".join(self.lines))


def _to_name_str(node: ast.AST) -> str:
    # Turn Name and Attribute nodes to strings, e.g "ValueError" or
    # "pkg.mod.error", handling any depth of attribute accesses.
    if isinstance(node, ast.Name):
        return node.id
    assert isinstance(node, ast.Attribute)
    return _to_name_str(node.value) + "." + node.attr


@attr.s
class PyTestRailVisitor(ast.NodeVisitor):
    filename = attr.ib()
    lines = attr.ib()
    node_stack = attr.ib(default=attr.Factory(list))
    node_window = attr.ib(default=attr.Factory(list))
    errors = attr.ib(default=attr.Factory(list))
    futures = attr.ib(default=attr.Factory(set))

    def visit_FunctionDef(self, node: ast.FunctionDef) -> None:
        # if function is not a test, skip it
        if re.match(TEST_FUNCTION_PATTERN, node.name):
            pytestrail_decorators = [
                dec
                for dec in cast(Iterable[ast.Call], node.decorator_list)
                if _to_name_str(dec.func) in EXPECTED_DECORATORS
            ]
            if not pytestrail_decorators:
                self.errors.append(TR001(node.lineno, node.col_offset))
            elif len(pytestrail_decorators) > 1:
                self.errors.append(TR002(node.lineno, node.col_offset))
            else:
                dec = pytestrail_decorators[0]
                if dec.args:
                    for arg in dec.args:
                        if not (
                            (
                                isinstance(arg, ast.Constant)
                                and isinstance(arg.value, str)
                                and re.match(TEST_CASE_PATTERN, arg.value)
                            )
                            or (
                                isinstance(arg, ast.Str)
                                and re.match(TEST_CASE_PATTERN, arg.s)
                            )
                        ):
                            self.errors.append(
                                TR003(
                                    node.lineno,
                                    node.col_offset,
                                    vars=(TEST_CASE_PATTERN,),
                                )
                            )
                else:
                    self.errors.append(
                        TR003(node.lineno, node.col_offset, vars=(TEST_CASE_PATTERN,))
                    )

        self.generic_visit(node)


class ExtendedError(NamedTuple):
    lineno: int
    col: int
    message: str
    type: Any
    vars: Tuple[Any, ...]


Error = partial(partial, ExtendedError, type=PyTestRailChecker, vars=())


TR001 = Error(message="TR001 Missing `@pytestrail.case()` decorator")
TR002 = Error(message="TR002 Multiple `@pytestrail.case()` decorators")
TR003 = Error(message='TR003 Test case ID should match "{0}" pattern')
