import pytest
from project.Task3.un_curry_explicit import *


def test_curry_explicit_basic():
    def func(a, b, c):
        return f"({a}, {b}, {c})"

    curried = curry_explicit(func, 3)

    assert curried(1)(2)(3) == "(1, 2, 3)"
    assert curried(1, 2)(3) == "(1, 2, 3)"
    assert curried(1, 2, 3) == "(1, 2, 3)"


def test_curry_explicit_zero_arity():
    def func():
        return "result"

    curried = curry_explicit(func, 0)
    assert curried() == "result"


def test_curry_explicit_negative_arity():
    with pytest.raises(ValueError):
        curry_explicit(lambda x: x, -1)


def test_curry_explicit_with_builtin():
    curried_add = curry_explicit(lambda x, y: x + y, 2)
    assert curried_add(5)(3) == 8
    assert curried_add(10)(20) == 30


def test_curry_explicit_variable_arity_ignored():
    def func(a, b, c):
        return a + b + c

    curried = curry_explicit(func, 3)

    assert curried(1, 2, 3, 4, 5) == 6
    assert curried(1)(2, 3, 4, 5) == 6


def test_curry_explicit_multiple_args_at_once():
    def func(a, b, c, d):
        return f"{a} {b} {c} {d}"

    curried = curry_explicit(func, 4)

    assert curried(1)(2, 3)(4) == "1 2 3 4"
    assert curried(1, 2)(3, 4) == "1 2 3 4"
    assert curried(1, 2, 3)(4) == "1 2 3 4"


def test_uncurry_explicit_basic():
    def func(a, b, c):
        return a + b + c

    curried = curry_explicit(func, 3)
    uncurried = uncurry_explicit(curried, 3)

    assert uncurried(1, 2, 3) == 6


def test_uncurry_explicit_zero_arity():
    def func():
        return "zero"

    curried = curry_explicit(func, 0)
    uncurried = uncurry_explicit(curried, 0)

    assert uncurried() == "zero"


def test_uncurry_explicit_wrong_args_count():
    curried = curry_explicit(lambda x, y: x + y, 2)
    uncurried = uncurry_explicit(curried, 2)

    with pytest.raises(ValueError):
        uncurried(1, 2, 3)


def test_uncurry_explicit_negative_arity():
    with pytest.raises(ValueError):
        uncurry_explicit(lambda x: x, -1)


def test_uncurry_explicit_with_builtin():
    curried = curry_explicit(lambda x, y, z: x * y * z, 3)
    uncurried = uncurry_explicit(curried, 3)

    assert uncurried(2, 3, 4) == 24
