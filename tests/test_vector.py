import pytest
import math
import project.vectors as vt

class Test_Vector_Operations:
    def test_dot_product(self):
        
        assert vt.dot_product([1, 2, 3], [4, 5, 6]) == 32

        assert vt.dot_product([0, 0], [0, 0]) == 0

        assert vt.dot_product([-1, 2], [3, -4]) == -11

        assert abs(vt.dot_product([0.1, 0.2], [0.3, 0.4]) - 0.11) < 0.0001

        with pytest.raises(ValueError):
            vt.dot_product([1, 2], [1, 2, 3])  # different lenght

    def test_vector_length(self):

        assert vt.vector_length([3, 4]) == 5.0

        assert vt.vector_length([0, 0]) == 0.0

        assert vt.vector_length([-3, -4]) == 5.0

        assert abs(vt.vector_length([1, 2, 2]) - 3.0) < 0.0001

    def test_angle_between_vectors(self):

        assert vt.angle_between_vectors([1, 0], [2, 0]) == pytest.approx(0.0)

        assert vt.angle_between_vectors([1, 0], [0, 1]) == pytest.approx(math.pi / 2)

        assert vt.angle_between_vectors([1, 0, 0], [0, 1, 0]) == pytest.approx(math.pi / 2)

        with pytest.raises(ValueError):
            vt.angle_between_vectors([0, 0], [1, 2])  # nool vector

        with pytest.raises(ValueError):
            vt.angle_between_vectors([1, 2], [1, 2, 3])  # Different lenght