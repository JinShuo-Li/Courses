# Modules
import copy

# Matrix Class
class Matrix:
    def __init__(self, data=None, dim=None, init_value=0, directed=False):
        if data == None and dim == None:
            raise ValueError("1-1: Lack enough variables")
        if data is not None:
            if not isinstance(data, list):
                raise TypeError("1-2: The data should be a nested list")
            else:
                for i in range(len(data)):
                    if i == 0:
                        if not isinstance(data[i], list):
                            raise TypeError("1-3: All the elements in 'data' should be a list")
                        else:
                            continue
                    else:
                        if (not isinstance(data[i], list)) or (len(data[i]) != len(data[i-1])):
                            raise TypeError("1-4: All the elements in 'data' should be a list and they must have the same lenth to be a matrix")
                        else:
                            continue
                    
            if len(data) == 0:
                self.data = []
                self.dim = (0, 0)
                self.init_value = init_value
            else:
                row_num = len(data)
                col_num = len(data[0])
                dim = (row_num, col_num)
        else:
            if not isinstance(dim, tuple):
                raise TypeError("1-5: The variable 'dim' should be a tuple")
            if len(dim) != 2:
                raise ValueError("1-6: The tuple 'dim' should contains two elements")
            m, n = dim
            if not (isinstance(m, int) and isinstance(n, int)):
                raise TypeError("1-7: The elements in 'dim' should be integers")
            data = [[init_value for _ in range(n)] for _ in range(m)]
        
        self.data = data
        self.dim = dim
        self.init_value = init_value

    def T(self):
        """
        Transpose The matrix
        """
        if not isinstance(self, Matrix):
            raise TypeError("5-1: Only Matrix objects can be transposed")
        res = []
        for i in range(len(self.data[0])):
            new_row = []
            for j in range(len(self.data)):
                new_row.append(self.data[j][i])
            res.append(new_row)
        return Matrix(res)

    def __pow__(self, n):
        """
        Return the Matrix object of the power of self.
        """
        if not isinstance(n, int):
            raise TypeError("11-1: Exponent must be an integer")
        if not isinstance(self, Matrix):
            raise TypeError("11-2: Only Matrix objects can be exponentiated")
        if len(self.data) == 0 or len(self.data[0]) == 0:
            raise ValueError("11-3: We do not accept empty matrix and list")
        if len(self.data) != len(self.data[0]):
            return ValueError("11-4: Only square matrix can be exponentiated")
        
        res = Matrix(data=self.data)
        for _ in range(n-1):
            res = res * self
            res = Matrix(data=res.data)
        return res

    def __add__(self, other):
        """
        Add two Matrix objects.
        """
        if (not isinstance(self, Matrix)) or (not isinstance(other, Matrix)):
            raise TypeError("12-1: Only Matrix objects can be added")
        if len(self.data) == 0 or len(self.data[0]) == 0 or len(other.data) == 0 or len(other.data[0]) == 0:
            raise ValueError("12-2: Empty matrices cannot be added")
        if len(self.data) != len(other.data) or len(self.data[0]) != len(other.data[0]):
            raise ValueError("12-3: Matrix dimensions do not match for addition")
        
        res = []
        for i in range(len(self.data)):
            row = []
            for j in range(len(self.data[0])):
                row.append(self.data[i][j] + other.data[i][j])
            res.append(row)
        
        return Matrix(data=res)

    def __mul__(self, other):
        """
        'Multiple' two Matrix objects. (Matrix Multiplication)
        """
        if not (isinstance(self, Matrix) and isinstance(other, Matrix)):
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

