import math
import random

try:
    import numpy as np
except ImportError:
    np = None

from matlibrary import Matrix


def _frob_norm(data):
    total = 0.0
    for row in data:
        for val in row:
            total += val * val
    return math.sqrt(total)


def _diff_frob(a, b):
    if not a:
        return 0.0
    total = 0.0
    rows = len(a)
    cols = len(a[0])
    for i in range(rows):
        for j in range(cols):
            diff = a[i][j] - b[i][j]
            total += diff * diff
    return math.sqrt(total)


def _residual_error(A, Q, R):
    A_data = A.to_float_data()
    QR_data = (Q * R).to_float_data()
    return _diff_frob(A_data, QR_data)


def _orthogonality_error(Q):
    m, _ = Q.dim
    QtQ = Q.transpose() * Q
    I = Matrix.identity(m, tolerance=Q.tolerance, dtype="float")
    return _diff_frob(QtQ.to_float_data(), I.to_float_data())


def _numpy_qr(data):
    if np is None:
        print("numpy is not installed. Install with: pip install numpy")
        return None
    A_np = np.array(data, dtype=float)
    Q_np, R_np = np.linalg.qr(A_np)
    return A_np, Q_np, R_np


def _numpy_echelon(data, tol=1e-12):
    """Return numpy row echelon form (not reduced) of a matrix."""
    if np is None:
        return None
    A = np.array(data, dtype=float, copy=True)
    rows, cols = A.shape
    row = 0
    for col in range(cols):
        if row >= rows:
            break
        pivot = row + int(np.argmax(np.abs(A[row:, col])))
        if abs(A[pivot, col]) <= tol:
            continue
        if pivot != row:
            A[[row, pivot]] = A[[pivot, row]]
        for r in range(row + 1, rows):
            factor = A[r, col] / A[row, col]
            if abs(factor) > tol:
                A[r, col:] -= factor * A[row, col:]
        row += 1
    return A


def _format_matrix(data, precision=6, width=12):
    if not data:
        return "[]"
    lines = []
    for row in data:
        parts = [f"{val:>{width}.{precision}f}" for val in row]
        lines.append("[" + " ".join(parts) + "]")
    return "\n".join(lines)


def _array_to_float_list(array_like):
    if np is None:
        return []
    return np.array(array_like, dtype=float).tolist()


def main():
    print("=" * 60)
    print("Task 1")

    rng = random.Random(0)
    rows, cols = 10, 8
    data = [[rng.randint(-9, 9) for _ in range(cols)] for _ in range(rows)]
    A = Matrix(data, tolerance=1e-10, dtype="float")

    print("Original matrix A (10x8):")
    print(A)
    print()

    ref, swaps = A.gauss_elimination(pivoting=True)
    print("Row echelon form (pivoting=True):")
    print(ref)
    print(f"Number of row swaps: {swaps}")
    print()

    if np is not None:
        np_ech = _numpy_echelon(data)
        if np_ech is not None:
            print("Numpy row echelon form (for comparison):")
            print(_format_matrix(_array_to_float_list(np_ech), precision=4, width=10))
            our_rank = ref.rank()
            np_rank = int(np.linalg.matrix_rank(np.array(data, dtype=float)))
            print(f"Our rank: {our_rank}, Numpy rank: {np_rank}")
    else:
        print("numpy not available for verification.")
    print()

    print("=" * 60)
    print("Task 2")

    A2_data = [[3, 14, 9],
               [6, 43, 3],
               [6, 22, 15]]
    A2 = Matrix(A2_data, tolerance=1e-10, dtype="float")
    Q2_h, R2_h = A2.qr_decomposition(method="householder")

    print("Matrix A:")
    print(A2)
    print()
    print("Householder Q:")
    print(Q2_h)
    print()
    print("Householder R:")
    print(R2_h)
    print()

    err_h = _residual_error(A2, Q2_h, R2_h)
    orth_h = _orthogonality_error(Q2_h)
    print(f"Householder: residual={err_h:.6e}, orthogonality={orth_h:.6e}")
    print()

    numpy_result2 = _numpy_qr(A2_data)
    if numpy_result2 is not None:
        A2_np, Q2_np, R2_np = numpy_result2
        diff = A2_np - Q2_np @ R2_np
        err_np = float(np.linalg.norm(diff, ord="fro"))
        print("Numpy Q:")
        print(_format_matrix(_array_to_float_list(Q2_np), precision=4, width=12))
        print("Numpy R:")
        print(_format_matrix(_array_to_float_list(R2_np), precision=4, width=12))
        print(f"Numpy QR:    residual={err_np:.6e}")
    print()

    print("=" * 60)
    print("Task 3")

    A3_data = [[2, 2, 1],
               [0, 2, 2],
               [2, 1, 2]]
    A3 = Matrix(A3_data, tolerance=1e-10, dtype="float")
    Q3_g, R3_g = A3.qr_decomposition(method="givens")

    print("Matrix A:")
    print(A3)
    print()
    print("Givens Q:")
    print(Q3_g)
    print()
    print("Givens R:")
    print(R3_g)
    print()

    err_g = _residual_error(A3, Q3_g, R3_g)
    orth_g = _orthogonality_error(Q3_g)
    print(f"Givens:      residual={err_g:.6e}, orthogonality={orth_g:.6e}")
    print()

    # numpy verification
    numpy_result3 = _numpy_qr(A3_data)
    if numpy_result3 is not None:
        A3_np, Q3_np, R3_np = numpy_result3
        diff = A3_np - Q3_np @ R3_np
        err_np = float(np.linalg.norm(diff, ord="fro"))
        print("Numpy Q:")
        print(_format_matrix(_array_to_float_list(Q3_np), precision=4, width=12))
        print("Numpy R:")
        print(_format_matrix(_array_to_float_list(R3_np), precision=4, width=12))
        print(f"Numpy QR:    residual={err_np:.6e}")
    print()


if __name__ == "__main__":
    main()