import copy
import inspect
from typing import Callable


class Evaluated:
    def __init__(self, func: Callable) -> None:

        if isinstance(func, Isolated):
            raise KeyError("no need to combine Isolated and Evaluated")

        self.func = func


class Isolated:
    def __init__(self, obj=None) -> None:

        if isinstance(obj, Evaluated):
            raise KeyError("no need to combine Isolated and Evaluated")
        self.obj = obj


def smart_args(func):
    """
    A smart decorator for handling function arguments with Isolated and Evaluated.

    Adds special logic for arguments with default values:
        Evaluated: calculates the value each time the function is called
        Isolated: creates a deep copy of the passed value

    Arguments:
        func: The function

    Returns:
        The function with smart argument handling

    AssertionError: If Isolated and Evaluated are used together
    AssertionError: If Isolated/Evaluated arguments are not keyword-only
    ValueError: If no value is passed for the Isolated argument
    """
    signature = inspect.signature(func)  # information about function parameters

    # It is necessary that ONLY named ones are transmitted
    for param_name, param in signature.parameters.items():
        if isinstance(param.default, (Isolated, Evaluated)):
            assert (
                param.kind == param.KEYWORD_ONLY
            ), f"The '{param_name}' argument with {type(param.default).__name__} must be keyword-only (use * for separation)"

    def wrapper(*args, **kwargs):
        bound_args = signature.bind(
            *args, **kwargs
        )  # substitutes the arguments that are passed to the function
        bound_args.apply_defaults()  # takes arguments that were not passed and are given by default and substitutes the default value for the parameter value

        for param_name, param in signature.parameters.items():

            # Evaluated Processing
            if param_name not in kwargs and param.default is not param.empty:
                default_value = param.default

                if isinstance(default_value, Evaluated):
                    bound_args.arguments[param_name] = default_value.func()

            # Isolated Processing
            if param_name in bound_args.arguments and isinstance(
                param.default, Isolated
            ):

                if param_name not in kwargs:
                    raise ValueError(
                        f"The argument {param_name} with Isolated() must be passed a value"
                    )

                original_value = bound_args.arguments[param_name]
                copied_value = copy.deepcopy(original_value)
                bound_args.arguments[param_name] = copied_value

        return func(*bound_args.args, **bound_args.kwargs)

    return wrapper