#Graph Class
class Graph:
    def __init__(self, data=[]):
        """
        Initialize the Graph object.
        
        Checks:
        1. Data is a nested list.
        2. Data is not empty.
        3. Matrix is square (row count == column count).
        """
        if not isinstance(data, list):
            raise TypeError("1-1: The graph should be expressed using an adjacency matrix (nested list)")
        if len(data) == 0:
            raise ValueError("1-2: The graph data shouldn't be empty")
        
        try:
            length = len(data[0])
        except:
            raise TypeError("1-3: The graph data should be a nested list")
            
        if length != len(data):
            raise ValueError("1-4: The adjacency matrix should be square")
            
        for i, row in enumerate(data):
            if not isinstance(row, list):
                raise TypeError("1-5: The graph data should be a nested list")
            if len(row) != length:
                raise ValueError("1-6: Every row of the matrix should have the same number of columns")
        
        self.data = data

    def get_neighbors(self, vertex):
        """
        Return a list of neighbors for the given vertex.
        """
        # Error Code 2-X
        if not isinstance(vertex, int):
            raise TypeError("2-1: Vertex index must be an integer")
        if vertex < 0 or vertex >= len(self.data):
            raise ValueError(f"2-2: Vertex index out of range. Valid range: 0 to {len(self.data)-1}")
            
        neighbors = []
        for i in range(len(self.data[vertex])):
            if self.data[vertex][i] != 0:
                neighbors.append(i)
        return neighbors

    def get_degree(self, vertex):
        """
        Return a tuple (out_degree, in_degree) for the given vertex.
        """
        if not isinstance(vertex, int):
            raise TypeError("3-1: Vertex index must be an integer")
        if vertex < 0 or vertex >= len(self.data):
            raise ValueError(f"3-2: Vertex index out of range. Valid range: 0 to {len(self.data)-1}")
            
        out_degree = 0
        in_degree = 0
        vertices_count = len(self.data)

        for i in range(vertices_count):
            if self.data[vertex][i] != 0:
                out_degree += 1

        for j in range(vertices_count):
            if self.data[j][vertex] != 0:
                in_degree += 1
                
        return (out_degree, in_degree)

    def add_edge(self, start, end, weight=1):
        """
        Add an edge or update weight between start and end vertices.
        """
        vertices_count = len(self.data)
        if not (isinstance(start, int) and isinstance(end, int)):
            raise TypeError("4-1: Vertex indices must be integers")
        if not (0 <= start < vertices_count and 0 <= end < vertices_count):
            raise ValueError(f"4-2: Vertex index out of range. Valid range: 0 to {vertices_count-1}")
        if not isinstance(weight, (int, float)):
            raise TypeError("4-3: Weight must be a number")
            
        self.data[start][end] = weight

    def remove_edge(self, start, end):
        """
        Remove the edge from start to end (set weight to 0).
        """
        vertices_count = len(self.data)
        if not (isinstance(start, int) and isinstance(end, int)):
            raise TypeError("5-1: Vertex indices must be integers")
        if not (0 <= start < vertices_count and 0 <= end < vertices_count):
            raise ValueError(f"5-2: Vertex index out of range. Valid range: 0 to {vertices_count-1}")
            
        self.data[start][end] = 0

    def count_edges(self):
        """
        Return the total number of edges in the graph.
        """
        count = 0
        vertices_count = len(self.data)
        for i in range(vertices_count):
            for j in range(vertices_count):
                if self.data[i][j] != 0:
                    count += 1
        return count

    def is_complete(self):
        """
        Check if the graph is a complete graph.
        """
        vertices_count = len(self.data)
        for i in range(vertices_count):
            for j in range(vertices_count):
                if i != j:
                    if self.data[i][j] == 0:
                        return False
        return True

    def find_shortest_path_CPX(self, start, end):
        """
        Find shortest path using Matrix multiplication (CPX method).
        This method computes A, A^2, A^3... to find connectivity.
        """
        vertices_count = len(self.data)
        if not (isinstance(start, int) and isinstance(end, int)):
            raise TypeError("6-1: Start and End vertices must be integers")
        if not (0 <= start < vertices_count and 0 <= end < vertices_count):
            raise ValueError(f"6-2: Vertex index out of range. Valid range is 0 to {vertices_count - 1}")

        try:
            _ = Matrix([[1]]) 
        except NameError:
            raise NameError("6-3: The 'Matrix' class is not defined. Please import or define the Matrix class before using CPX method.")
        except Exception as e:
            raise RuntimeError(f"6-4: The 'Matrix' class exists but failed to initialize. Error: {str(e)}")
        try:
            _ = self.data[0][0] + 0 
        except TypeError:
             raise ValueError("6-5: Graph data contains non-numeric values, which are incompatible with Matrix multiplication.")

        if start == end:
            return [start]
            
        adj_matrix = Matrix(copy.deepcopy(self.data))
        matrices = [Matrix(copy.deepcopy(self.data))]
        found = False

        for i in range(vertices_count):
            if matrices[-1].data[start][end] != 0:
                found = True
                break
            matrices.append(matrices[-1] * adj_matrix)
        if not found:
            return None
        res = [end]
        for k in range(len(matrices) - 1, 0, -1):
            target = res[-1]
            prev_matrix = matrices[k-1]
            for mid in range(vertices_count):
                if prev_matrix.data[start][mid] != 0 and adj_matrix.data[mid][target] != 0:
                    res.append(mid)
                    break
        res.append(start)
        return res[::-1]

    def find_shortest_path_BFS(self, start, end):
        """
        Find shortest path using Breadth-First Search (unweighted).
        """
        vertices_count = len(self.data)
        if not (isinstance(start, int) and isinstance(end, int)):
            raise TypeError("7-1: Start and End vertices must be integers")
        if not (0 <= start < vertices_count and 0 <= end < vertices_count):
            raise ValueError("7-2: Vertex index out of range")

        queue = [start]
        mat = self.data
        memory = {start: None}
        found = False
        idx = 0

        while idx < len(queue):
            curr = queue[idx]
            if curr == end:
                found = True
                break
            
            for i in range(vertices_count):
                if mat[curr][i] != 0 and i not in memory:
                    memory[i] = curr
                    queue.append(i)
                    if i == end:
                        found = True
                        break
            if found:
                break
            idx += 1
            
        if not found:
            return None
            
        path = []
        index = end
        while index is not None:
            path.append(index)
            index = memory[index]
        return path[::-1]

    def find_path_DFS(self, start, end):
        """
        Find a path using Depth-First Search.
        """
        vertices_count = len(self.data)
        if not (isinstance(start, int) and isinstance(end, int)):
            raise TypeError("8-1: Start and End vertices must be integers")
        if not (0 <= start < vertices_count and 0 <= end < vertices_count):
            raise ValueError("8-2: Vertex index out of range")

        stack = [start]
        mat = self.data
        memory = {start: None}
        found = False
        
        while len(stack) > 0:
            curr = stack.pop()
            if curr == end:
                found = True
                break
            
            for i in range(vertices_count):
                if mat[curr][i] != 0 and i not in memory:
                    memory[i] = curr
                    stack.append(i)
                    
        if not found:
            return None
            
        path = []
        curr_node = end
        while curr_node is not None:
            path.append(curr_node)
            curr_node = memory[curr_node]
        return path[::-1]

    def find_shortest_path_weight(self, start, end):
        """
        Find shortest path using Dijkstra's Algorithm (weighted).
        """
        vertices_count = len(self.data)
        if not (isinstance(start, int) and isinstance(end, int)):
            raise TypeError("9-1: Start and End vertices must be integers")
        if not (0 <= start < vertices_count and 0 <= end < vertices_count):
            raise ValueError("9-2: Vertex index out of range")

        distances = {i: float('inf') for i in range(vertices_count)}
        distances[start] = 0
        visited = [False] * vertices_count
        parent = {start: None}
        
        for _ in range(vertices_count):
            min_dist = float('inf')
            curr = -1
            for i in range(vertices_count):
                if not visited[i] and distances[i] < min_dist:
                    min_dist = distances[i]
                    curr = i
            if curr == -1 or distances[curr] == float('inf'):
                break
            if curr == end:
                break
            visited[curr] = True
            for i in range(vertices_count):
                weight = self.data[curr][i]
                if weight > 0 and not visited[i]:
                    new_dist = distances[curr] + weight
                    if new_dist < distances[i]:
                        distances[i] = new_dist
                        parent[i] = curr
                        
        if end not in parent:
            return None
            
        path = []
        curr_node = end
        while curr_node is not None:
            path.append(curr_node)
            curr_node = parent[curr_node]   
        return path[::-1]

    def minimum_spanning_tree_prim(self, weights):
        """
        Implementation of Prim's algorithm for MST.
        Returns the MST as an adjacency matrix.
        """
        if not isinstance(weights, list):
            raise TypeError("10-1: Weights must be a nested list (matrix)")
        if len(weights) == 0:
            raise ValueError("10-2: Weights matrix cannot be empty")
        if len(weights) != len(weights[0]):
             raise ValueError("10-3: Weights matrix must be square")
        
        n = len(weights)
        INF = float('inf')
        key = [INF] * n
        parent = [None] * n
        mst_set = [False] * n
        key[0] = 0
        parent[0] = -1

        for _ in range(n):
            min_val = INF
            u = -1
            for v in range(n):
                if not mst_set[v] and key[v] < min_val:
                    min_val = key[v]
                    u = v
                    
            if u == -1: 
                break
            mst_set[u] = True
            for v in range(n):
                w = weights[u][v]
                if w > 0 and not mst_set[v] and w < key[v]:
                    key[v] = w
                    parent[v] = u
                    
        mst_matrix = [[0] * n for _ in range(n)]
        for i in range(1, n):
            if parent[i] is not None:
                u, v = parent[i], i
                weight = weights[u][v]
                mst_matrix[u][v] = weight
                mst_matrix[v][u] = weight
        return mst_matrix

    def minimum_spanning_tree_kruskal(self, weights):
        """
        Implementation of Kruskal's algorithm for MST.
        Returns the MST as an adjacency matrix.
        """
        if not isinstance(weights, list):
            raise TypeError("11-1: Weights must be a nested list (matrix)")

        n = len(weights)
        edges = []
        for i in range(n):
            for j in range(i + 1, n):
                if weights[i][j] > 0:
                    edges.append((weights[i][j], i, j))
        edges.sort()
        
        parent = list(range(n))
        
        def find(i):
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])
            return parent[i]
            
        def union(i, j):
            root_i = find(i)
            root_j = find(j)
            if root_i != root_j:
                parent[root_i] = root_j
                return True
            return False
            
        mst_matrix = [[0] * n for _ in range(n)]
        
        for w, u, v in edges:
            if union(u, v):
                mst_matrix[u][v] = w
                mst_matrix[v][u] = w
        return mst_matrix

    def connectness(self):
        """
        Check the connectivity of the graph.
        Return True if connected, False otherwise.
        """
        try:
            mat = Matrix(self.data)
        except NameError:
             raise NameError("12-1: Matrix class is not defined. Cannot compute connectivity.")

        vertices_count = len(mat.data)
        res = Matrix(dim=mat.dim, init_value=0)
        for i in range(1, vertices_count + 1):
            res += mat**i
            
        for j in range(len(mat.data)):
            for k in range(len(mat.data[0])):
                if j == k:
                    continue
                else:
                    if res.data[j][k] == 0:
                        return False
        return True

    def connect_components(self):
        """
        Find connected components in the graph.
        Returns a list of lists, where each sublist contains vertex indices of a component.
        """
        mat = self.data
        vertices_count = len(mat)
        visited = [False for _ in range(vertices_count)]
        res = []
        
        for index in range(vertices_count):
            if not visited[index]:
                component_list = [index]
                in_check = {index}
                idx = 0
                
                while idx < len(component_list):
                    current_vertex = component_list[idx]
                    if not visited[current_vertex]:
                        visited[current_vertex] = True
                        for neighbor in range(vertices_count):
                            if (neighbor != current_vertex and 
                                mat[current_vertex][neighbor] != 0 and 
                                not visited[neighbor] and 
                                neighbor not in in_check):
                                component_list.append(neighbor)
                                in_check.add(neighbor)
                    idx += 1
                res.append(component_list)
        return res

    def is_bipartite_BFS(self):
        """
        Check whether the graph is bipartite using BFS.
        Returns True or False.
        """
        mat = self.data
        vertices_count = len(mat)
        color = {}
        
        for start in range(vertices_count):
            if start not in color:
                color[start] = 0
                queue = [start]
                while queue:
                    u = queue.pop(0)
                    for v in range(vertices_count):
                        if mat[u][v] != 0:
                            if v not in color:
                                color[v] = 1 - color[u]
                                queue.append(v)
                            elif color[v] == color[u]:
                                return False
        return True

