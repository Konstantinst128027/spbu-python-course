import pytest
from project.Task3.smart_args import *

counter = 0
def get_counter():
    global counter
    counter += 1
    return counter

def test_evaluated_basic():
    global counter
    counter = 0
    
    @smart_args
    def test_func(*, x=Evaluated(get_counter)):
        return x
    
    result1 = test_func()
    result2 = test_func()
    
    assert result1 == 1
    assert result2 == 2

def test_evaluated_with_passed_argument():
    global counter
    counter = 0
    
    @smart_args
    def test_func(*, x=Evaluated(get_counter)):
        return x
    
    result = test_func(x=100)
    assert result == 100
    assert counter == 0

def test_isolated_basic():
    original_list = [1, 2, 3]
    
    @smart_args
    def test_func(*, data=Isolated()):
        data.append(4)
        return data
    
    result = test_func(data=original_list)
    
    assert result == [1, 2, 3, 4]
    assert original_list == [1, 2, 3]  # Оригинал не изменился

def test_isolated_without_value():
    @smart_args
    def test_func(*, data=Isolated()):
        return data
    
    with pytest.raises(ValueError):
        test_func()


def test_isolated_and_evaluated_together_error():
    with pytest.raises(AssertionError):
        @smart_args
        def invalid_func(*, x=Isolated(), y=Evaluated(get_counter)):
            return x, y

def test_non_keyword_only_error():
    with pytest.raises(AssertionError):
        @smart_args
        def invalid_func(x=Isolated()):
            return x
    with pytest.raises(AssertionError):
        @smart_args
        def invalid_func(x=Evaluated(get_counter)):
            return x