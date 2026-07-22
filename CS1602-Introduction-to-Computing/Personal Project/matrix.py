import random
import copy
from fractions import Fraction

#Matrix Class
class Matrix:
	def __init__(self, data=None, dim=None, init_value=0):
		if data == None and dim == None:
			raise ValueError("1-1: Lack enough variables")
		if data is not None:
			if not isinstance(data,list):
				raise TypeError("1-2: The data should be a nested list")
			else:
				for i in range(len(data)):
					if i == 0:
						if not isinstance(data[i],list):
							raise TypeError("1-3: All the elements in 'data' should be a list")
						else:
							continue
					else:
						if (not isinstance(data[i],list)) or (len(data[i]) != len(data[i-1])):
							raise TypeError("1-4: All the elements in 'data' should be a list and they must have the same lenth to be a matrix")
						else:
							continue
					
			if len(data) == 0:
				self.data = []
				self.dim = (0,0)
				self.init_value = init_value
			else:
				row_num = len(data)
				col_num = len(data[0])
				dim = (row_num,col_num)
		else:
			if not isinstance(dim,tuple):
				raise TypeError("1-5: The variable 'dim' should be a tuple")
			if len(dim) != 2:
				raise ValueError("1-6: The tuple 'dim' should contains two elements")
			m,n = dim
			if not (isinstance(m,int) and isinstance(n,int)):
				raise TypeError("1-7: The elements in 'dim' should be integers")
			data = [[init_value for _ in range(n)] for _ in range(m)]
		
		self.data = data
		self.dim = dim
		self.init_value = init_value

		

	def shape(self):
		'''
		Return the shape of class matrix
		'''
		if not isinstance(self,Matrix):
			raise TypeError("2-1: Only Matrix objects have shape")
		return self.dim

	def reshape(self, newdim):
		"""
		Reshape the matrix, input a tuple with two elements
		"""
		if not isinstance(newdim,tuple):
			raise TypeError("3-1: The variable 'newdim' should be a tuple")
		elif len(newdim) != 2:
			raise ValueError("3-2: The lenth of the tuple 'newdim' must be 2")
		elif not isinstance(self, Matrix):
			raise TypeError("3-3: Only Matrix objects can be reshaped")
		else:
			pass

		m,n = self.dim
		init_total = m*n
		s,t = newdim
		target_total = s*t

		if init_total != target_total:
			raise ValueError("3-4: You can't change the size of the matrix")
		if init_total == 0:
			return Matrix(data=[])
				
		flated_lst = []
		for i in range(len(self.data)):
			for j in range(len(self.data[0])):
				flated_lst.append(self.data[i][j])
		
		index = 0
		res = []

		for i in range(s):
			row = []
			for j in range(t):
				row.append(flated_lst[index])
				index += 1
			res.append(row)
		
		return Matrix(data=res)

	def T(self):
		"""
		Transpose The matrix
		"""
		if not isinstance(self,Matrix):
			raise TypeError("5-1: Only Matrix objects can be transposed")
		res = []
		for i in range(len(self.data[0])):
			new_row = []
			for j in range(len(self.data)):
				new_row.append(self.data[j][i])
			res.append(new_row)
		return Matrix(res)

	def sum(self, axis=None): 
		"""
		Sum the matrix:
		axis = 0: sum by column
		axis = 1: sum by row
		axis = None: sum the matrix
		"""
		if axis not in {0,1,None}:
			raise ValueError("6-1: The variable 'axis' should be 0, 1, or None")
		if len(self.data) == 0 or len(self.data[0]) == 0:
			raise ValueError("6-2: We do not accept empty matrix and list")
		
		if axis == None:
			sum = 0
			for i in self.data:
				for j in i:
					sum += j
			res = [[sum]]

		if axis == 0:
			res = []
			for m in range(len(self.data[0])):
				sum = 0
				for n in range(len(self.data)):
					sum += self.data[n][m]
				res.append(sum)
			res = [res]
			
		if axis == 1:
			res = []
			for s in range(len(self.data)):
				sum = 0
				for t in range(len(self.data[0])):
					sum += self.data[s][t]
				res.append([sum])

		return Matrix(res)

	def copy(self):
		"""
		Deepcopy the matrix (The out put is another Matrix class)
		"""
		if not isinstance(self, Matrix):
			raise TypeError("7-1: We only copy the Matrix objects")
		return Matrix(data=copy.deepcopy(self.data))
	
	def Kronecker_product(self, other):
		"""
		Calculate the Kronecke product
		"""
		if not isinstance(self, Matrix) or not isinstance(other, Matrix):
			raise TypeError("8-1: Self and other should belong to the class 'Matrix'")
            
		m1, n1 = self.dim
		m2, n2 = other.dim
        
		result_data = [[0] * (n1 * n2) for _ in range(m1 * m2)]
        
		for i in range(m1):
			for j in range(n1):
				for p in range(m2):
					for q in range(n2):
						row_idx = i * m2 + p
						col_idx = j * n2 + q
						result_data[row_idx][col_idx] = self.data[i][j] * other.data[p][q]
        
		return Matrix(data=result_data)
	
	def __getitem__(self, key):
		"""
		Get elements or matrix from the Matrix object
		For example: x = Matrix(data = mat)
		Acceptable input: (x[int,int])/(x[int,slice])/(x[slice,int])/(x[slice,slice])
		Here the only acceptable step value is int(1).
		"""
		if not isinstance(key, tuple):
			raise TypeError("9-1: The variable 'key' should be a tuple")
		
		if len(key) != 2:
			raise TypeError("9-2: The tuple 'key' should contains two elements")
		
		row_key, col_key = key
		n, m = self.dim
		
		if isinstance(row_key, int):
			if row_key < 0 or row_key >= n:
				raise IndexError("9-3: The index shound be in range(n)")
			row_start = row_key
			row_end = row_key + 1
			row_step = 1
			single_row = True
		elif isinstance(row_key, slice):
			start = row_key.start if row_key.start is not None else 0
			stop = row_key.stop if row_key.stop is not None else n
			step = row_key.step if row_key.step is not None else 1
			
			if start < 0:
				start = n + start
			if stop < 0:
				stop = n + stop
			
			row_start = max(0, min(start, n))
			row_end = max(0, min(stop, n))
			row_step = step
			single_row = False
		else:
			raise TypeError("9-4: The index in key should be integer or slice")
		
		if isinstance(col_key, int):
			if col_key < 0 or col_key >= m:
				raise IndexError("9-5: The index shound be in range(m)")
			col_start = col_key
			col_end = col_key + 1
			col_step = 1
			single_col = True
		elif isinstance(col_key, slice):
			start = col_key.start if col_key.start is not None else 0
			stop = col_key.stop if col_key.stop is not None else m
			step = col_key.stop if col_key.step is not None else 1

			if start < 0:
				start = m + start
			if stop < 0:
				stop = m + stop

			col_start = max(0, min(start, m))
			col_end = max(0, min(stop, m))
			col_step = step
			single_col = False
		else:
			raise TypeError("9-6: The index in key should be integer or slice")

		if single_row and single_col:
			return self.data[row_start][col_start]
		
		result_data = []
		i = row_start
		while (row_step > 0 and i < row_end) or (row_step < 0 and i > row_end):
			row = []
			j = col_start
			while (col_step > 0 and j < col_end) or (col_step < 0 and j > col_end):
				row.append(self.data[i][j])
				j += col_step
			
			result_data.append(row)
			i += row_step

		if len(result_data) == 0:
			return Matrix(data = [[]])

		return Matrix(data=result_data)

	def __setitem__(self, key, value):
		"""
		Set elements or matrix for the Matrix object
		For example: x = Matrix(data = mat)
		Acceptable input: (x[int,int]=k)/(x[int,slice]=Matrix)/(x[slice,int]=Matrix)/(x[slice,slice]=Matrix)
		Here the only acceptable step value is int(1).
		We will return nothing but only change the elements in the matrix.
		"""
		if not isinstance(key, tuple):
			raise TypeError("10-1: The variable 'key' should be a tuple")
		
		if len(key) != 2:
			raise TypeError("10-2: The tuple 'key' should contains two elements")
		
		row_key, col_key = key
		n, m = self.dim
		
		if isinstance(row_key, int):
			if row_key < 0 or row_key >= n:
				raise IndexError("10-3: The index shound be in range(n)")
			row_start = row_key
			row_end = row_key + 1
			row_step = 1
			single_row = True
		elif isinstance(row_key, slice):
			start = row_key.start if row_key.start is not None else 0
			stop = row_key.stop if row_key.stop is not None else n
			step = row_key.step if row_key.step is not None else 1
			
			if start < 0:
				start = n + start
			if stop < 0:
				stop = n + stop
			
			row_start = max(0, min(start, n))
			row_end = max(0, min(stop, n))
			row_step = step
			single_row = False
		else:
			raise TypeError("10-4: The index in key should be integer or slice")
		
		if isinstance(col_key, int):
			if col_key < 0 or col_key >= m:
				raise IndexError("10-5: The index shound be in range(m)")
			col_start = col_key
			col_end = col_key + 1
			col_step = 1
			single_col = True
		elif isinstance(col_key, slice):
			start = col_key.start if col_key.start is not None else 0
			stop = col_key.stop if col_key.stop is not None else m
			step = col_key.stop if col_key.stop is not None else 1

			if start < 0:
				start = m + start
			if stop < 0:
				stop = m + stop

			col_start = max(0, min(start, m))
			col_end = max(0, min(stop, m))
			col_step = step
			single_col = False
		else:
			raise TypeError("10-6: The index in key should be integer or slice")

		if single_row and single_col:
			if not isinstance(value,int):
				raise TypeError("10-7: The variable 'value' should be a integer in such condition")
			self.data[row_start][col_start] = value
			return
		
		i = row_start
		if not isinstance(value,Matrix):
			raise TypeError("10-8: The variable 'value' should be a Matrix in such condition")
		while (row_step > 0 and i < row_end) or (row_step < 0 and i > row_end):
			j = col_start
			while (col_step > 0 and j < col_end) or (col_step < 0 and j > col_end):
				self.data[i][j] = value.data[i-row_start][j-col_start]
				j += col_step
			i += row_step
		return

	def __mul__(self,other):
		"""
		Matrix multiplication (dot multiplication), input two objects that belong to class 'Matrix'
		"""
		if not (isinstance(self,Matrix) and isinstance(other,Matrix)):
			raise TypeError("4-1: Self and other should be Matrix obects")
		if len(self.data) == 0 or len(other.data) == 0 or len(self.data[0]) == 0 or len(other.data[0]) == 0:
			raise ValueError("4-2: We do not accept empty matrix and list")
		if len(self.data[0]) != len(other.data):
			raise TypeError("4-3: These two matrix can't be multiplied")
		
		new_self = self.data
		new_other = (other.T()).data
		width = len(new_self[0])
		
		res = []
		for i in range(len(new_self)):
			new_row = []
			for j in range(len(new_other)):
				new_ele = 0
				for k in range(width):
					new_ele += new_self[i][k] * new_other[j][k]
				new_row.append(new_ele)
			res.append(new_row)
		
		return Matrix(data=res)

	def __pow__(self, n):
		"""
		Return the Matrix object of the power of self. Mind that we have redefined the operator for class Matrix
		For example: x = Matrix(data=mat), x**n
		"""
		if not isinstance(n,int):
			raise TypeError("11-1: Exponent must be an integer")
		if not isinstance(self,Matrix):
			raise TypeError("11-2: Only Matrix objects can be exponentiated")
		if len(self.data) == 0 or len(self.data[0]) == 0:
			raise ValueError("11-3: We do not accept empty matrix and list")
		if len(self.data) != len(self.data[0]):
			return ValueError("11-4: Only square matrix can be exponentiated")
		
		res = Matrix(data=self.data)
		for _ in range(n-1):
			res = res*self
			res = Matrix(data = res.data)
		return res

	def __add__(self, other):
		"""
		Add two Matrix objects. And return a Matrix object.
		Mind that we have redefined the operator.
		"""
		if (not isinstance(self,Matrix)) or (not isinstance(other,Matrix)):
			raise TypeError("12-1: Only Matrix objects can be added")
		if len(self.data) == 0 or len(self.data[0]) == 0 or len(other.data) == 0 or len(other.data[0]) == 0:
			raise ValueError("12-2: Empty matrices cannot be added")
		if len(self.data) != len(other.data) or len(self.data[0]) != len(other.data[0]):
			raise ValueError("12-3: Matrix dimensions do not match for addition")
		
		res = []
		for i in range(len(self.data)):
			row = []
			for j in range(len(self.data[0])):
				row.append(self.data[i][j]+other.data[i][j])
			res.append(row)
		
		return Matrix(data=res)

	def __sub__(self, other):
		"""
		Subtract two Matrix objects. And return a Matrix object.
		Mind that we have redefined the operator.
		"""
		if (not isinstance(self,Matrix)) or (not isinstance(other,Matrix)):
			raise TypeError("13-1: Only Matrix objects can be subtracted")
		if len(self.data) == 0 or len(self.data[0]) == 0 or len(other.data) == 0 or len(other.data[0]) == 0:
			raise ValueError("13-2: Empty matrices cannot be subtracted")
		if len(self.data) != len(other.data) or len(self.data[0]) != len(other.data[0]):
			raise ValueError("13-3: Matrix dimensions do not match for subtraction")
		
		res = []
		for i in range(len(self.data)):
			row = []
			for j in range(len(self.data[0])):
				row.append(self.data[i][j]-other.data[i][j])
			res.append(row)
		
		return Matrix(data=res)

	def __len__(self):
		"""
		Measure the number of elements in the Matrix
		Return an integer.
		"""
		if not isinstance(self,Matrix):
			raise TypeError("15-1: Length can only be calculated for Matrix objects")
		m,n = self.dim
		return m*n

	def __str__(self):
		"""
		Formatted the matrix into a form that is reader friendly
		"""
		if not isinstance(self,Matrix):
			raise TypeError("16-1: Only Matrix objects can be converted to string")
		if len(self.data) == 0 or len(self.data[0]) == 0:
			raise ValueError("16-2: Empty matrix cannot be converted to string")
		
		max_lenth = 0
		for i in range(len(self.data)):
			for j in range(len(self.data[0])):
				if len(str(self.data[i][j])) > max_lenth:
					max_lenth = len(str(self.data[i][j]))
		
		matrix = self.data
		lines = []
		for row in matrix:
			row_str = "[" + " ".join(f"{num:{max_lenth}}" for num in row) + "]"
			lines.append(row_str)
		
		result = "[" + lines[0]
		for line in lines[1:]:
			result += "\n" + line
		result += "]"

		return result

	def det(self):
		"""
		Calculate the determinant of the Matrix.
		Return an integer.
		"""
		def gaussian_elimination(mat):
			'''
			Simplified gaussian elimination method.
			Return the REF and an index indicating the power of (-1) when calculating the determinant.
			'''
			matrix = copy.deepcopy(mat)
			matrix = [[Fraction(x) for x in row] for row in matrix]
			n = len(matrix)
			m = len(matrix[0])
			index = 0
			counter = 0
			for j in range(m):
				if index >= n:
					break
				t = index
				while t < n and matrix[t][j] == 0:
					t += 1
				if t == n:
					continue
				else:
					if index != t:
						counter += 1
					matrix[index], matrix[t] = matrix[t], matrix[index]
					factor = matrix[index][j]
					for row in range(index+1,n):
						if matrix[row][j] == 0:
							continue
						else:
							multiplier = matrix[row][j] / factor
							for col in range(j,m):
								matrix[row][col] = matrix[row][col] - multiplier * matrix[index][col]
				index += 1
			return matrix, counter
		def det_REF(mat, counter):
			m = len(mat)
			n = len(mat[0])
			result = 1
			if m != n:
				raise ValueError
			else:
				for i in range(m):
					result *= mat[i][i]
			result = result * ((-1)**(counter))
			return result
		
		if not isinstance(self, Matrix):
			raise TypeError("17-1: Determinant can only be calculated for Matrix objects")
		m,n = gaussian_elimination(self.data)
		res = det_REF(m,n)
		if res.denominator == 1:
			result = res.numerator
		else:
			result = float(res)
		return result

	def inverse(self):
		r"""
		Inverse the matrix and return a Matrix object.
		"""
		def gaussian_elimination_simplified(mat):
			matrix = copy.deepcopy(mat)
			matrix = [[Fraction(x) for x in row] for row in matrix]

			n = len(matrix)
			m = len(matrix[0])
			index = 0
			counter = 0
			
			for j in range(m):
				if index >= n:
					break
				t = index
				while t < n and matrix[t][j] == 0:
					t += 1
				if t == n:
					continue
				else:
					if index != t:
						counter += 1
					matrix[index], matrix[t] = matrix[t], matrix[index]
					
					pivot = matrix[index][j]
					if pivot != 0:
						for col in range(j, m):
							matrix[index][col] = matrix[index][col] / pivot
					
					for row in range(n):
						if row == index:
							continue
						if matrix[row][j] != 0:
							multiplier = matrix[row][j]
							for col in range(j, m):
								matrix[row][col] = matrix[row][col] - multiplier * matrix[index][col]
					
					index += 1
			return matrix, counter
		
		if len(self.data) == 0 or len(self.data[0]) == 0:
			raise ValueError("18-1: Empty matrix has no inverse")
		if len(self.data) != len(self.data[0]):
			raise ValueError("18-2: Only square matrices have inverses")
		if self.det() == 0:
			raise TypeError("18-3: Matrix is singular (determinant is zero)")
		
		matrix = copy.deepcopy(self.data)
		for i in range(len(matrix)):
			new_part = [0 for _ in range(len(matrix))]
			new_part[i] = 1
			matrix[i] = matrix[i] + new_part
		
		res,_ = gaussian_elimination_simplified(matrix)
		res_assis = Matrix(data=res)
		n = len(matrix)
		inverse_data = (res_assis[:,n:]).data
		for i in range(len(inverse_data)):
			for j in range(len(inverse_data[0])):
				if inverse_data[i][j].denominator == 1:
					inverse_data[i][j] = inverse_data[i][j].numerator
				else:
					inverse_data[i][j] = float(inverse_data[i][j])
		result = Matrix(data=inverse_data)
		return result

	def rank(self):
		"""
		Calculate the rank of the Matrix object
		"""
		if not isinstance(self, Matrix):
			raise TypeError("19-1: Rank can only be calculated for Matrix objects")

		n, m = self.dim
		if n == 0 or m == 0:
			return 0

		matrix = copy.deepcopy(self.data)
		matrix = [[Fraction(x) for x in row] for row in matrix]

		rank = 0
		for col in range(m):
			pivot_row = None
			for row in range(rank, n):
				if matrix[row][col] != 0:
					pivot_row = row
					break
			if pivot_row is None:
				continue
			if pivot_row != rank:
				matrix[rank], matrix[pivot_row] = matrix[pivot_row], matrix[rank]
			
			pivot = matrix[rank][col]
			if pivot != 0:
				for j in range(col, m):
					matrix[rank][j] /= pivot
			
			for i in range(rank + 1, n):
				if matrix[i][col] != 0:
					factor = matrix[i][col]
					for j in range(col, m):
						matrix[i][j] -= matrix[rank][j] * factor
			rank += 1

			if rank == min(n, m):
				break
		
		return rank

