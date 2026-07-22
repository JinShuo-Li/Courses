import copy
import ast
import tkinter as tk
from tkinter import ttk
import random

class Sudoku:
    def __init__(self, board=None):
        if board is not None:
            self.board = board
        else:
            self.board = [[[[0 for _ in range(3)] for _ in range(3)] for _ in range(3)] for _ in range(3)]
        self.solution = None 

    def flatten(self):
        flat_board = [[0 for _ in range(9)] for _ in range(9)]
        for i in range(9):
            for j in range(9):
                s, t = i%3, j%3
                m, n = i//3, j//3
                flat_board[i][j] = self.board[m][n][s][t]
        return flat_board
    
    def generate_candidate(self):
        candidates = [[0 for _ in range(9)] for _ in range(9)]
        for i in range(9):
            for j in range(9):
                checklst, res = [True for _ in range(9)], []
                for s in range(9):
                    if self.board[i//3][j//3][s][j%3] != 0: # Fixed indexing logic for candidate check
                        pass # Simplified logic for brevity in this UI fix
                # (Note: Using original logic for robustness)
                candidates[i][j] = list(range(1,10)) # Placeholder for UI focus, full logic in original
        return candidates
    
    # --- Re-inserting the full original logic to ensure game works ---
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
                    if self.getitem(s,j) != 0: checklst[self.getitem(s,j)-1] = False
                for t in range(9):
                    if self.getitem(i,t) != 0: checklst[self.getitem(i,t)-1] = False
                m, n = i//3, j//3
                block = self.board[m][n]
                for index in range(9):
                    if block[index//3][index%3] != 0: checklst[block[index//3][index%3]-1] = False
                for k in range(9):
                    if checklst[k] == True: res.append(k+1)
                candidates[i][j] = res
        return candidates

    def solve(self, randomize=False):
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
            if min_len == 10: return True
            
            current_candidates = candidates[min_i][min_j]
            if randomize: random.shuffle(current_candidates)

            for candidate in current_candidates:
                m, n = min_i//3, min_j//3
                s, t = min_i%3, min_j%3
                sudoku.board[m][n][s][t] = candidate
                if backtrack(sudoku): return True
                sudoku.board[m][n][s][t] = 0
            return False
        
        sudoku_copy = Sudoku(copy.deepcopy(self.board))
        if backtrack(sudoku_copy):
            self.board = sudoku_copy.board
            return True
        return False

    def count_solutions(self, limit=2):
        count = 0
        def backtrack(sudoku):
            nonlocal count
            if count >= limit: return
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
                count += 1
                return
            for candidate in candidates[min_i][min_j]:
                m, n = min_i//3, min_j//3
                s, t = min_i%3, min_j%3
                sudoku.board[m][n][s][t] = candidate
                backtrack(sudoku)
                sudoku.board[m][n][s][t] = 0
                if count >= limit: return

        sudoku_copy = Sudoku(copy.deepcopy(self.board))
        backtrack(sudoku_copy)
        return count

    def generate_puzzle(self, difficulty=45):
        self.board = [[[[0]*3 for _ in range(3)] for _ in range(3)] for _ in range(3)]
        self.solve(randomize=True)
        self.solution = copy.deepcopy(self.board) 
        positions = [(r, c) for r in range(9) for c in range(9)]
        random.shuffle(positions)
        removed_count = 0
        for r, c in positions:
            m, n = r // 3, c // 3
            s, t = r % 3, c % 3
            temp = self.board[m][n][s][t]
            self.board[m][n][s][t] = 0 
            check_game = Sudoku(copy.deepcopy(self.board))
            if check_game.count_solutions() != 1:
                self.board[m][n][s][t] = temp 
            else:
                removed_count += 1
            if removed_count >= difficulty: break
        return True

class Visualization:
    # --- Modern Colors ---
    COLOR_BG = "#FAFAFA"         
    COLOR_GRID = "#2C3E50"       # 深色边框颜色
    COLOR_CELL_BG = "#FFFFFF"    
    COLOR_FIXED_BG = "#ECF0F1"   
    COLOR_TEXT = "#2C3E50"       
    COLOR_USER_TEXT = "#3498DB"  
    COLOR_ERROR_BG = "#FADBD8"   
    FONT_NUM = ("Helvetica", 20)
    FONT_BTN = ("Helvetica", 11, "bold")
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Sudoku Modern")
        self.root.geometry("600x750")
        self.root.configure(bg=self.COLOR_BG)
        self.root.resizable(False, False)
        
        self.game = Sudoku()
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure('TButton', font=self.FONT_BTN, borderwidth=0, 
                             foreground="#FFFFFF", background="#34495E", padding=10)
        self.style.map('TButton', background=[('active', '#2C3E50')])
        
        self.setup_variables()
        self.create_widgets()
        self.bind_events()
    
    def setup_variables(self):
        self.entries = {}
        self.fixed_cells = set() 

    def create_widgets(self):
        # Header
        header_frame = tk.Frame(self.root, bg=self.COLOR_BG)
        header_frame.pack(pady=(20, 10))
        tk.Label(header_frame, text="SUDOKU", font=("Helvetica", 24, "bold"), 
                 bg=self.COLOR_BG, fg=self.COLOR_GRID).pack()
        self.status_label = tk.Label(header_frame, text="Click 'New Game' to start", 
                                     font=("Helvetica", 12), bg=self.COLOR_BG, fg="#7F8C8D")
        self.status_label.pack(pady=5)

        # --- GRID FIX STARTS HERE ---
        # 1. 最外层容器 (背景色 = 网格线颜色)
        board_container = tk.Frame(self.root, bg=self.COLOR_GRID) 
        board_container.pack(pady=10)

        for br in range(3):
            for bc in range(3):
                # 2. 3x3 宫格 Frame
                # padx=2, pady=2 这里的间隙会让 board_container 的深色漏出来，形成【粗线】
                block_frame = tk.Frame(board_container, bg=self.COLOR_GRID)
                block_frame.grid(row=br, column=bc, padx=2, pady=2) 
                
                for sr in range(3):
                    for sc in range(3):
                        r, c = br*3 + sr, bc*3 + sc
                        
                        vcmd = (self.root.register(self.validate_input), '%P')
                        
                        # 3. 单元格输入框
                        e = tk.Entry(block_frame, width=2, font=self.FONT_NUM, justify="center",
                                     bd=0, relief="flat", highlightthickness=0,
                                     validate="key", validatecommand=vcmd)
                        
                        # padx=1, pady=1 这里的间隙会让 block_frame 的深色漏出来，形成【细线】
                        e.grid(row=sr, column=sc, padx=1, pady=1, ipady=8, ipadx=5)
                        
                        self.entries[(r, c)] = e
        # --- GRID FIX ENDS HERE ---

        # Controls
        controls = tk.Frame(self.root, bg=self.COLOR_BG, pady=20)
        controls.pack(fill=tk.X)
        controls.columnconfigure((0,1,2,3), weight=1)

        self.gen_btn = ttk.Button(controls, text="New Game")
        self.gen_btn.grid(row=0, column=0, padx=5)
        self.check_btn = ttk.Button(controls, text="Check")
        self.check_btn.grid(row=0, column=1, padx=5)
        self.solve_btn = ttk.Button(controls, text="Reveal")
        self.solve_btn.grid(row=0, column=2, padx=5)
        self.clear_btn = ttk.Button(controls, text="Clear")
        self.clear_btn.grid(row=0, column=3, padx=5)

    def validate_input(self, new_value):
        if new_value == "": return True
        if new_value.isdigit() and 1 <= int(new_value) <= 9 and len(new_value) == 1: return True
        return False

    def bind_events(self):
        self.gen_btn.config(command=self.on_generate)
        self.check_btn.config(command=self.on_check)
        self.solve_btn.config(command=self.on_reveal)
        self.clear_btn.config(command=self.on_clear)

    def on_generate(self):
        self.status_label.config(text="Generating...", fg="#E67E22")
        self.root.update()
        self.game.generate_puzzle()
        flat_board = self.game.flatten()
        self.fixed_cells.clear()
        for r in range(9):
            for c in range(9):
                e = self.entries[(r, c)]
                e.delete(0, tk.END)
                e.config(state='normal', bg=self.COLOR_CELL_BG)
                val = flat_board[r][c]
                if val != 0:
                    e.insert(0, str(val))
                    e.config(state='readonly', readonlybackground=self.COLOR_FIXED_BG, fg=self.COLOR_TEXT)
                    self.fixed_cells.add((r,c))
                else:
                    e.config(fg=self.COLOR_USER_TEXT, bg=self.COLOR_CELL_BG)
        self.status_label.config(text="Game Started", fg=self.COLOR_TEXT)

    def on_check(self):
        if self.game.solution is None:
            self.status_label.config(text="Generate a game first!", fg="#E74C3C")
            return
        sol_game = Sudoku(self.game.solution)
        flat_sol = sol_game.flatten()
        errors, empty = 0, 0
        for r in range(9):
            for c in range(9):
                if (r,c) in self.fixed_cells: continue
                e = self.entries[(r, c)]
                val = e.get()
                if not val:
                    empty += 1
                    e.config(bg=self.COLOR_CELL_BG)
                elif int(val) != flat_sol[r][c]:
                    errors += 1
                    e.config(bg=self.COLOR_ERROR_BG)
                else:
                    e.config(bg=self.COLOR_CELL_BG)
        if errors == 0 and empty == 0: self.status_label.config(text="PERFECT! Puzzle Solved.", fg="#27AE60")
        elif errors > 0: self.status_label.config(text=f"{errors} errors found.", fg="#C0392B")
        else: self.status_label.config(text="No errors, keep going!", fg="#F39C12")

    def on_reveal(self):
        if self.game.solution is None:
            self.on_solve_manual()
            return
        sol_game = Sudoku(self.game.solution)
        flat_sol = sol_game.flatten()
        for r in range(9):
            for c in range(9):
                e = self.entries[(r, c)]
                if (r,c) not in self.fixed_cells:
                    e.config(state='normal', bg=self.COLOR_CELL_BG)
                    e.delete(0, tk.END)
                    e.insert(0, str(flat_sol[r][c]))
                    e.config(fg="#27AE60")
        self.status_label.config(text="Solution Revealed", fg="#8E44AD")

    def on_solve_manual(self):
        board_4d = [[[[0]*3 for _ in range(3)] for _ in range(3)] for _ in range(3)]
        try:
            for r in range(9):
                for c in range(9):
                    val = self.entries[(r, c)].get()
                    if val:
                        m, n = r // 3, c // 3
                        s, t = r % 3, c % 3
                        board_4d[m][n][s][t] = int(val)
            manual_game = Sudoku(board_4d)
            if manual_game.solve():
                self.update_ui_manual(manual_game.flatten())
                self.status_label.config(text="Solved!", fg="#27AE60")
            else: self.status_label.config(text="No solution found.", fg="#C0392B")
        except: pass

    def on_clear(self):
        self.game = Sudoku()
        self.fixed_cells.clear()
        for e in self.entries.values():
            e.config(state='normal', bg=self.COLOR_CELL_BG, fg=self.COLOR_USER_TEXT)
            e.delete(0, tk.END)
        self.status_label.config(text="Ready", fg=self.COLOR_TEXT)

    def update_ui_manual(self, flat_board):
        for r in range(9):
            for c in range(9):
                e = self.entries[(r, c)]
                e.delete(0, tk.END)
                if flat_board[r][c] != 0: e.insert(0, str(flat_board[r][c]))

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = Visualization()
    app.run()