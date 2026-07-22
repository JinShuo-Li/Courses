import copy
import tkinter as tk
from tkinter import ttk, messagebox

#################################################################
### 1. BACKEND CODE (Your functions, updated and completed)
#################################################################

def transpose(mat):
    """Calculates the transpose of a matrix."""
    if not mat or not mat[0]:
        return []
    
    rows = len(mat)
    cols = len(mat[0])
    
    transposed = []
    for j in range(cols):
        new_row = []
        for i in range(rows):
            # Check for jagged arrays (uneven rows)
            if i < len(mat) and j < len(mat[i]):
                new_row.append(mat[i][j])
            else:
                # Pad with 0 if matrix is not rectangular
                new_row.append(0) 
        transposed.append(new_row)
    return transposed

def gaussian_elimination(mat):
    """Transfers the matrix into Row Echelon Form (REF) using Gaussian elimination."""
    matrix = copy.deepcopy(mat)
    n = len(matrix)
    m = len(matrix[0]) if n > 0 else 0
    if n == 0 or m == 0:
        return matrix, 0
        
    index = 0
    counter = 0  # Row swap counter
    for j in range(m):
        if index >= n:
            break
        
        # Find pivot
        t = index
        while t < n and abs(matrix[t][j]) < 1e-10:
            t += 1
            
        if t == n: # No pivot in this column
            continue
        else:
            if index != t:
                counter += 1
                matrix[index], matrix[t] = matrix[t], matrix[index]
            
            factor = matrix[index][j]
            if abs(factor) < 1e-10: continue # Should not happen, but safe
            
            # Eliminate rows below
            for row in range(index + 1, n):
                if abs(matrix[row][j]) > 1e-10:
                    multiplier = matrix[row][j] / factor
                    for col in range(j, m):
                        matrix[row][col] -= multiplier * matrix[index][col]
        index += 1
    return matrix, counter

def gaussian_elimination_simplified(mat):
    """Transfers the matrix into Row Reduced Echelon Form (RREF)."""
    matrix = copy.deepcopy(mat)
    n = len(matrix)
    m = len(matrix[0]) if n > 0 else 0
    if n == 0 or m == 0:
        return matrix, 0

    index = 0
    counter = 0 # Row swap counter
    
    for j in range(m):
        if index >= n:
            break
        
        # Find pivot
        t = index
        while t < n and abs(matrix[t][j]) < 1e-10:
            t += 1
            
        if t == n: # No pivot
            continue
        else:
            if index != t:
                counter += 1
                matrix[index], matrix[t] = matrix[t], matrix[index]
            
            # Scale pivot row to 1
            pivot = matrix[index][j]
            if abs(pivot) > 1e-10:
                for col in range(j, m):
                    matrix[index][col] /= pivot
            
            # Eliminate all other rows (above and below)
            for row in range(n):
                if row == index:
                    continue
                if abs(matrix[row][j]) > 1e-10:
                    multiplier = matrix[row][j]
                    for col in range(j, m):
                        matrix[row][col] -= multiplier * matrix[index][col]
            
            index += 1
    return matrix, counter

def rank_of_matrix(mat):
    """Determines the rank of a matrix."""
    matrix, _ = gaussian_elimination(mat) # Use REF
    rank = 0
    for row in matrix:
        for val in row:
            if abs(val) > 1e-10:
                rank += 1
                break
    return rank

def format_matrix(matrix, decimals=3):
    """Formats the matrix for clean printing."""
    formatted = []
    for row in matrix:
        formatted_row = []
        for value in row:
            if abs(value) < 1e-10:
                formatted_value = 0.0
            else:
                formatted_value = round(value, decimals)
            formatted_row.append(formatted_value)
        formatted.append(formatted_row)
    return formatted

def det_REF(mat, counter):
    """Calculate the determinant from an REF matrix and row-swap counter."""
    m = len(mat)
    n = len(mat[0]) if m > 0 else 0
    result = 1
    if m != n:
        raise ValueError("Determinant requires a square matrix.")
    if m == 0:
        return 1 # Determinant of empty matrix is 1
        
    for i in range(m):
        result *= mat[i][i]
    result = result * ((-1) ** counter)
    return result

