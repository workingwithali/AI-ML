import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import numpy as np
from calculator import (
    add_matrices, subtract_matrices, multiply_matrices,
    transpose_matrix, inverse_matrix
)


def test_addition():
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])
    result = add_matrices(A, B)
    assert np.array_equal(result, np.array([[6, 8], [10, 12]]))

def test_subtraction():
    A = np.array([[5, 6], [7, 8]])
    B = np.array([[1, 2], [3, 4]])
    result = subtract_matrices(A, B)
    assert np.array_equal(result, np.array([[4, 4], [4, 4]]))

def test_multiplication():
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[2, 0], [1, 2]])
    result = multiply_matrices(A, B)
    assert np.array_equal(result, np.array([[4, 4], [10, 8]]))

def test_transpose():
    A = np.array([[1, 2, 3], [4, 5, 6]])
    result = transpose_matrix(A)
    assert np.array_equal(result, np.array([[1, 4], [2, 5], [3, 6]]))

def test_inverse():
    A = np.array([[4, 7], [2, 6]])
    result = inverse_matrix(A)
    expected = np.array([[0.6, -0.7], [-0.2, 0.4]])
    assert np.allclose(result, expected)
