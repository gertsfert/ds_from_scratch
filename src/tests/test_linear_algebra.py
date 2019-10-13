import pytest

from src.linear import (
    Vector,
    VectorSizesDifferentError,
    vector_sum,
    vector_sub,
    scalar_multiply,
    vector_mean,
    sum_of_squares,
    magnitude,
    distance,
    dot)


def test_vector_sum():
    v = [1, 2, 3]
    w = [4, 5, 6]
    z = [0, 0, 1]
    assert vector_sum([v, w, z]) == [5, 7, 10]


def test_vector_sub():
    v = [3, 6, 9]
    w = [1, 2, 3]
    assert vector_sub(v, w) == [2, 4, 6]


def test_vector_sum_different_sizes_exception():
    with pytest.raises(VectorSizesDifferentError):
        vector_sum([[1, 2], [0]])


def test_vector_sub_different_sizes_exception():
    with pytest.raises(VectorSizesDifferentError):
        vector_sub([1, 2], [0])


def test_vector_add_empty_vector_list_error():
    with pytest.raises(ValueError):
        vector_sum([])


def test_vector_scalar_multiply():
    assert scalar_multiply(3, [1, 2, 0, 3]) == [3, 6, 0, 9]


def test_vector_mean():
    assert vector_mean([
        [1, 2],
        [3, 4],
        [5, 6]]) == [3, 4]


def test_dot():
    assert dot(
        [1, 2, 3],
        [4, 5, 6]) == 32


def test_dot_raise_error_on_different_vectors():
    with pytest.raises(VectorSizesDifferentError):
        dot([1, 2], [3])


def test_sum_of_squares():
    assert sum_of_squares([1, 2, 3]) == 14


def test_magnitude():
    assert magnitude([3, 4]) == 5


def test_distance():
    assert distance(
        [9, 7],
        [6, 3]) == 5
