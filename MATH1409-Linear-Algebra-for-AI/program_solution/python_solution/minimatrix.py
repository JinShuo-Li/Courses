import sympy as sp

class Matrix:
    """
    A minimal Matrix class mimicking the custom Matrix implementation, 
    but powered internally by SymPy.
    """
    def __init__(self, data=None, dim=None, init_value=0):
        if data is None and dim is None:
            raise ValueError("1-1: Lack enough variables")
            
        if data is not None:
            if len(data) == 0:
                self.mat = sp.Matrix([])
            else:
                self.mat = sp.Matrix(data)
        else:
            m, n = dim
            self.mat = sp.Matrix(m, n, lambda i, j: init_value)
            
        self.dim = self.mat.shape
        self.data = self.mat.tolist() if self.mat.shape != (0, 0) else []

    def _sync_data(self):
        """Helper to keep self.data synchronized if someone accesses it directly."""
        self.dim = self.mat.shape
        if self.mat.rows == 0 or self.mat.cols == 0:
            self.data = []
        else:
            self.data = self.mat.tolist()

    def shape(self):
        return self.mat.shape

    def reshape(self, newdim):
        s, t = newdim
        reshaped_mat = self.mat.reshape(s, t)
        return Matrix(data=reshaped_mat.tolist())

    def T(self):
        return Matrix(data=self.mat.transpose().tolist())

    def sum(self, axis=None):
        if self.mat.rows == 0 or self.mat.cols == 0:
            raise ValueError("6-2: We do not accept empty matrix and list")
        
        if axis is None:
            return Matrix(data=[[sum(self.mat)]])
        elif axis == 0:
            res = [sum(self.mat[:, i]) for i in range(self.mat.cols)]
            return Matrix(data=[res])
        elif axis == 1:
            res = [[sum(self.mat[i, :])] for i in range(self.mat.rows)]
            return Matrix(data=res)
        else:
            raise ValueError("6-1: The variable 'axis' should be 0, 1, or None")

    def copy(self):
        return Matrix(data=self.mat.tolist())

    def Kronecker_product(self, other):
        if not isinstance(other, Matrix):
            raise TypeError("8-1: Self and other should belong to the class 'Matrix'")
        
        m1, n1 = self.shape()
        m2, n2 = other.shape()
        
        res = sp.zeros(m1 * m2, n1 * n2)
        for i in range(m1):
            for j in range(n1):
                res[i*m2:(i+1)*m2, j*n2:(j+1)*n2] = self.mat[i, j] * other.mat
        return Matrix(data=res.tolist())

    def __getitem__(self, key):
        res = self.mat[key]
        if isinstance(res, sp.MatrixBase):
            if res.rows == 0 or res.cols == 0:
                return Matrix(data=[[]])
            return Matrix(data=res.tolist())
        return res

    def __setitem__(self, key, value):
        if isinstance(value, Matrix):
            self.mat[key] = value.mat
        else:
            self.mat[key] = value
        self._sync_data()

    def __mul__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError("4-1: Self and other should be Matrix obects")
        res = self.mat * other.mat
        return Matrix(data=res.tolist())

    def __pow__(self, n):
        if not isinstance(n, int):
            raise TypeError("11-1: Exponent must be an integer")
        res = self.mat ** n
        return Matrix(data=res.tolist())

    def __add__(self, other):
        if not isinstance(other, Matrix):
             raise TypeError("12-1: Only Matrix objects can be added")
        res = self.mat + other.mat
        return Matrix(data=res.tolist())

    def __sub__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError("13-1: Only Matrix objects can be subtracted")
        res = self.mat - other.mat
        return Matrix(data=res.tolist())

    def __len__(self):
        # Original logic returned m*n
        return len(self.mat)

    def __str__(self):
        if self.mat.rows == 0 or self.mat.cols == 0:
            return "[]"
        
        str_data = [[str(self.mat[i, j]) for j in range(self.mat.cols)] for i in range(self.mat.rows)]
        max_length = max([max([len(s) for s in row]) for row in str_data]) if str_data else 0
        
        lines = []
        for row in str_data:
            row_str = "[" + " ".join(f"{s:>{max_length}}" for s in row) + "]"
            lines.append(row_str)
            
        return "\n".join(lines)

    def det(self):
        return self.mat.det()

    def inverse(self):
        return Matrix(data=self.mat.inv().tolist())

    def rank(self):
        return self.mat.rank()

    def jordan_normal_form(self):
        """
        Uses SymPy's builtin jordan_form method.
        Note: SymPy returns (P, J) where A = P * J * P**-1
        """
        P, J = self.mat.jordan_form()
        return Matrix(data=J.tolist())


def I(n):
    """Return an n*n unit matrix"""
    return Matrix(data=sp.eye(n).tolist())


def concatenate(items, axis=0):
    items = list(items)
    if len(items) == 0:
        raise ValueError("29-1: No matrices to concatenate")
    
    sp_mats = []
    for item in items:
        if not isinstance(item, Matrix):
            raise TypeError("29-2: All items must be Matrix objects")
        sp_mats.append(item.mat)

    if axis == 0:
        res = sp.Matrix.vstack(*sp_mats)
    elif axis == 1:
        res = sp.Matrix.hstack(*sp_mats)
    else:
        raise ValueError("29-5: Axis must be 0 or 1")
    
    return Matrix(data=res.tolist())


if __name__ == "__main__":
    print("\n" + "="*40)
    print("Testing SymPy-based minimatrix.py")
    print("="*40)
    
    A = Matrix(data=[[1, 2], [3, 4]])
    B = Matrix(data=[[2, 0], [1, 2]])
    
    print("\nMatrix A:")
    print(A)
    print("\nMatrix B:")
    print(B)
    
    print("\nA + B:")
    print(A + B)
    
    print("\nA * B:")
    print(A * B)
    
    print("\nDeterminant of A:", A.det())
    print("\nInverse of A:")
    print(A.inverse())
    print("\nRank of A:", A.rank())
    
    print("\n" + "-"*40)
    print("Jordan Normal Form Tests")
    print("-"*40)
    
    # 3x3 Test
    C_data = [[-1, 1, 0], [-4, 3, 0], [1, 0, 2]]
    C = Matrix(data=C_data)
    print("\nMatrix C (3x3):")
    print(C)
    print("Jordan Normal Form of C:")
    print(C.jordan_normal_form())
    
    # 5x5 Test    
    D_data = [
        [2, 1, 0, 0, 1],
        [0, 2, 1, 0, 0],
        [0, 0, 2, 0, 0],
        [0, 0, 0, 2, 1],
        [0, 0, 0, 0, 2]
    ]
    D = Matrix(data=D_data)
    print("\nMatrix D (5x5):")
    print(D)
    print("Jordan Normal Form of D:")
    print(D.jordan_normal_form())

    # 6x6 Test
    E_data = [
        [ 0,  1,  0,  0,  0,  0],
        [-1,  2,  0,  0,  0,  0],
        [ 1,  1,  1,  1,  0,  0],
        [-1, -1,  0,  1,  0,  0],
        [ 0,  0,  0,  0,  2,  1],
        [ 0,  0,  0,  0, -1,  4]
    ]
    E = Matrix(data=E_data)
    print("\nMatrix E (6x6):")
    print(E)
    print("Jordan Normal Form of E:")
    print(E.jordan_normal_form())
