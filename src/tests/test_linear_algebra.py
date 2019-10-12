import pytest

from src.linear import (
    Vector,
    VectorSizesDifferentError,
    vector_add,
    vector_sub)


def test_vector_add():
    v = [1, 2, 3]
    w = [4, 5, 6]
    z = [0, 0, 1]
    assert vector_add([v, w, z]) == [5, 7, 10]


def test_vector_sub():
    v = [3, 6, 9]
    w = [1, 2, 3]
    assert vector_sub(v, w) == [2, 4, 6]


def test_vector_add_different_sizes_exception():
    with pytest.raises(VectorSizesDifferentError):
        vector_add([[1, 2], [0]])


def test_vector_sub_different_sizes_exception():
    with pytest.raises(VectorSizesDifferentError):
        vector_sub([1, 2], [0])


def test_vector_add_empty_vector_list_error():
    with pytest.raises(ValueError):
        vector_add([])
