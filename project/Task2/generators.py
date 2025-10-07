from typing import (Any, Generator, Iterable, List, Union, Dict, Callable, Iterator)
from functools import reduce

def data_generator(
    data_source: Union[List[Any], Generator[Any, None, None], range, Iterable[Any]] # Iterable - objects that can be traversed element by element
) -> Generator[Any, None, None]: # Arg_2 - what type can be added , Arg_3 - what type can be returned
    
    """
    Generator for input data generation.
    Args:
        data_source: Source of data (list, generator or range)
    Yields:
        Data items from the source
    """
    if isinstance(data_source, Generator): # checks for type

        yield from data_source

    else:

        for item in data_source:
            yield item


def create_pipeline(data: Iterable[Any]) -> Dict[str, Any]:
    """
    Creates a new pipeline with source data.

    Args:
        data: Source data (list, generator, range, etc.)

    Returns:
        Dictionary with data and processing steps
    """
    return {
        'data': data,
        'steps': []
    }

def add_pipeline_step(
    pipeline: Dict[str, Any], 
    func: Callable[..., Any], # ... - everything type of object
    *args: Any, 
    **kwargs: Any
) -> Dict[str, Any]:
    """
    Adds a processing step to the pipeline.

    Args:
        pipeline: Pipeline to modify
        func: Function to apply to data
        *args: Positional arguments for the function
        **kwargs: Keyword arguments for the function

    Returns:
        Updated pipeline (for method chaining)
    """
    pipeline['steps'].append((func, args, kwargs))
    return pipeline

def execute_pipeline(pipeline: Dict[str, Any]) -> Iterator[Any]:
    """
    Executes all pipeline steps and returns an iterator.

    Args:
        pipeline: Pipeline to execute

    Returns:
        Iterator over processed data
    """

    current_data: Iterable[Any] = pipeline['data']
    
    for step in pipeline['steps']:
        func, args, kwargs = step
        current_data = func(*args, current_data, **kwargs)
    
    # return iterator
    return iter(current_data)

def collect_pipeline_result(
    pipeline: Iterator[Any],
    collector: Callable[[Iterable[Any]], Any] = list,
    *args: Any,
    **kwargs: Any
) -> Any:
    """
    Collects pipeline results into a collection.

    Args:
        pipeline: Pipeline to collect results from
        collector: Function to collect results (list, set, tuple, etc.)
        *args: Arguments for the collector
        **kwargs: Keyword arguments for the collector

    Returns:
        Collected data in the specified format
    """

    return collector(pipeline, *args, **kwargs)

def func(
    f: Callable[..., Any], 
    *args: Any, 
    **kwargs: Any
) -> Callable[[Iterable[Any]], Iterator[Any]]:
    """
    Adapts a function to work with the pipeline (map, filter, enumerate, reduce)

    Args:
        f: Function to wrap
        *args: Positional arguments for the function
        **kwargs: Keyword arguments for the function

    Returns:
        function that takes iterable and returns iterator
    """
    
    # for filter, map, enumerate - because they have already been iterator
    if f in [filter, map, enumerate]:
        return lambda data: f(*args, data, **kwargs)
    
    # for reduce - special realization
    elif f == reduce:
        if len(args) >= 2:
            return lambda data: iter([f(args[0], data, *args[1:], **kwargs)])
        else:
            return lambda data: iter([f(*args, data, **kwargs)])
    
    else:
        return lambda data: iter(f(data, *args, **kwargs))
    

