#include <iostream>
#include <vector>
#include <string>
#include <stdexcept>
#include <iomanip>

using namespace std;

template <typename T>
class Matrix {
    // I will begin to rewrite the Matrix class, which is originally achived using Python
    // I will try to obtain as much as features, if possible
    // I will also try to improve the performance
    // Let's get started!
private:
    vector<vector<T>> data;
    size_t rows_, cols_;

public:
    Matrix() : rows_(0), cols_(0) {}
    Matrix(size_t r, size_t c) : rows_(r), cols_(c), data(r, vector<T>(c, T{})) {}
    Matrix(initializer_list<initializer_list<T>> il) {
        rows_ = il.size();
        cols_ = il.begin()->size();
        data.reserve(rows_);
        for (const auto& row : il) {
            if (row.size() != cols_)
                throw invalid_argument("All rows must have the same number of columns");
            data.emplace_back(row);
        }
    }

    explicit Matrix(const vector<vector<T>>& mat) {
        if (mat.empty()) {
            rows_ = cols_ = 0;
            return;
        }
        rows_ = mat.size();
        cols_ = mat[0].size();
        for (const auto& row : mat)
            if (row.size() != cols_)
                throw invalid_argument("All rows must have the same number of columns");
        data = mat;
    }

    size_t rows() const { return rows_; }
    size_t cols() const { return cols_; }

    T& operator()(size_t i, size_t j) {
        if (i >= rows_ || j >= cols_)
            throw out_of_range("Matrix index out of bounds");
        return data[i][j];
    }
    const T& operator()(size_t i, size_t j) const {
        if (i >= rows_ || j >= cols_)
            throw out_of_range("Matrix index out of bounds");
        return data[i][j];
    }

    Matrix operator*(const Matrix& rhs) const {
        if (cols_ != rhs.rows_)
            throw invalid_argument("Matrix multiplication dimension mismatch: " +
                to_string(cols_) + " != " + to_string(rhs.rows_));
        Matrix result(rows_, rhs.cols_);
        for (size_t i = 0; i < rows_; ++i)
            for (size_t j = 0; j < rhs.cols_; ++j)
                for (size_t k = 0; k < cols_; ++k)
                    result.data[i][j] += data[i][k] * rhs.data[k][j];
        return result;
    }

    friend ostream& operator<<(ostream& os, const Matrix& m) {
        for (size_t i = 0; i < m.rows_; ++i) {
            for (size_t j = 0; j < m.cols_; ++j)
                os << setw(6) << m.data[i][j] << " ";
            os << '\n';
        }
        return os;
    }
};

int main() {
    try {
        Matrix<int> A = { {1, 2, 3},
                         {4, 5, 6} };
        Matrix<int> B = { {1, 2},
                         {3, 4},
                         {5, 6} };

        cout << "Matrix A:\n" << A << endl;
        cout << "Matrix B:\n" << B << endl;

        Matrix<int> C = A * B;
        cout << "A * B:\n" << C << endl;

        cout << "Attempting D * D (dimension mismatch):\n";
        Matrix<int> D = { {1, 2, 3},
                         {4, 5, 6} };
        Matrix<int> E = D * D;
        cout << E << endl;

    }
    catch (const exception& e) {
        cerr << "ERROR: " << e.what() << endl;
    }

    return 0;
}