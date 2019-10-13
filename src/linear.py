from typing import List
from math import sqrt

Vector = List[float]


class VectorSizesDifferentError(Exception):
    """ Error raised when the input vectors are of different
    sizes (for elementwise operations)
    """
    pass


def vector_sum(vectors: List[Vector]) -> Vector:
    """Adds corresponding elements"""
    if not(vectors):
        raise ValueError("No vectors provided")

    num_elements = len(vectors[0])
    if not(all(len(v) == num_elements for v in vectors)):
        raise VectorSizesDifferentError

    return [sum(vector[i] for vector in vectors)
            for i in range(num_elements)]


def vector_sub(v: Vector, w: Vector) -> Vector:
    """Subtracts vector w from v (elementwise)"""
    if not(len(v) == len(w)):
        raise VectorSizesDifferentError

    return [v_i - w_i for v_i, w_i in zip(v, w)]


def scalar_multiply(c: float, v: Vector) -> Vector:
    """Multiplies every element by c"""
    return [c * v_i for v_i in v]


def vector_mean(vectors: List[Vector]) -> Vector:
    """Computes the elementwise average"""
    n = len(vectors)

    return scalar_multiply(1/n, vector_sum(vectors))


def dot(v: Vector, w: Vector) -> float:
    """Computes the dot product of the vectors v and w"""
    if not(len(v) == len(w)):
        raise VectorSizesDifferentError

    return sum(v_i * w_i for v_i, w_i in zip(v, w))


def sum_of_squares(v: Vector) -> float:
    """Returns v_1 * v_1 ... + v_n * v_n"""
    return dot(v, v)


def magnitude(v: Vector) -> float:
    """Returns the magnitude (or length) of v"""
    return sqrt(sum_of_squares(v))


def distance(v: Vector, w: Vector) -> float:
    """Computes the scalar distance between the vectors
    v and w"""
    return magnitude(vector_sub(v, w))
