#ifndef MATRIX_H
#define MATRIX_H

#include <iostream>
#include <string>
#include <vector>

enum ErrorCode {
    NoError,
    IndexOutOfRange,
    DimensionMismatch,
    InvalidDimension
};

class Matrix {
private:
    int rowNum;
    int colNum;
    std::vector<std::vector<int> > data;
    ErrorCode errorCode;

public:
    Matrix();
    Matrix(int rowNum, int colNum);

    void set(int row, int col, int value);
    int get(int row, int col);

    Matrix add(const Matrix& other) const;
    Matrix mul(const Matrix& other) const;

    std::string toString() const;
    ErrorCode getErrorCode() const;

    friend Matrix operator+(const Matrix& lhs, const Matrix& rhs);
    friend Matrix operator*(const Matrix& lhs, const Matrix& rhs);
    friend std::ostream& operator<<(std::ostream& os, const Matrix& matrix);
};

void printErrorCode(ErrorCode code);

#endif
