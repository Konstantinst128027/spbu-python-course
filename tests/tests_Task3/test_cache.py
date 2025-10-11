import pytest
from project.Task3.cache import cache

class Test_cache:
    
    def test_simple_function_caching(self):
        """Simple function caching test"""
        @cache(maxsize=3)
        def add(a, b):
            return a + b
        
        result1 = add(2, 3)
        assert result1 == 5
        assert len(add.cache_dict) == 1
        
        result2 = add(5, 7)
        assert result2 == 12
        assert len(add.cache_dict) == 2
        
        result3 = add(2, 3)
        assert result3 == 5
        assert len(add.cache_dict) == 2
    
    def test_builting_functions(self):
        """Test with built-in Python functions"""

        cached_upper = cache(maxsize=2)(str.upper)
        cached_len = cache(maxsize=2)(len)

        result1 = cached_upper("hello")
        result2 = cached_upper("world")
        result3 = cached_upper("hello")
    
        assert result1 == "HELLO"
        assert result2 == "WORLD"
        assert result3 == "HELLO"
        assert len(cached_upper.cache_dict) == 2

        result4 = cached_len("hello")
        result5 = cached_len((1, 2, 3))
        result6 = cached_len("hello")
    
        assert result4 == 5
        assert result5 == 3
        assert result6 == 5
        assert len(cached_len.cache_dict) == 2
    
    def test_unhashable_arguments(self):
        """Test with non-hashable arguments (lists, dictionaries)"""
        @cache(maxsize=2)
        def process_data(data_list, config_dict):
            return len(data_list), len(config_dict)
    
        result1 = process_data([1, 2, 3], {'mode': 'fast'})
        assert result1 == (3, 1)
        assert len(process_data.cache_dict) == 1
    
        result2 = process_data([4, 5], {'mode': 'slow', 'speed': 'high'})
        assert result2 == (2, 2)
        assert len(process_data.cache_dict) == 2

    
    def test_cache_overflow(self):
        """Cache overflow test"""
        @cache(maxsize=2)
        def multiply(a, b):
            return a * b
        
        multiply(2, 3)
        multiply(4, 5)

        with pytest.raises(ValueError):
            multiply(6, 7)
        
        assert len(multiply.cache_dict) == 2
    
    def test_no_caching(self):
        """Disable caching test (maxsize=None)"""
        @cache(maxsize=None)
        def subtract(a, b):
            return a - b
        
        result1 = subtract(10, 3)
        result2 = subtract(10, 3)
        
        assert result1 == 7
        assert result2 == 7

        # We check that the cache was not created
        assert not hasattr(subtract, 'cache_dict')
    