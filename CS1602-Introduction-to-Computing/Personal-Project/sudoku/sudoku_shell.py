import copy
import ast

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

if __name__ == "__main__":
    print("Please enter the Sudoku board as a nested list (9x9 2D list or 3x3x3x3 4D list):")
    try:
        user_input = input()
        board_data = parse_input(user_input)
        
        if board_data:
            game = Sudoku(board_data)
            print("\nInitial Board:")
            print_board(game)
            
            print("\nSolving...")
            if game.solve():
                print("\nSolved Board:")
                print_board(game)
            else:
                print("\nNo solution found.")
    except Exception as e:
        print(f"An error occurred: {e}")
