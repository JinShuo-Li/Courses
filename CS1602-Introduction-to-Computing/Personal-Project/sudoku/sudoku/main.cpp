#include <iostream>
#include <vector>
#include <algorithm>
#include <memory>
#include <cstring>
#include <string>
#include <sstream>
#include <cctype>

class Sudoku {
private:
    int board[9][9];
    std::vector<int> candidates[9][9];

public:
    // initiate
    Sudoku(int input[9][9]) {
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                board[i][j] = input[i][j];
            }
        }
    }

    // initiate from the board
    Sudoku(const std::vector<std::vector<int>>& input) {
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                board[i][j] = input[i][j];
            }
        }
    }

    // deepcopy
    Sudoku(const Sudoku& other) {
        std::memcpy(board, other.board, sizeof(board));
    }

    // printboard
    void printBoard() const {
        std::cout << "-------------------------" << std::endl;
        for (int i = 0; i < 9; i++) {
            if (i > 0 && i % 3 == 0) {
                std::cout << "-------------------------" << std::endl;
            }
            for (int j = 0; j < 9; j++) {
                if (j > 0 && j % 3 == 0) {
                    std::cout << " | ";
                }
                if (board[i][j] == 0) {
                    std::cout << ". ";
                }
                else {
                    std::cout << board[i][j] << " ";
                }
            }
            std::cout << std::endl;
        }
        std::cout << "-------------------------" << std::endl;
    }

    // get value function
    int getValue(int i, int j) const {
        return board[i][j];
    }

    // set value function
    void setValue(int i, int j, int value) {
        board[i][j] = value;
    }

    // generate candicate
    void generateCandidates() {
        // clear candidate
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                candidates[i][j].clear();
            }
        }

        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                if (board[i][j] != 0) {
                    continue;
                }

                bool check[9] = { true, true, true, true, true, true, true, true, true };

                for (int col = 0; col < 9; col++) {
                    int val = board[i][col];
                    if (val != 0) {
                        check[val - 1] = false;
                    }
                }

                for (int row = 0; row < 9; row++) {
                    int val = board[row][j];
                    if (val != 0) {
                        check[val - 1] = false;
                    }
                }

                int blockRow = i / 3;
                int blockCol = j / 3;
                for (int r = blockRow * 3; r < blockRow * 3 + 3; r++) {
                    for (int c = blockCol * 3; c < blockCol * 3 + 3; c++) {
                        int val = board[r][c];
                        if (val != 0) {
                            check[val - 1] = false;
                        }
                    }
                }

                for (int k = 0; k < 9; k++) {
                    if (check[k]) {
                        candidates[i][j].push_back(k + 1);
                    }
                }
            }
        }
    }

    bool findEmptyCellWithMinCandidates(int& minRow, int& minCol, int& minCount) const {
        minCount = 10;
        minRow = -1;
        minCol = -1;

        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                if (board[i][j] == 0) {
                    int count = candidates[i][j].size();
                    if (count < minCount) {
                        minCount = count;
                        minRow = i;
                        minCol = j;
                    }
                }
            }
        }

        return (minRow != -1 && minCol != -1);
    }

    bool backtrack() {
        generateCandidates();

        int minRow, minCol, minCount;
        if (!findEmptyCellWithMinCandidates(minRow, minCol, minCount)) {
            return true;
        }

        for (int candidate : candidates[minRow][minCol]) {
            board[minRow][minCol] = candidate;

            if (backtrack()) {
                return true;
            }

            board[minRow][minCol] = 0;
        }

        return false;
    }

    // main function
    bool solve() {
        Sudoku copy(*this);
        if (copy.backtrack()) {
            std::memcpy(board, copy.board, sizeof(board));
            return true;
        }
        return false;
    }


    bool isValid() const {
        for (int i = 0; i < 9; i++) {
            bool seen[9] = { false };
            for (int j = 0; j < 9; j++) {
                if (board[i][j] != 0) {
                    if (seen[board[i][j] - 1]) {
                        return false;
                    }
                    seen[board[i][j] - 1] = true;
                }
            }
        }

        for (int j = 0; j < 9; j++) {
            bool seen[9] = { false };
            for (int i = 0; i < 9; i++) {
                if (board[i][j] != 0) {
                    if (seen[board[i][j] - 1]) {
                        return false;
                    }
                    seen[board[i][j] - 1] = true;
                }
            }
        }

        for (int blockRow = 0; blockRow < 3; blockRow++) {
            for (int blockCol = 0; blockCol < 3; blockCol++) {
                bool seen[9] = { false };
                for (int i = blockRow * 3; i < blockRow * 3 + 3; i++) {
                    for (int j = blockCol * 3; j < blockCol * 3 + 3; j++) {
                        if (board[i][j] != 0) {
                            if (seen[board[i][j] - 1]) {
                                return false;
                            }
                            seen[board[i][j] - 1] = true;
                        }
                    }
                }
            }
        }

        return true;
    }
};

