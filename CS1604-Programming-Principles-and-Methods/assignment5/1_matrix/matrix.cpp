#include "matrix.h"

#include <sstream>

Matrix::Matrix() : rowNum(1), colNum(1), data(1, std::vector<int>(1, 0)), errorCode(NoError) {
}

Matrix::Matrix(int rowNum, int colNum) : rowNum(rowNum), colNum(colNum), errorCode(NoError) {
    if (rowNum <= 0 || colNum <= 0) {
        this->rowNum = 0;
        this->colNum = 0;
        this->data.clear();
        this->errorCode = InvalidDimension;
    } else {
        this->data.assign(rowNum, std::vector<int>(colNum, 0));
    }
}

void Matrix::set(int row, int col, int value) {
    if (row < 0 || row >= rowNum || col < 0 || col >= colNum) {
        errorCode = IndexOutOfRange;
        return;
    }

    data[row][col] = value;
    errorCode = NoError;
}

int Matrix::get(int row, int col) {
    if (row < 0 || row >= rowNum || col < 0 || col >= colNum) {
        errorCode = IndexOutOfRange;
        return -1;
    }

    errorCode = NoError;
    return data[row][col];
}

Matrix Matrix::add(const Matrix& other) const {
    if (rowNum != other.rowNum || colNum != other.colNum) {
        Matrix result;
        result.errorCode = DimensionMismatch;
        return result;
    }

    Matrix result(rowNum, colNum);
    for (int i = 0; i < rowNum; ++i) {
        for (int j = 0; j < colNum; ++j) {
            result.data[i][j] = data[i][j] + other.data[i][j];
        }
    }
    result.errorCode = NoError;
    return result;
}

Matrix Matrix::mul(const Matrix& other) const {
    if (colNum != other.rowNum) {
        Matrix result;
        result.errorCode = DimensionMismatch;
        return result;
    }

    Matrix result(rowNum, other.colNum);
    for (int i = 0; i < rowNum; ++i) {
        for (int j = 0; j < other.colNum; ++j) {
            int sum = 0;
            for (int k = 0; k < colNum; ++k) {
                sum += data[i][k] * other.data[k][j];
            }
            result.data[i][j] = sum;
        }
    }
    result.errorCode = NoError;
    return result;
}

std::string Matrix::toString() const {
    std::ostringstream oss;
    for (int i = 0; i < rowNum; ++i) {
        for (int j = 0; j < colNum; ++j) {
            if (j > 0) {
                oss << ' ';
            }
            oss << data[i][j];
        }
        if (i + 1 < rowNum) {
            oss << '\n';
        }
    }
    return oss.str();
}

ErrorCode Matrix::getErrorCode() const {
    return errorCode;
}

Matrix operator+(const Matrix& lhs, const Matrix& rhs) {
    return lhs.add(rhs);
}

Matrix operator*(const Matrix& lhs, const Matrix& rhs) {
    return lhs.mul(rhs);
}

std::ostream& operator<<(std::ostream& os, const Matrix& matrix) {
    os << matrix.toString();
    return os;
}

void printErrorCode(ErrorCode code) {
    switch (code) {
        case NoError:
            std::cout << "No Error" << std::endl;
            break;
        case IndexOutOfRange:
            std::cout << "Index out of Range" << std::endl;
            break;
        case DimensionMismatch:
            std::cout << "Dimension Mismatch" << std::endl;
            break;
        case InvalidDimension:
            std::cout << "Invalid Dimension" << std::endl;
            break;
    }
}
