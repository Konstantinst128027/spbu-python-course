from typing import List, Union, Any
import math

# This function add matrix1 and matrix2
def matrix_addition(
    matrix1: List[List[Union[int, float]]], matrix2: List[List[Union[int, float]]]
) -> List[List[Union[int, float]]]:

    """
    Args:
        param1: First matrix, which consists of elements of type int or float (list of lists)
        param2: Second matrix, which consists of elements of type int or float (list of lists)

    Returns:
        matrix that consists of elements obtained by adding the elements of the first and second matrices (list of lists)

    Raises:
        ValueError: if the two matrices have different sizes or if the row sizes are different
    """

    if len(matrix1) != len(matrix2) or any(
        len(row1) != len(row2) for row1, row2 in zip(matrix1, matrix2)
    ):
        raise ValueError("The matrices must be the same size")

    return [[x + y for x, y in zip(row1, row2)] for row1, row2 in zip(matrix1, matrix2)]


# This function multiplies matrix1 and matrix2
def matrix_multiplication(
    matrix1: List[List[Union[int, float]]], matrix2: List[List[Union[int, float]]]
) -> List[List[Union[int, float]]]:
    """
    Args:
        param1: First matrix, which consists of elements of type int or float (list of lists)
        param2: Second matrix, which consists of elements of type int or float (list of lists)

    Returns:
        matrix of the product of two matrices

    Raises:
        ValueError: if the row length of the first matrix is not equal to the column length of the other matrix
    """

    if len(matrix1[0]) != len(matrix2):
        raise ValueError(
            "the number of columns in a matrix must be equal to the number of rows in another matrix"
        )

    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            element = sum(matrix1[i][k] * matrix2[k][j] for k in range(len(matrix2)))
            row.append(element)
        result.append(row)

    return result


# This function transpose matrix
def matrix_transpose(matrix: List[List[Any]]) -> List[List[Any]]:
    """
    Args:
        param1: First matrix, which consists of elements (list of lists)
        param2: Second matrix, which consists of elements (list of lists)

    Returns:
        transported matrix
    """
    return [list(row) for row in zip(*matrix)]  # '*' - unpacks the matrix