def det(mat):
    """Calculate the determinant using Laplace method and Recursion."""
    result = 0
    m = len(mat)
    n = len(mat[0]) if m > 0 else 0
    if m != n:
        raise ValueError("Determinant requires a square matrix.")
    if m == 0:
        return 1
    elif m == 1:
        return mat[0][0]
    elif m == 2:
        return (mat[0][0] * mat[1][1]) - (mat[1][0] * mat[0][1])
    else:
        for j in range(m):
            new_mat = []
            if abs(mat[0][j]) < 1e-10:
                continue
            for i in range(1, m):
                row = []
                for k in range(m):
                    if j == k:
                        continue
                    else:
                        row.append(mat[i][k])
                new_mat.append(row)
            result += ((-1) ** j) * (det(new_mat)) * (mat[0][j])
    return result

def full_rank_decomposition(matrix):
    """Performs full rank decomposition A = FG."""
    r = rank_of_matrix(matrix)
    if r == 0:
        return [], [], 0
        
    rref_matrix, _ = gaussian_elimination_simplified(matrix)
    pivot_columns = []
    rows = len(rref_matrix)
    cols = len(rref_matrix[0]) if rows > 0 else 0
    
    for i in range(rows):
        for j in range(cols):
            if abs(rref_matrix[i][j]) > 1e-10:
                pivot_columns.append(j)
                break
    
    # Extract F from original matrix columns
    F = []
    for i in range(len(matrix)):
        new_row = []
        for j in pivot_columns:
            new_row.append(matrix[i][j])
        F.append(new_row)
        
    # Extract G from non-zero rows of RREF
    G = []
    for i in range(rows):
        is_zero_row = True
        for val in rref_matrix[i]:
            if abs(val) > 1e-10:
                is_zero_row = False
                break
        if not is_zero_row:
            G.append(rref_matrix[i])
            
    return F, G, r

def find_maximal_linearly_independent_subset(mat):
    """Finds a maximal linearly independent subset of the columns."""
    matrix = transpose(mat) # Work with columns as rows
    result_subset = []
    index = 0
    for i in matrix:
        test_subset = result_subset + [i]
        if rank_of_matrix(test_subset) == index + 1:
            result_subset.append(i)
            index += 1
    return transpose(result_subset) # Transpose back to columns

def matrix_addition(mat_1, mat_2):
    """Adds two matrices."""
    if not mat_1 or not mat_2 or len(mat_1) != len(mat_2) or len(mat_1[0]) != len(mat_2[0]):
        raise ValueError("Matrices must have the same dimensions for addition.")
    
    result = []
    for i in range(len(mat_1)):
        row = []
        for j in range(len(mat_1[0])):
            new_element = mat_1[i][j] + mat_2[i][j]
            row.append(new_element)
        result.append(row)
    return result

def matrix_product(mat_1, mat_2):
    """Multiplies two matrices (mat_1 * mat_2)."""
    if not mat_1 or not mat_2 or len(mat_1[0]) != len(mat_2):
        raise ValueError("Dimension mismatch: mat_1 columns must equal mat_2 rows.")
    
    result = []
    mat_assis = transpose(mat_2) # Transpose mat_2 for easier row-column multiplication
    for i in range(len(mat_1)):
        row = []
        for j in range(len(mat_2[0])):
            new_element = 0
            for k in range(len(mat_1[0])):
                new_element += mat_1[i][k] * mat_assis[j][k]
            row.append(new_element)
        result.append(row)
    return result

def matrix_scalar_product(k, mat):
    """Multiplies a matrix by a scalar k."""
    if not isinstance(mat, list) or not mat or not mat[0]:
        raise ValueError("Invalid matrix provided for scalar multiplication.")
        
    result = []
    for i in range(len(mat)):
        row = []
        for j in range(len(mat[0])):
            new_element = k * mat[i][j]
            row.append(new_element)
        result.append(row)
    return result

def vector_dot_production(vec_1, vec_2):
    if len(vec_1) != len(vec_2) or len(vec_1) == 0:
        raise ValueError("Vectors must be non-empty and have the same length for dot product.")
    ans = 0
    for i in range(len(vec_1)):
        ans += vec_1[i] * vec_2[i]
    return ans

