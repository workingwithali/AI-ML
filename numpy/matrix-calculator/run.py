# run.py
import numpy as np
from calculator import (
    add_matrices, subtract_matrices, multiply_matrices,
    transpose_matrix, inverse_matrix
)

def get_matrix_input(name):
    rows = int(input(f"Enter number of rows for {name}: "))
    cols = int(input(f"Enter number of columns for {name}: "))
    print(f"Enter elements row by row, separated by spaces:")
    elements = []
    for i in range(rows):
        row = list(map(float, input(f"Row {i+1}: ").split()))
        if len(row) != cols:
            raise ValueError("Row length mismatch.")
        elements.append(row)
    return np.array(elements)

def main():
    print("=== Matrix Calculator ===")
    print("Choose operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Transpose")
    print("5. Inverse")
    
    choice = input("Enter choice (1-5): ")

    if choice in {"1", "2", "3"}:
        A = get_matrix_input("Matrix A")
        B = get_matrix_input("Matrix B")
        if choice == "1":
            result = add_matrices(A, B)
        elif choice == "2":
            result = subtract_matrices(A, B)
        else:
            result = multiply_matrices(A, B)
    elif choice == "4":
        A = get_matrix_input("Matrix A")
        result = transpose_matrix(A)
    elif choice == "5":
        A = get_matrix_input("Matrix A")
        result = inverse_matrix(A)
    else:
        print("Invalid choice.")
        return

    print("\nResult:\n", result)

if __name__ == "__main__":
    main()