// interactive main
static bool parse_embedded_numbers(const std::string& s, std::vector<int>& out) {
    out.clear();
    for (size_t i = 0; i < s.size(); ++i) {
        char c = s[i];
        if (c == '.') {
            out.push_back(0);
        } else if (std::isdigit(static_cast<unsigned char>(c))) {
            out.push_back(c - '0');
        }
    }
    return out.size() == 81;
}

static bool read_full_paste_mode(std::vector<std::vector<int>>& grid) {
    std::cout << "Paste the board (you can paste a Python-style list or any text containing 81 digits/dots):\n";
    std::string line, all;
    while (true) {
        if (!std::getline(std::cin, line)) break;
        if (line.empty()) break;
        all += line;
    }
    std::vector<int> nums;
    if (!parse_embedded_numbers(all, nums)) {
        std::cout << "Failed to parse 81 numbers from input.\n";
        return false;
    }
    grid.assign(9, std::vector<int>(9, 0));
    for (int r = 0; r < 9; ++r) {
        for (int c = 0; c < 9; ++c) {
            grid[r][c] = nums[r * 9 + c];
        }
    }
    return true;
}

static bool read_rows_mode(std::vector<std::vector<int>>& grid) {
    std::cout << "Enter 9 rows, each with 9 entries (use 0 or . for empty), separated by spaces.\n";
    grid.clear();
    for (int i = 0; i < 9; ++i) {
        std::string line;
        std::cout << "Row " << (i + 1) << ": ";
        if (!std::getline(std::cin, line)) return false;
        if (line.empty()) { --i; continue; }
        std::istringstream iss(line);
        std::vector<int> row;
        std::string token;
        while (iss >> token) {
            if (token == ".") row.push_back(0);
            else {
                try {
                    int v = std::stoi(token);
                    if (v < 0 || v > 9) throw std::out_of_range("");
                    row.push_back(v);
                } catch (...) { row.clear(); break; }
            }
        }
        if (row.size() != 9) {
            std::cout << "Each row must contain 9 numbers. Please re-enter this row.\n";
            --i;
            continue;
        }
        grid.push_back(row);
    }
    return grid.size() == 9;
}

static bool read_cells_mode(std::vector<std::vector<int>>& grid) {
    std::cout << "Enter cells as: row col value (1-9 for row/col, 0 for empty). Empty line to finish.\n";
    grid.assign(9, std::vector<int>(9, 0));
    std::string line;
    while (true) {
        std::cout << "Input (or empty to finish): ";
        if (!std::getline(std::cin, line)) break;
        if (line.empty()) break;
        std::istringstream iss(line);
        int r, c, v;
        if (!(iss >> r >> c >> v)) {
            std::cout << "Invalid input, expected three integers.\n";
            continue;
        }
        if (r < 1 || r > 9 || c < 1 || c > 9 || v < 0 || v > 9) {
            std::cout << "Values out of range. Rows/cols: 1-9, value: 0-9.\n";
            continue;
        }
        grid[r-1][c-1] = v;
    }
    return true;
}

int main() {
    std::cout << "Interactive Sudoku solver" << std::endl;
    std::cout << "Choose input mode:\n";
    std::cout << "1) Paste full board (Python list or any text with 81 digits/dots). Finish with an empty line.\n";
    std::cout << "2) Enter 9 rows (each row 9 tokens separated by spaces, use . for empty).\n";
    std::cout << "3) Enter cells one by one (r c v), empty line to finish.\n";
    std::cout << "Select mode (1/2/3): ";
    std::string mode;
    if (!std::getline(std::cin, mode)) return 0;
    std::vector<std::vector<int>> puzzle;
    bool ok = false;
    if (mode == "1") {
        ok = read_full_paste_mode(puzzle);
    } else if (mode == "2") {
        ok = read_rows_mode(puzzle);
    } else if (mode == "3") {
        ok = read_cells_mode(puzzle);
    } else {
        std::cout << "Unknown mode. Exiting.\n";
        return 0;
    }

    if (!ok) {
        std::cout << "Failed to read puzzle. Exiting.\n";
        return 0;
    }

    Sudoku sudoku(puzzle);
    std::cout << "\nInitial Sudoku:" << std::endl;
    sudoku.printBoard();

    if (!sudoku.isValid()) {
        std::cout << "\nInvalid Sudoku puzzle." << std::endl;
        return 0;
    }

    std::cout << "\nSolve? (y/n): ";
    std::string ans;
    if (!std::getline(std::cin, ans)) return 0;
    if (ans.empty() || (ans[0] != 'y' && ans[0] != 'Y')) {
        std::cout << "Canceled." << std::endl;
        return 0;
    }

    std::cout << "Solving..." << std::endl;
    if (sudoku.solve()) {
        std::cout << "\nSolved Sudoku:" << std::endl;
        sudoku.printBoard();
    } else {
        std::cout << "\nNo solution found." << std::endl;
    }

    return 0;
}
