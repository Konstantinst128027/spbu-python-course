from typing import List, Union, Any
import math

# This function produces a scalar product of two vectors
def dot_product(
    vector1: List[Union[int, float]], vector2: List[Union[int, float]]
) -> Union[int, float]:
    """
    Args:
        param1: First vector (list)
        param2: Second vector (list)

    Returns:
        scalar product of vectors (number)

    Raises:
        ValueError: if the two vectors have different size
    """
    if len(vector1) != len(vector2):
        raise ValueError("The vectors must be the same length.")
    return sum(x * y for x, y in zip(vector1, vector2))


# This function calculates the length of the vector
def vector_length(vector: List[Union[int, float]]) -> float:
    """
    Args:
        param1: vector (list)

    Returns:
        lenght of vector(number)
    """
    return math.sqrt(sum(x * x for x in vector))


# This function finds the angle between two vectors
def angle_between_vectors(
    vector1: List[Union[int, float]], vector2: List[Union[int, float]]
) -> float:
    """
    Args:
        param1: first vector (list)
        param2: second vector (list)

    Returns:
        we get the angle in radiars

    Raises:
        ValueError: if the two vectors have different size
        ValueError: if one of vectors is null
    """
    if len(vector1) != len(vector2):
        raise ValueError("The vectors must be the same length.")

    dot = dot_product(vector1, vector2)
    length1 = vector_length(vector1)
    length2 = vector_length(vector2)

    if length1 == 0 or length2 == 0:
        raise ValueError("the vectors should not be null")

    cos_angle = dot / (length1 * length2)

    # Ensuring that the value is within the valid range for arccos
    cos_angle = max(-1.0, min(1.0, cos_angle))

    return math.acos(cos_angle)
