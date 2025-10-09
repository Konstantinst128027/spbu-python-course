import pytest
from project.Task2.generators import *


class Test_pipeline_with_func:
    @pytest.mark.parametrize(
        "input_data,operations,expected",
        [
            (
                [1, 2, 3, 4, 5],
                [
                    (map, (lambda x: x * 3,)),
                    (filter, (lambda x: x % 2 == 1,)),
                ],
                [3, 9, 15],
            ),
            (
                [10, 20, 30, 40, 50],
                [
                    (filter, (lambda x: x > 25,)),
                    (map, (lambda x: x - 5,)),
                ],
                [25, 35, 45],
            ),
            (
                ["a", "bb", "ccc", "dddd", "eeeee"],
                [
                    (filter, (lambda x: len(x) >= 3,)),
                    (map, (lambda x: x * 2,)),
                ],
                ["cccccc", "dddddddd", "eeeeeeeeee"],
            ),
        ],
    )
    def test_pipeline_func(self, input_data, operations, expected):
        pipeline = create_pipeline(data_generator(input_data))
        for f, args in operations:
            pipeline = add_pipeline_step(pipeline, func(f, *args))

        result_iterator = execute_pipeline(pipeline)
        result = collect_pipeline_result(result_iterator)
        assert result == expected


class Test_pipeline_collectors:
    @pytest.mark.parametrize(
        "input_data,collector,expected",
        [
            ([10, 20, 30, 40, 50], list, [10, 20, 30, 40, 50]),
            ([1, 2, 2, 3, 3, 3, 4, 4, 4, 4], set, {1, 2, 3, 4}),
            ([100, 200, 300, 400, 500], tuple, (100, 200, 300, 400, 500)),
            (["python", "java", "rust", "go"], list, ["python", "java", "rust", "go"]),
            (
                ["apple", "banana", "apple", "orange"],
                set,
                {"apple", "banana", "orange"},
            ),
            (["hello", "world", "!"], tuple, ("hello", "world", "!")),
            (
                [("name", "Alice"), ("age", 25), ("city", "London")],
                dict,
                {"name": "Alice", "age": 25, "city": "London"},
            ),
        ],
    )
    def test_pipeline_collectors(self, input_data, collector, expected):
        """Test Pipeline with different collectors"""
        result = collect_pipeline_result(data_generator(input_data), collector)
        assert result == expected

    # Lazy_test
    # Calculated only when needed.
    def test_pipeline_laziness_next(self):
        input_data = [1, 2, 3, 4, 5]

        pipeline = create_pipeline(data_generator(input_data))
        pipeline = add_pipeline_step(pipeline, func(map, lambda x: x * 2))
        pipeline = add_pipeline_step(pipeline, func(filter, lambda x: x > 5))

        result_iterator = execute_pipeline(pipeline)

        first = next(result_iterator)
        assert first == 6

        second = next(result_iterator)
        assert second == 8

        third = next(result_iterator)
        assert third == 10