def I(n):
	'''
	return an n*n unit matrix
	'''
	if not isinstance(n,int) or n <= 0:
		raise ValueError("20-1: Dimension must be a positive integer")
	data = [[0 for _ in range(n)] for _ in range(n)]
	for i in range(n):
		data[i][i] = 1
	
	return Matrix(data=data)

def narray(dim, init_value=1):
	"""
	Return a matrix with dim = dim, initial value = init_value
	"""
	return Matrix(dim=dim, init_value=init_value)

def arange(start, end, step):
	"""
	Return a (1*t) matrix object
	"""
	if not isinstance(start, (int, float)) or not isinstance(end, (int, float)) or not isinstance(step, (int, float)):
		raise TypeError("22-1: Parameters must be integers or floats")
    
	if step == 0:
		raise ValueError("22-2: Step cannot be zero")
    
	if (end - start) * step <= 0:
		return Matrix(data=[[]])
    
	data = []
	current = start
	while (step > 0 and current < end) or (step < 0 and current > end):
		data.append(current)
		current += step
    
	return Matrix(data=[data])

def zeros(dim):
	"""
	Generate a matrix with apointed shape, all the elements are int(0).
	"""
	return narray(dim,0)

def zeros_like(matrix):
	"""
	Generate a matrix with the same shape of 'matrix', but all the elements in the matrix is 0
	"""
	if not isinstance(matrix, Matrix):
		raise TypeError("24-1: Argument must be a Matrix object")
	
	return zeros(matrix.dim)

