# calculator.py
import numpy as np

def add_matrices(A, B):
    A, B = np.array(A), np.array(B)
    if A.shape != B.shape:
        raise ValueError("Matrices must have the same shape for addition.")
    return A + B

def subtract_matrices(A, B):
    A, B = np.array(A), np.array(B)
    if A.shape != B.shape:
        raise ValueError("Matrices must have the same shape for subtraction.")
    return A - B

def multiply_matrices(A, B):
    A, B = np.array(A), np.array(B)
    if A.shape[1] != B.shape[0]:
        raise ValueError("Invalid shapes: A’s columns must equal B’s rows.")
    return A.dot(B)

def transpose_matrix(A):
    return np.array(A).T

def inverse_matrix(A):
    A = np.array(A)
    if A.shape[0] != A.shape[1]:
        raise ValueError("Matrix must be square to invert.")
    if np.linalg.det(A) == 0:
        raise ValueError("Matrix is singular and cannot be inverted.")
    return np.linalg.inv(A)
