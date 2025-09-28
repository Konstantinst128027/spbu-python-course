import pytest
import math
import project.matrixs as mt

class Test_Matrix_Operations:
    def test_matrix_addition(self):

        matrix1 = [[1, 2], [3, 4]]
        matrix2 = [[5, 6], [7, 8]]
        expected = [[6, 8], [10, 12]]
        assert mt.matrix_addition(matrix1, matrix2) == expected

        matrix1 = [[-1, 2], [3, -4]]
        matrix2 = [[5, -6], [-7, 8]]
        expected = [[4, -4], [-4, 4]]
        assert mt.matrix_addition(matrix1, matrix2) == expected

        with pytest.raises(ValueError):
            mt.matrix_addition([[1, 2]], [[1]])  # different size of matrix

    def test_matrix_multiplication(self):

        matrix1 = [[1, 2], [3, 4]]
        matrix2 = [[5, 6], [7, 8]]
        expected = [[19, 22], [43, 50]]
        assert mt.matrix_multiplication(matrix1, matrix2) == expected

        matrix1 = [[1, 2, 3], [4, 5, 6]]
        matrix2 = [[7, 8], [9, 10], [11, 12]]
        expected = [[58, 64], [139, 154]]
        assert mt.matrix_multiplication(matrix1, matrix2) == expected

        with pytest.raises(ValueError):
            mt.matrix_multiplication([[1, 2, 3]], [[1, 2]])  # incompatible sizes

    def test_matrix_transpose(self):

        matrix = [[1, 2, 3], [4, 5, 6]]
        expected = [[1, 4], [2, 5], [3, 6]]
        assert mt.matrix_transpose(matrix) == expected

        matrix = [[1, 2], [3, 4]]
        expected = [[1, 3], [2, 4]]
        assert mt.matrix_transpose(matrix) == expected

        matrix = [[1, 2, 3]]
        expected = [[1], [2], [3]]
        assert mt.matrix_transpose(matrix) == expected