def ones(dim):
	"""
	Generate a matrix with apointed shape, all the elements are int(1).
	"""
	return narray(dim,1)

def ones_like(matrix):
	"""
	Generate a matrix with the same shape of 'matrix', but all the elements in the matrix is 1
	"""
	if not isinstance(matrix, Matrix):
		raise TypeError("26-1: Argument must be a Matrix object")
	
	return ones(matrix.dim)

def nrandom(dim):
	"""
	Generate a matrix with apointed shape, all the elements are randomly generated.
	"""
	if not isinstance(dim,tuple):
		raise TypeError("27-1: Dimension must be a tuple")
	if len(dim) != 2:
		raise TypeError("27-2: Dimension tuple must have 2 elements")
	
	m,n = dim
	if m <= 0 or n <= 0:
		raise ValueError("27-3: Dimensions must be positive integers")
	
	res = [[random.random() for _ in range(n)] for _ in range(m)]
	return Matrix(data=res)

def nrandom_like(matrix):
	"""
	Generate a matrix with the same shape of 'matrix', but all the elements in the matrix is randomly generated.
	"""
	if not isinstance(matrix, Matrix):
		raise TypeError("28-1: Argument must be a Matrix object")
	
	return nrandom(matrix.dim)

def concatenate(items, axis=0):
	"""
	Concatenate the Matrix objects in items, according to the axis.
	Mind that items can be list, tuple, even set.
	"""
	items = list(items)
	if len(items) == 0:
		raise ValueError("29-1: No matrices to concatenate")
    
	for item in items:
		if not isinstance(item, Matrix):
			raise TypeError("29-2: All items must be Matrix objects")
    
	if axis == 0:
		cols = items[0].dim[1]
		for item in items:
			if item.dim[1] != cols:
				raise ValueError("29-3: All matrices must have the same number of columns for axis=0 concatenation")
        
		result_data = []
		for item in items:
			result_data.extend(item.data)
        
		return Matrix(data=result_data)
    
	elif axis == 1:
		rows = items[0].dim[0]
		for item in items:
			if item.dim[0] != rows:
				raise ValueError("29-4: All matrices must have the same number of rows for axis=1 concatenation")
        
		result_data = []
		for i in range(rows):
			row = []
			for item in items:
				row.extend(item.data[i])
			result_data.append(row)
        
		return Matrix(data=result_data)

	else:
		raise ValueError("29-5: Axis must be 0 or 1")

def vectorize(func):
	"""
	Make func appliable to all the elements in the matrix.
	Return a new function.
	"""
	def f(x):
		if not isinstance(x,Matrix):
			raise TypeError("30-1: Argument must be a Matrix object")
		data = x.data
		result_data = []
		for row in data:
			new_row = []
			for element in row:
				new_row.append(func(element))
			result_data.append(new_row)
		return Matrix(data = result_data)
	return f

if __name__ == "__main__":
	print("This is a module for Matrix operations. Please import it to use its functions and classes.")
	quit()