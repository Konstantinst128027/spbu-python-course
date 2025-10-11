from typing import Callable, Any, Dict, Optional
from functools import wraps
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
        
        # Привдим нехэшируемые типы объектов к хэшируемым
        def to_hashable(obj: Any) -> Any:
                """We use recursion to make elements like [1, 2, [3, 4]] work correctly"""
                if isinstance(obj, (int, float, str, bytes, bool, type(None))):
                    return obj
                elif isinstance(obj, (list, tuple)):
                    return tuple(to_hashable(item) for item in obj)
                elif isinstance(obj, dict):
                    return tuple(sorted((k, to_hashable(v)) for k, v in obj.items()))
                elif isinstance(obj, set):
                    return tuple(sorted(to_hashable(item) for item in obj))
                else:
                    try:
                        hash(obj)
                        return obj
                    except TypeError:
                        # for other non-hashable objects, use repr to convert them to a string
                        return repr(obj)
        
        cache_dict: Dict[Any, Any] = {}
        
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            sig = inspect.signature(func)
            bound_args = sig.bind(*args, **kwargs)
            bound_args.apply_defaults()
            
            hashable_args = to_hashable(bound_args.args)
            hashable_kwargs = to_hashable(bound_args.kwargs)

            cache_key = (func.__name__, hashable_args, hashable_kwargs)

            if cache_key in cache_dict:
                return cache_dict[cache_key]
            
            if len(cache_dict) == maxsize:
               raise ValueError(f"Cache full: {maxsize} items max")
            
            result = func(*args, **kwargs)
            cache_dict[cache_key] = result
            return result
        
        setattr(wrapper, 'cache_dict', cache_dict)
        
        return wrapper
    
    return decorator