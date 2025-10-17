from typing import Callable, Any, Dict, Optional
import inspect


def cache(maxsize: Optional[int] = None) -> Callable:
    """
    Caches the results of a function.

    Stores the results of function calls with different arguments.

    Arguments:
    maxsize: How many results to store. If None, the cache is disabled.

    Returns:
    A function with caching.

    ValueError: if the cache is full
    """

    def decorator(func: Callable) -> Callable:
        if maxsize is None:
            return func

        def to_hashable(obj: Any) -> Any:
            """We use recursion to make elements like [1, 2, [3, 4]] work correctly"""
            if isinstance(obj, (int, float, str, bool, type(None))):
                return obj
            elif isinstance(obj, (list, tuple)):
                return tuple(to_hashable(item) for item in obj)
            elif isinstance(obj, dict):
                return tuple(sorted((k, to_hashable(v)) for k, v in obj.items()))
            elif isinstance(obj, set):
                return tuple(sorted(to_hashable(item) for item in obj))
            else:
                try:
                    hash(obj)  # outputs a number
                    return obj
                except TypeError:
                    # for other non-hashable objects, use repr to convert them to a string
                    return repr(obj)

        cache_dict: Dict[Any, Any] = {}
        keys: list[Any] = []

        def wrapper(*args: Any, **kwargs: Any) -> Any:

            hashable_args = to_hashable(args)
            hashable_kwargs = to_hashable(kwargs)

            cache_key = (func.__name__, hashable_args, hashable_kwargs)
            keys.append((func.__name__, hashable_args, hashable_kwargs))

            if cache_key in cache_dict:
                return cache_dict[cache_key]

            if len(cache_dict) == maxsize:

                oldest_key = keys.pop(0)  # deleting the very first key
                del cache_dict[oldest_key]  # deleting the very first function call

            result = func(*args, **kwargs)
            cache_dict[cache_key] = result
            return result

        setattr(wrapper, "cache_dict", cache_dict)
        setattr(wrapper, "keys", keys)

        return wrapper

    return decorator
