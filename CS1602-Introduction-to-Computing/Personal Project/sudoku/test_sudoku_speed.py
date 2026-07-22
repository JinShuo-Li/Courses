import time
import sudoku_shell
import sudoku_optim
import copy

# Example Sudoku (Hard)
# https://abcnews.go.com/blogs/headlines/2012/06/can-you-solve-the-hardest-ever-sudoku
# 800000000003600000070090200050007000000045700000100030001000068008500010090000400
sample_grid = [
    [8,0,0,0,0,0,0,0,0],
    [0,0,3,6,0,0,0,0,0],
    [0,7,0,0,9,0,2,0,0],
    [0,5,0,0,0,7,0,0,0],
    [0,0,0,0,4,5,7,0,0],
    [0,0,0,1,0,0,0,3,0],
    [0,0,1,0,0,0,0,6,8],
    [0,0,8,5,0,0,0,1,0],
    [0,9,0,0,0,0,4,0,0]
]

def convert_to_4d(grid):
    board_4d = [[[[0 for _ in range(3)] for _ in range(3)] for _ in range(3)] for _ in range(3)]
    for r in range(9):
        for c in range(9):
            val = grid[r][c]
            m, n = r // 3, c // 3
            s, t = r % 3, c % 3
            board_4d[m][n][s][t] = val
    return board_4d

def benchmark():
    board_4d_1 = convert_to_4d(sample_grid)
    board_4d_2 = convert_to_4d(sample_grid)

    print("Starting benchmark...")
    
    print("-" * 30)
    print("Running Sudoku_shell (Backtracking)...")
    start = time.time()
    try:
        s1 = sudoku_shell.Sudoku(board_4d_1)
        if s1.solve():
            print(f"Sudoku_shell solved in {time.time() - start:.4f}s")
        else:
            print("Sudoku_shell failed to solve")
    except Exception as e:
         print(f"Sudoku_shell error: {e}")

    print("-" * 30)
    print("Running Sudoku_optim (CDCL)...")
    start = time.time()
    try:
        s2 = sudoku_optim.Sudoku(board_4d_2)
        if s2.solve():
            print(f"Sudoku_optim (CDCL) solved in {time.time() - start:.4f}s")
        else:
            print("Sudoku_optim failed to solve")
    except Exception as e:
        print(f"Sudoku_optim error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    benchmark()
