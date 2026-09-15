import copy
import ast
import tkinter as tk
from tkinter import ttk

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
    
    def generate_candidate(self):
        candidates = [[0 for _ in range(9)] for _ in range(9)]
        for i in range(9):
            for j in range(9):
                checklst, res = [True for _ in range(9)], []
                for s in range(9):
                    if self.getitem(s,j) != 0:
                        checklst[self.getitem(s,j)-1] = False
                for t in range(9):
                    if self.getitem(i,t) != 0:
                        checklst[self.getitem(i,t)-1] = False
                m, n = i//3, j//3
                block = self.board[m][n]
                for index in range(9):
                    if block[index//3][index%3] != 0:
                        checklst[block[index//3][index%3]-1] = False
                for k in range(9):
                    if checklst[k] == True:
                        res.append(k+1)
                candidates[i][j] = res
        return candidates
    
    def initialize(self):
        return copy.deepcopy(self.board)
    
    def solve(self):
        def backtrack(sudoku):
            flat_board = sudoku.flatten()
            candidates = sudoku.generate_candidate()
            min_len, min_i, min_j = 10, -1, -1
            for i in range(9):
                for j in range(9):
                    if flat_board[i][j] == 0:
                        if len(candidates[i][j]) < min_len:
                            min_len = len(candidates[i][j])
                            min_i, min_j = i, j
            if min_len == 10:
                return True
            for candidate in candidates[min_i][min_j]:
                m, n = min_i//3, min_j//3
                s, t = min_i%3, min_j%3
                sudoku.board[m][n][s][t] = candidate
                if backtrack(sudoku):
                    return True
                sudoku.board[m][n][s][t] = 0
            return False
        
        sudoku_copy = Sudoku(self.initialize())
        if backtrack(sudoku_copy):
            self.board = sudoku_copy.board
            return True
        else:
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

class Visualization:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("The Sudoku Solver")
        self.root.geometry("800x600")
        self.root.resizable(True,True)
        self.style = ttk.Style()
        self.style.configure('calm')
        self.setup_variables()
        self.create_widgets()
        self.bind_events()
    
    def setup_variables(self):
        self.entries = {}

    def create_widgets(self):
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)

        title = ttk.Label(main_frame, text="Sudoku Solver", font=("Helvetica", 16, "bold"))
        title.pack(pady=(0, 20))

        grid_frame = tk.Frame(main_frame, bg="gray")
        grid_frame.pack()

        for br in range(3):
            for bc in range(3):
                block_frame = tk.Frame(grid_frame, bd=1, highlightbackground="black", highlightthickness=1)
                block_frame.grid(row=br, column=bc, padx=1, pady=1)
                
                for sr in range(3):
                    for sc in range(3):
                        r, c = br*3 + sr, bc*3 + sc
                        vcmd = (self.root.register(self.validate_input), '%P')
                        e = tk.Entry(block_frame, width=3, font=("Helvetica", 14), justify="center",
                                     validate="key", validatecommand=vcmd)
                        e.grid(row=sr, column=sc, padx=1, pady=1)
                        self.entries[(r, c)] = e

        controls = ttk.Frame(main_frame, padding="20")
        controls.pack()

        self.solve_btn = ttk.Button(controls, text="Solve")
        self.solve_btn.pack(side=tk.LEFT, padx=10)

        self.clear_btn = ttk.Button(controls, text="Clear")
        self.clear_btn.pack(side=tk.LEFT, padx=10)

        self.status_label = ttk.Label(main_frame, text="Ready", foreground="blue")
        self.status_label.pack(pady=5)

    def validate_input(self, new_value):
        if new_value == "": return True
        if new_value.isdigit() and 1 <= int(new_value) <= 9 and len(new_value) == 1:
            return True
        return False

    def bind_events(self):
        self.solve_btn.config(command=self.on_solve)
        self.clear_btn.config(command=self.on_clear)

    def on_solve(self):
        board_4d = [[[[0]*3 for _ in range(3)] for _ in range(3)] for _ in range(3)]
        try:
            for r in range(9):
                for c in range(9):
                    val = self.entries[(r, c)].get()
                    if val:
                        m, n = r // 3, c // 3
                        s, t = r % 3, c % 3
                        board_4d[m][n][s][t] = int(val)
            
            self.status_label.config(text="Solving...", foreground="blue")
            self.root.update()

            game = Sudoku(board_4d)
            if game.solve():
                result = game.flatten()
                self.update_ui(result)
                self.status_label.config(text="Solved!", foreground="green")
            else:
                self.status_label.config(text="No solution found.", foreground="red")
        except Exception as e:
            self.status_label.config(text=f"Error: {e}", foreground="red")

    def on_clear(self):
        for e in self.entries.values():
            e.delete(0, tk.END)
        self.status_label.config(text="Ready", foreground="blue")

    def update_ui(self, flat_board):
        for r in range(9):
            for c in range(9):
                e = self.entries[(r, c)]
                e.delete(0, tk.END)
                if flat_board[r][c] != 0:
                    e.insert(0, str(flat_board[r][c]))

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = Visualization()
    app.run()