def vector_substitution(vec_1, vec_2):
    if len(vec_1) != len(vec_2) or len(vec_1) == 0:
        raise ValueError("Vectors must be non-empty and have the same length for substitution.")
    vec_res = []
    for i in range(len(vec_1)):
        vec_res.append(vec_1[i] - vec_2[i])
    return vec_res

def vector_scalar_product(k, vec):
    if len(vec) == 0:
        raise ValueError("Vector cannot be empty.")
    result = []
    for i in vec:
        result.append(k * i)
    return result

def Schimidt_Orthogonalization(mat):
    """Performs Gram-Schmidt orthogonalization on the columns of the matrix."""
    if not mat or not mat[0]:
        raise ValueError("Matrix cannot be empty.")
        
    matrix = transpose(mat) # Process columns
    result = []
    for i in range(len(matrix)):
        assist = matrix[i]
        for j in range(i):
            dot_vj_vj = vector_dot_production(result[j], result[j])
            if abs(dot_vj_vj) < 1e-10: # If vector is zero, factor is 0
                factor = 0
            else:
                factor = vector_dot_production(matrix[i], result[j]) / dot_vj_vj
            assist = vector_substitution(assist, vector_scalar_product(factor, result[j]))
        result.append(assist)
    res = transpose(result) # Transpose back
    return res

def congruent_diagonalization(mat):
    """Performs congruent diagonalization (for symmetric matrices)."""
    matrix = copy.deepcopy(mat)
    n = len(matrix)
    if n == 0 or len(matrix[0]) != n:
        raise ValueError("Matrix must be square.")
    
    for k in range(n):
        # Find a non-zero pivot
        pivot_row = k
        while pivot_row < n and abs(matrix[pivot_row][k]) < 1e-10:
            pivot_row += 1
        
        if pivot_row == n: # No pivot
            continue 
            
        if pivot_row != k:
            # Swap row k and pivot_row
            matrix[k], matrix[pivot_row] = matrix[pivot_row], matrix[k]
            # Swap col k and pivot_row
            for i in range(n):
                matrix[i][k], matrix[i][pivot_row] = matrix[i][pivot_row], matrix[i][k]
        
        pivot = matrix[k][k]
        if abs(pivot) < 1e-10:
            continue

        for i in range(k + 1, n):
            if abs(matrix[i][k]) > 1e-10:
                factor = matrix[i][k] / pivot
                # Row operation: R_i = R_i - factor * R_k
                for j in range(k, n):
                    matrix[i][j] -= factor * matrix[k][j]
                # Col operation: C_i = C_i - factor * C_k
                for j in range(k, n): # Note: range can be 0 to n
                    matrix[j][i] -= factor * matrix[j][k]
                    
    return matrix

def solve_homogeneous_system(A):
    if not A or not A[0]:
        return []
    
    R, _ = gaussian_elimination_simplified(A)
    n_rows = len(R)
    n_cols = len(R[0]) if n_rows > 0 else 0
    
    pivot_columns = []
    pivot_rows = [-1] * n_cols
    for i in range(n_rows):
        for j in range(n_cols):
            if abs(R[i][j]) > 1e-10:
                pivot_columns.append(j)
                pivot_rows[j] = i
                break
    
    free_columns = [j for j in range(n_cols) if j not in pivot_columns]
    
    if not free_columns:
        # Only the trivial solution exists
        return [[0.0] * n_cols] 
    
    basis_vectors = []
    for free_col in free_columns:
        x = [0.0] * n_cols
        x[free_col] = 1.0 # Set the free variable
        
        # Solve for pivot variables
        for pivot_col in pivot_columns:
            row = pivot_rows[pivot_col]
            if row != -1:
                x[pivot_col] = -R[row][free_col]
                
        basis_vectors.append(x)
    
    return basis_vectors

def matrix_subtraction(mat_1, mat_2):
    if not mat_1 or not mat_2 or len(mat_1) != len(mat_2) or len(mat_1[0]) != len(mat_2[0]):
        raise ValueError("Matrices must have the same dimensions for subtraction.")
    
    result = []
    for i in range(len(mat_1)):
        row = []
        for j in range(len(mat_1[0])):
            new_element = mat_1[i][j] - mat_2[i][j]
            row.append(new_element)
        result.append(row)
    return result

