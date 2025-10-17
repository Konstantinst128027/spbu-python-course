from typing import Callable, Any


def curry_explicit(function: Callable[..., Any], arity: int = 0) -> Callable[..., Any]:
    """
    Converts a function to a curried version.

    Arguments:
        function: The function to curry
        arity: How many arguments the original function should take

    Returns:
        The curried version of the function

    ValueError: If arity is a negative number
    """
    if arity < 0:
        raise ValueError("Arity cannot be negative")

    if arity == 0:

        def curried_zero() -> Any:
            return function()

        return curried_zero

    def curried(first_arg: Any) -> Any:
        args: tuple[Any, ...] = (first_arg,)

        if len(args) == arity:  # verification for arity = 1
            return function(*args)

        def next_curried(next_arg: Any) -> Any:
            nonlocal args
            args += (next_arg,)

            if len(args) == arity:
                return function(*args)
            else:
                return next_curried

        return next_curried

    return curried


def uncurry_explicit(
    function: Callable[..., Any], arity: int = 0
) -> Callable[..., Any]:
    """
    Makes a curried function a regular function.

    Args:
        function: A curried function
        arity: The number of arguments

    Returns:
        A function

    ValueError: If arity < 0 or the number of arguments is incorrect
    TypeError: If currying is violated
    """
    if arity < 0:
        raise ValueError("Arity cannot be negative")

    if arity == 0:

        def uncurried_zero() -> Any:
            return function()

        return uncurried_zero

    def uncurried(*args: Any) -> Any:
        if len(args) != arity:
            raise ValueError(f"Expected {arity} arguments, but received {len(args)}")

        result = function
        for arg in args:
            result = result(arg)
        return result

    return uncurried
