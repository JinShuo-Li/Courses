import copy
import ast
import time
import sys

# CDCL Solver Implementation
class CDCLSolver:
    def __init__(self, num_vars, clauses):
        self.num_vars = num_vars
        self.clauses = [c[:] for c in clauses]
        self.learnt = []
        self.assignment = {}  # var -> bool
        self.decision_level = 0
        self.trail = []       
        self.trail_lim = []   
        self.reason = {}      # var -> clause
        self.level = {}       # var -> int
        self.q_prop = []      

        # Two-watched literals
        # Map: literal_index -> list of clause references
        # lit_index: 2*v if lit>0, 2*v+1 if lit<0
        self.watches = [[] for _ in range(2 * num_vars + 2)]
        
        # VSIDS Heuristic state
        self.activity = [0.0] * (num_vars + 1)
        self.var_inc = 1.0
        self.var_decay = 0.95
        
        self._init_watches()

    def lit_to_int(self, lit):
        v = abs(lit)
        return v * 2 if lit > 0 else v * 2 + 1

    def _init_watches(self):
        for c in self.clauses:
            if len(c) == 0:
                pass 
            elif len(c) == 1:
                self.q_prop.append(c[0])
            else:
                self.watches[self.lit_to_int(c[0])].append(c)
                self.watches[self.lit_to_int(c[1])].append(c)

    def value(self, lit):
        v = abs(lit)
        if v not in self.assignment:
            return None
        return self.assignment[v] if lit > 0 else not self.assignment[v]

    def assign(self, lit, reason=None):
        v = abs(lit)
        if v in self.assignment:
            return
        self.assignment[v] = (lit > 0)
        self.level[v] = self.decision_level
        self.reason[v] = reason
        self.trail.append(lit)
        self.q_prop.append(lit)

    def propagate(self):
        while self.q_prop:
            p = self.q_prop.pop(0)
            false_lit = -p
            idx = self.lit_to_int(false_lit)
            
            original_watches = self.watches[idx]
            self.watches[idx] = []
            
            i = 0
            while i < len(original_watches):
                c = original_watches[i]
                
                if c[0] == false_lit:
                    c[0], c[1] = c[1], c[0]
                
                if self.value(c[0]) is True:
                    self.watches[idx].append(c)
                    i += 1
                    continue
                
                found_new = False
                for k in range(2, len(c)):
                    if self.value(c[k]) is not False:
                        c[1], c[k] = c[k], c[1]
                        self.watches[self.lit_to_int(c[1])].append(c)
                        found_new = True
                        break
                
                if found_new:
                    i += 1
                    continue
                
                self.watches[idx].append(c)
                
                if self.value(c[0]) is False:
                    # Conflict
                    self.watches[idx].extend(original_watches[i+1:])
                    self.q_prop = []
                    return c
                else:
                    self.assign(c[0], c)
                
                i += 1
        return None

    def analyze(self, conflict):
        if self.decision_level == 0:
            return None, -1
            
        learnt = []
        seen = set()
        count = 0 
        
        # Initialize with conflict
        # Calculate count of literals at current level
        for lit in conflict:
            v = abs(lit)
            if v not in seen and self.level.get(v, -1) == self.decision_level:
                seen.add(v)
                count += 1
        
        # Add literals from lower levels to learnt
        for lit in conflict:
            v = abs(lit)
            if self.level.get(v, -1) != self.decision_level:
                learnt.append(lit)
                
        idx = len(self.trail) - 1
        p = None

        while count > 0:
            while True:
                if idx < 0: break 
                p = self.trail[idx]
                idx -= 1
                if abs(p) in seen:
                    break
            
            seen.remove(abs(p))
            count -= 1
            
            if count == 0:
                learnt.append(-p) # Asserting literal
                break
            
            reason = self.reason[abs(p)]
            if reason is None:
                # Should not happen
                break
                
            for lit in reason:
                v = abs(lit)
                if v != abs(p):
                    if v not in seen and self.level.get(v, -1) == self.decision_level:
                        seen.add(v)
                        count += 1
                    elif v not in seen and self.level.get(v, -1) != self.decision_level:
                        if lit not in learnt:
                             learnt.append(lit)

        # Backtrack level
        if len(learnt) == 1:
            bt_level = 0
        else:
            max_lvl = 0
            for lit in learnt[:-1]: # Last one is asserting literal
                lvl = self.level.get(abs(lit), 0)
                if lvl > max_lvl:
                    max_lvl = lvl
            bt_level = max_lvl
            
        return learnt, bt_level

    def pick_branching_variable(self):
        best_v = None
        best_score = -1.0
        
        for v in range(1, self.num_vars + 1):
            if v not in self.assignment:
                score = self.activity[v]
                if score > best_score:
                    best_score = score
                    best_v = v
        return best_v

    def cancel_until(self, level):
        while self.decision_level > level:
            if not self.trail_lim: break
            limit = self.trail_lim.pop()
            for i in range(len(self.trail) - 1, limit - 1, -1):
                lit = self.trail[i]
                v = abs(lit)
                del self.assignment[v]
                del self.level[v]
                del self.reason[v]
            
            del self.trail[limit:]
            self.decision_level -= 1

    def solve(self):
        if self.propagate() is not None:
            return None
            
        while True:
            next_v = self.pick_branching_variable()
            if next_v is None:
                return self.assignment
            
            self.decision_level += 1
            self.trail_lim.append(len(self.trail))
            
            # Simple polarity: True
            self.assign(next_v)
            
            while True:
                conflict = self.propagate()
                if conflict is None:
                    break
                
                if self.decision_level == 0:
                    return None
                
                learnt_clause, bt_level = self.analyze(conflict)
                self.cancel_until(bt_level)
                
                self.learnt.append(learnt_clause)
                
                # Decay
                for lit in learnt_clause:
                    self.activity[abs(lit)] += self.var_inc
                self.var_inc *= (1 / self.var_decay)
                if self.var_inc > 1e100:
                    self.var_inc *= 1e-100
                    for i in range(len(self.activity)):
                        self.activity[i] *= 1e-100
                
                if len(learnt_clause) > 0:
                    p = learnt_clause[-1]
                    if len(learnt_clause) > 1:
                        # Swap asserting literal to index 0 for watching
                        learnt_clause[0], learnt_clause[-1] = learnt_clause[-1], learnt_clause[0]
                        self.watches[self.lit_to_int(learnt_clause[0])].append(learnt_clause)
                        self.watches[self.lit_to_int(learnt_clause[1])].append(learnt_clause)
                    
                    self.assign(p, learnt_clause)