def identity_matrix(n):
    if n < 0: raise ValueError("Size must be non-negative.")
    matrix = []
    for i in range(n):
        row = [0.0] * n
        row[i] = 1.0
        matrix.append(row)
    return matrix

def matrix_inverse(mat):
    n = len(mat)
    if n == 0 or len(mat[0]) != n:
        raise ValueError("Matrix must be square to find its inverse.")
        
    # Augment matrix A with identity matrix I -> [A | I]
    aug_matrix = copy.deepcopy(mat)
    ident = identity_matrix(n)
    for i in range(n):
        aug_matrix[i].extend(ident[i])
        
    # Compute RREF
    rref_matrix, _ = gaussian_elimination_simplified(aug_matrix)
    
    # Check if left side is I
    for i in range(n):
        if abs(rref_matrix[i][i] - 1.0) > 1e-10:
            raise ValueError("Matrix is singular and cannot be inverted.")
            
    # Extract inverse from the right side
    inverse = []
    for i in range(n):
        inverse.append(rref_matrix[i][n:])
        
    return inverse

def solve_system(A, b):
    n_rows_A = len(A)
    n_cols_A = len(A[0]) if n_rows_A > 0 else 0
    n_rows_b = len(b)
    
    if n_rows_A != n_rows_b:
        raise ValueError("Matrix A and vector b must have the same number of rows.")
    if len(b[0]) != 1:
        raise ValueError("Vector b must be a single column (n x 1 matrix).")

    # Augment matrix A with vector b -> [A | b]
    aug_matrix = copy.deepcopy(A)
    for i in range(n_rows_A):
        aug_matrix[i].append(b[i][0])
        
    # Compute RREF
    R, _ = gaussian_elimination_simplified(aug_matrix)
    
    # Check for consistency (no solution)
    for i in range(n_rows_A):
        is_zero_row = True
        for j in range(n_cols_A):
            if abs(R[i][j]) > 1e-10:
                is_zero_row = False
                break
        if is_zero_row and abs(R[i][n_cols_A]) > 1e-10:
            return "No solution: The system is inconsistent."
            
    # Find pivot/free columns
    pivot_columns = []
    pivot_rows = [-1] * n_cols_A
    for i in range(n_rows_A):
        for j in range(n_cols_A):
            if abs(R[i][j]) > 1e-10:
                pivot_columns.append(j)
                pivot_rows[j] = i
                break
                
    free_columns = [j for j in range(n_cols_A) if j not in pivot_columns]
    
    # Get particular solution (xp)
    xp = [0.0] * n_cols_A
    for pivot_col in pivot_columns:
        row = pivot_rows[pivot_col]
        if row != -1:
            xp[pivot_col] = R[row][n_cols_A] # Value from the augmented column
            
    # Get homogeneous solution (null space)
    if not free_columns:
        # Unique solution
        return f"Unique Solution (xp):\n{format_matrix([xp])}"
    else:
        # Infinitely many solutions
        xh_basis = solve_homogeneous_system(A)
        result_str = f"Particular Solution (xp):\n{format_matrix([xp])}\n\n"
        result_str += f"Basis for Null Space (xh):\n{format_matrix(xh_basis)}"
        result_str += "\n\n(General solution is x = xp + xh)"
        return result_str


#################################################################
### 2. GUI APPLICATION (tkinter)
#################################################################

class MatrixCalculatorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Linear Algebra Calculator")
        self.geometry("800x600")

        # Configure main layout
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=3)
        self.grid_columnconfigure(1, weight=2)
        
        # --- Input Frames ---
        input_frame = ttk.Frame(self, padding="10")
        input_frame.grid(row=0, column=0, sticky="nsew")
        input_frame.grid_rowconfigure(1, weight=1)
        input_frame.grid_rowconfigure(3, weight=1)
        input_frame.grid_columnconfigure(0, weight=1)
        
        ttk.Label(input_frame, text="Matrix A", font=("Arial", 12, "bold")).grid(row=0, column=0, sticky="w", pady=2)
        self.text_A = tk.Text(input_frame, width=40, height=10, font=("Consolas", 10))
        self.text_A.grid(row=1, column=0, sticky="nsew")
        
        ttk.Label(input_frame, text="Matrix B / Vector b (for A*B, A+B, A-B, Ax=b)", font=("Arial", 12, "bold")).grid(row=2, column=0, sticky="w", pady=(10, 2))
        self.text_B = tk.Text(input_frame, width=40, height=10, font=("Consolas", 10))
        self.text_B.grid(row=3, column=0, sticky="nsew")
        
        # --- Output Frame ---
        output_frame = ttk.Frame(self, padding="10")
        output_frame.grid(row=1, column=0, sticky="nsew")
        output_frame.grid_rowconfigure(1, weight=1)
        output_frame.grid_columnconfigure(0, weight=1)

        ttk.Label(output_frame, text="Result", font=("Arial", 12, "bold")).grid(row=0, column=0, sticky="w", pady=2)
        self.text_result = tk.Text(output_frame, width=40, height=10, font=("Consolas", 10))
        self.text_result.grid(row=1, column=0, sticky="nsew")
        
