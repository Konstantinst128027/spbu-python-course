import pytest
from project.Task2.generators import data_generator


class Test_Data_Generator:
    @pytest.mark.parametrize(
        "input_data,expected",
        [
            ([10, 20, 30, 40, 50], [10, 20, 30, 40, 50]),
            (range(5, 11), [5, 6, 7, 8, 9, 10]),
            ([100, -50, 0, 75], [100, -50, 0, 75]),
            (["python", "java", "rust"], ["python", "java", "rust"]),
            (["a", "bb", "ccc", "dddd"], ["a", "bb", "ccc", "dddd"]),
            (["", "hello", "world"], ["", "hello", "world"]),
            ([1, "hello", 3.14, True], [1, "hello", 3.14, True]),
            ([None, 42, "text", False], [None, 42, "text", False]),
            ((100, 200, 300), [100, 200, 300]),
            ({"a": 1, "b": 2}, ["a", "b"]),
            ({1, 2, 3, 2, 1}, [1, 2, 3]),
            ([], []),
            ([999], [999]),
            ([0, 0, 0], [0, 0, 0]),
        ],
    )
    def test_data_generator(self, input_data, expected):
        result = list(data_generator(input_data))
        assert result == expected

        # Lazy_test
        gen = data_generator(input_data)
        for i in range(3):
            if i < len(expected):
                argument = next(gen)
                assert argument == expected[i]
            else:
                break
        if len(expected) > 3:
            assert list(gen) == expected[3:]
