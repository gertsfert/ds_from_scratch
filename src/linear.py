from typing import List

Vector = List[float]


class VectorSizesDifferentError(Exception):
    """ Error raised when the input vectors are of different
    sizes (for elementwise operations)
    """
    pass


def vector_add(vectors: List[Vector]) -> Vector:
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