# --- Button Frame ---
        button_frame = ttk.Frame(self, padding="10")
        button_frame.grid(row=0, column=1, rowspan=2, sticky="nsew")
        
        # Unary Operations (Need only A)
        unary_frame = ttk.LabelFrame(button_frame, text="Unary Operations (on Matrix A)")
        unary_frame.pack(fill="x", pady=5)
        
        btn_transpose = ttk.Button(unary_frame, text="Transpose", command=lambda: self.perform_operation('transpose'))
        btn_transpose.pack(fill="x", padx=2, pady=2)
        
        btn_ref = ttk.Button(unary_frame, text="Row Echelon Form (REF)", command=lambda: self.perform_operation('ref'))
        btn_ref.pack(fill="x", padx=2, pady=2)

        btn_rref = ttk.Button(unary_frame, text="Row Reduced Echelon (RREF)", command=lambda: self.perform_operation('rref'))
        btn_rref.pack(fill="x", padx=2, pady=2)

        btn_rank = ttk.Button(unary_frame, text="Rank", command=lambda: self.perform_operation('rank'))
        btn_rank.pack(fill="x", padx=2, pady=2)

        btn_det = ttk.Button(unary_frame, text="Determinant", command=lambda: self.perform_operation('det'))
        btn_det.pack(fill="x", padx=2, pady=2)

        btn_inv = ttk.Button(unary_frame, text="Inverse (A⁻¹)", command=lambda: self.perform_operation('inverse'))
        btn_inv.pack(fill="x", padx=2, pady=2)

        btn_null = ttk.Button(unary_frame, text="Solve Ax = 0 (Null Space)", command=lambda: self.perform_operation('nullspace'))
        btn_null.pack(fill="x", padx=2, pady=2)

        btn_schmidt = ttk.Button(unary_frame, text="Gram-Schmidt (Columns)", command=lambda: self.perform_operation('schmidt'))
        btn_schmidt.pack(fill="x", padx=2, pady=2)

        # Binary Operations (Need A and B)
        binary_frame = ttk.LabelFrame(button_frame, text="Binary Operations")
        binary_frame.pack(fill="x", pady=10)

        btn_add = ttk.Button(binary_frame, text="A + B", command=lambda: self.perform_operation('add'))
        btn_add.pack(fill="x", padx=2, pady=2)

        btn_sub = ttk.Button(binary_frame, text="A - B", command=lambda: self.perform_operation('sub'))
        btn_sub.pack(fill="x", padx=2, pady=2)

        btn_mul = ttk.Button(binary_frame, text="A * B", command=lambda: self.perform_operation('mul'))
        btn_mul.pack(fill="x", padx=2, pady=2)
        
        # System Solver
        system_frame = ttk.LabelFrame(button_frame, text="System Solver")
        system_frame.pack(fill="x", pady=10)
        
        btn_solve = ttk.Button(system_frame, text="Solve Ax = b (use B for 'b')", command=lambda: self.perform_operation('solve_axb'))
        btn_solve.pack(fill="x", padx=2, pady=2)

    def get_matrix(self, text_widget):
        """Parses matrix from a text widget."""
        data = text_widget.get("1.0", tk.END).strip()
        if not data:
            return []
        matrix = []
        try:
            for line in data.split('\n'):
                line_stripped = line.strip()
                if line_stripped:
                    row = [float(val) for val in line_stripped.split()]
                    matrix.append(row)
            
            # Check for rectangular
            if matrix:
                first_row_len = len(matrix[0])
                for row in matrix:
                    if len(row) != first_row_len:
                        raise ValueError("Matrix must be rectangular (all rows same length).")
            return matrix
        except ValueError as e:
            messagebox.showerror("Input Error", f"Invalid matrix format. Ensure all values are numbers.\nError: {e}")
            return None
        except Exception as e:
            messagebox.showerror("Input Error", f"Could not parse matrix: {e}")
            return None

    def format_for_display(self, data):
        """Formats the result (matrix, number, or string) for display."""
        if isinstance(data, (int, float)):
            return str(round(data, 5))
        if isinstance(data, list):
            if not data:
                return "[Empty]"
            # Format matrix
            formatted = format_matrix(data, decimals=5)
            return "\n".join([" ".join(map(str, row)) for row in formatted])
        if isinstance(data, str):
            return data # Already formatted (e.g., from solve_system)
        
        return "Unsupported result type."

    def set_result(self, data):
        """Clears and sets the text in the result box."""
        self.text_result.delete("1.0", tk.END)
        self.text_result.insert(tk.END, self.format_for_display(data))

    def perform_operation(self, op):
        """Main function to handle button clicks."""
        try:
            # Get Matrix A (always needed)
            mat_a = self.get_matrix(self.text_A)
            if mat_a is None: return # Error already shown
            if not mat_a and op not in ['add', 'sub', 'mul']: # Allow empty for binary ops if B is also empty
                 if not mat_a:
                    messagebox.showwarning("Input", "Matrix A is empty.")
                    return

            # Get Matrix B (if needed)
            mat_b = None
            if op in ['add', 'sub', 'mul', 'solve_axb']:
                mat_b = self.get_matrix(self.text_B)
                if mat_b is None: return # Error already shown
                if not mat_b:
                    messagebox.showwarning("Input", "Matrix B is empty.")
                    return
            
            # --- Perform Operation ---
            result = None
            if op == 'transpose':
                result = transpose(mat_a)
            elif op == 'ref':
                result, _ = gaussian_elimination(mat_a)
            elif op == 'rref':
                result, _ = gaussian_elimination_simplified(mat_a)
            elif op == 'rank':
                result = rank_of_matrix(mat_a)
            elif op == 'det':
                # Use REF method, it's more stable than recursive
                ref, counter = gaussian_elimination(mat_a)
                result = det_REF(ref, counter)
            elif op == 'inverse':
                result = matrix_inverse(mat_a)
            elif op == 'nullspace':
                result = solve_homogeneous_system(mat_a)
            elif op == 'schmidt':
                result = Schimidt_Orthogonalization(mat_a)
            elif op == 'add':
                result = matrix_addition(mat_a, mat_b)
            elif op == 'sub':
                result = matrix_subtraction(mat_a, mat_b)
            elif op == 'mul':
                result = matrix_product(mat_a, mat_b)
            elif op == 'solve_axb':
                result = solve_system(mat_a, mat_b)
            
            # --- Display Result ---
            self.set_result(result)

        except ValueError as e:
            messagebox.showerror("Calculation Error", str(e))
        except Exception as e:
            messagebox.showerror("Unhandled Error", f"An unexpected error occurred: {e}")


#################################################################
### 3. HOW TO USE
#################################################################

# To run the calculator:
# 1. Save this entire block of code as a Python file (e.g., matrix_calc.py).
# 2. Run the file from your terminal: python matrix_calc.py
# 3. The GUI window will appear.
#
# Instructions:
# - Type matrices into the text boxes.
# - Use spaces to separate numbers in a row.
# - Use new lines to separate rows.
#
# Example for Matrix A:
# 1 2 3
# 4 5 6
# 7 8 9
#
# Example for Vector b (for Solve Ax=b):
# 1
# 2
# 3

if __name__ == "__main__":
    app = MatrixCalculatorApp()
    app.mainloop()