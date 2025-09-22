from flask import Flask, render_template, request
import numpy as np
from calculator import (
    add_matrices, subtract_matrices, multiply_matrices,
    transpose_matrix, inverse_matrix
)

app = Flask(__name__)

def parse_matrix(matrix_str):
    """
    Convert a textarea string into a NumPy matrix.
    Rows separated by newlines, values by spaces.
    Example:
    1 2
    3 4
    """
    try:
        rows = matrix_str.strip().split("\n")
        matrix = [list(map(float, row.split())) for row in rows]
        return np.array(matrix)
    except Exception:
        raise ValueError("Invalid matrix format. Use rows separated by newlines and values by spaces.")

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None

    if request.method == "POST":
        operation = request.form.get("operation")
        try:
            A = parse_matrix(request.form.get("matrixA"))
            if operation in ["add", "subtract", "multiply"]:
                B = parse_matrix(request.form.get("matrixB"))
            else:
                B = None

            if operation == "add":
                result = add_matrices(A, B)
            elif operation == "subtract":
                result = subtract_matrices(A, B)
            elif operation == "multiply":
                result = multiply_matrices(A, B)
            elif operation == "transpose":
                result = transpose_matrix(A)
            elif operation == "inverse":
                result = inverse_matrix(A)
        except Exception as e:
            error = str(e)

    return render_template("index.html", result=result, error=error)

if __name__ == "__main__":
    app.run(debug=True)