class Sudoku:
    def __init__(self, board=None):
        if board is not None:
            self.board = board
        else:
            raise ValueError("The board should be a nested list")
    
    def flatten(self):
        flat_board = [[0 for _ in range(9)] for _ in range(9)]
        for i in range(9):
            for j in range(9):
                s, t = i%3, j%3
                m, n = i//3, j//3
                flat_board[i][j] = self.board[m][n][s][t]
        return flat_board
    
    def getitem(self,i,j):
        s, t = i%3, j%3
        m, n = i//3, j//3
        return self.board[m][n][s][t]

    def initialize(self):
        return copy.deepcopy(self.board)
    
    def solve(self):
        clauses = []
        def var(r, c, v): return r * 81 + c * 9 + v
        
        # 1. Each cell at least one value
        for r in range(9):
            for c in range(9):
                clauses.append([var(r, c, v) for v in range(1, 10)])
        
        # 2. Each cell at most one value
        for r in range(9):
            for c in range(9):
                for v1 in range(1, 10):
                    for v2 in range(v1+1, 10):
                        clauses.append([-var(r,c,v1), -var(r,c,v2)])

        # 3. Row, Col, Block uniqueness
        for v in range(1, 10):
            # Row
            for r in range(9):
                for c1 in range(9):
                    for c2 in range(c1+1, 9):
                        clauses.append([-var(r, c1, v), -var(r, c2, v)])
            # Col
            for c in range(9):
                for r1 in range(9):
                    for r2 in range(r1+1, 9):
                        clauses.append([-var(r1, c, v), -var(r2, c, v)])
            
            # Block
            for br in range(3):
                for bc in range(3):
                    cells = []
                    for i in range(3):
                        for j in range(3):
                            cells.append((br*3+i, bc*3+j))
                    for k1 in range(9):
                        for k2 in range(k1+1, 9):
                             r1, c1 = cells[k1]
                             r2, c2 = cells[k2]
                             clauses.append([-var(r1, c1, v), -var(r2, c2, v)])

        # Pre-assigned
        flat = self.flatten()
        for r in range(9):
            for c in range(9):
                if flat[r][c] != 0:
                    clauses.append([var(r, c, flat[r][c])])

        # 2. Solve
        solver = CDCLSolver(729, clauses)
        res = solver.solve()
        
        if res:
             for r in range(9):
                for c in range(9):
                    for v in range(1, 10):
                        idx = var(r, c, v)
                        if res.get(idx, False):
                            m, n = r // 3, c // 3
                            s, t = r % 3, c % 3
                            self.board[m][n][s][t] = v
             return True
        return False

def parse_input(input_str):
    try:
        grid = ast.literal_eval(input_str)

        if not isinstance(grid, list):
            raise ValueError("Input must be a list")

        if len(grid) == 9 and all(len(row) == 9 for row in grid):
            board_4d = [[[[0 for _ in range(3)] for _ in range(3)] for _ in range(3)] for _ in range(3)]
            for r in range(9):
                for c in range(9):
                    val = grid[r][c]
                    m, n = r // 3, c // 3
                    s, t = r % 3, c % 3
                    board_4d[m][n][s][t] = val
            return board_4d

        elif len(grid) == 3 and all(len(row) == 3 for row in grid):
            return grid
        else:
            raise ValueError("Input must be a 9x9 grid or a 3x3x3x3 block structure")
            
    except Exception as e:
        print(f"Error parsing input: {e}")
        return None

def print_board(sudoku):
    flat = sudoku.flatten()
    print("-" * 25)
    for i, row in enumerate(flat):
        line = ""
        if i > 0 and i % 3 == 0:
            print("-" * 25)
        for j, val in enumerate(row):
            if j > 0 and j % 3 == 0:
                line += " | "
            line += str(val) + " " if val != 0 else ". "
        print(line)
    print("-" * 25)

if __name__ == "__main__":
    print("Please enter the Sudoku board as a nested list (9x9 2D list or 3x3x3x3 4D list):")
    try:
        user_input = input()
        board_data = parse_input(user_input)
        
        if board_data:
            game = Sudoku(board_data)
            print("\nInitial Board:")
            print_board(game)
            
            print("\\nSolving using CDCL...")
            start_t = time.time()
            if game.solve():
                end_t = time.time()
                print(f"\\nSolved Board (Time: {end_t - start_t:.4f}s):")
                print_board(game)
            else:
                print("\\nNo solution found.")
    except Exception as e:
        print(f"An error occurred: {e}")