if __name__ == '__main__':
    data = [
        [0, 1, 0, 0, 1],
        [1, 0, 1, 0, 1],
        [0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1],
        [1, 1, 0, 1, 0]]
    g = Graph(data)

    print("Neighbors of vertex 1:", g.get_neighbors(1))
    print("Degree of vertex 1:", g.get_degree(1))
    
    print("Edge count:", g.count_edges())
    print("Is complete graph:", g.is_complete())

    g.add_edge(0, 2, 5)
    print("After adding edge (0, 2) with weight 5, value:", g.data[0][2])
    
    g.remove_edge(0, 2)
    print("After removing edge (0, 2), value:", g.data[0][2])

    print("Shortest path CPX (0 to 3):", g.find_shortest_path_CPX(0, 3))
    print("Shortest path BFS (0 to 3):", g.find_shortest_path_BFS(0, 3))
    print("Path DFS (0 to 3):", g.find_path_DFS(0, 3))

    weighted_data = [
        [0, 10, 3, 0],
        [10, 0, 1, 0],
        [3, 1, 0, 5],
        [0, 0, 5, 0]]
    g_weighted = Graph(weighted_data)
    print("Dijkstra shortest path (0 to 1):", g_weighted.find_shortest_path_weight(0, 1))

    print("MST Prim:", g.minimum_spanning_tree_prim(weighted_data))
    print("MST Kruskal:", g.minimum_spanning_tree_kruskal(weighted_data))

    print("Connectivity (Main Graph):", g.connectness())
    
    disconnected_data = [
        [0, 1, 0, 0],
        [1, 0, 0, 0],
        [0, 0, 0, 1],
        [0, 0, 1, 0]]
    g_disconnected = Graph(disconnected_data)
    print("Connectivity (Disconnected Graph):", g_disconnected.connectness())
    print("Connected components:", g_disconnected.connect_components())

    bipartite_data = [
        [0, 1, 0, 1],
        [1, 0, 1, 0],
        [0, 1, 0, 1],
        [1, 0, 1, 0]]
    g_bipartite = Graph(bipartite_data)
    print("Is Bipartite (Cycle 4):", g_bipartite.is_bipartite_BFS())
    print("Is Bipartite (Main Graph):", g.is_bipartite_BFS())