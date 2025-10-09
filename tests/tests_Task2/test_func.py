import pytest
from typing import Any, Iterable, Iterator
from functools import reduce
from project.Task2.generators import func, data_generator


class Test_Func:
    """Tests for func helper function"""

    # My own function
    def double_all(iterable: Iterable[Any]) -> Iterator[Any]:
        for item in iterable:
            yield item * 2

    @pytest.mark.parametrize(
        "f,args,test_data,expected",
        [
            (map, (lambda x: x**2,), [1, 2, 3, 4, 5], [1, 4, 9, 16, 25]),
            (map, (abs,), [-5, 3, -1, 0, -10], [5, 3, 1, 0, 10]),
            (map, (lambda x: x * 10 + 5,), [0, 1, 2], [5, 15, 25]),
            (filter, (lambda x: x > 0,), [-3, -1, 0, 2, 5, -2], [2, 5]),
            (
                filter,
                (lambda x: len(x) == 3,),
                ["cat", "dog", "elephant", "fox"],
                ["cat", "dog", "fox"],
            ),
            (filter, (lambda x: x % 3 == 0,), range(1, 11), [3, 6, 9]),
            (
                filter,
                (lambda x: x.startswith("A"),),
                ["Apple", "Banana", "Apricot", "Cherry"],
                ["Apple", "Apricot"],
            ),
            (
                enumerate,
                (),
                ["first", "second", "third"],
                [(0, "first"), (1, "second"), (2, "third")],
            ),
            (enumerate, (), [100, 200, 300], [(0, 100), (1, 200), (2, 300)]),
            (zip, (["x", "y", "z"],), [1, 2, 3], [(1, "x"), (2, "y"), (3, "z")]),
            (zip, ([10, 20],), [1, 2, 3], [(1, 10), (2, 20)]),
            (
                zip,
                ([True, False], [0.1, 0.2]),
                [1, 2],
                [(1, True, 0.1), (2, False, 0.2)],
            ),
            (reduce, (lambda x, y: max(x, y),), [3, 1, 4, 1, 5], [5]),
            (reduce, (lambda x, y: min(x, y),), [3, 1, 4, 1, 5], [1]),
            (
                reduce,
                (lambda x, y: x + " " + y,),
                ["hello", "world", "!"],
                ["hello world !"],
            ),
            (reduce, (lambda x, y: x * y, 2), [3, 4, 5], [120]),
            (reduce, (lambda x, y: x - y, 100), [10, 20, 30], [40]),
            (double_all, (), [-1, 0, 1], [-2, 0, 2]),
        ],
    )
    def test_func(self, f, args, test_data, expected):
        wrapped_func = func(f, *args)
        result = list(wrapped_func(test_data))
        assert result == expected

        # Lazy_test
        gen = wrapped_func(data_generator(test_data))

        taken_elements = []

        for i in range(min(3, len(expected))):
            element = next(gen)
            taken_elements.append(element)
            assert element == expected[i]

        if len(expected) > 3:
            remaining = list(gen)
            assert taken_elements + remaining == expected
