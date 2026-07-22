#include "matrix.h"

#include <iostream>
#include <map>
#include <string>

int main() {
    std::map<std::string, Matrix> matrices;
    std::string command;

    while (std::cin >> command) {
        if (command == "new") {
            std::string name;
            int row, col;
            std::cin >> name >> row >> col;
            matrices[name] = Matrix(row, col);
        } else if (command == "set") {
            std::string name;
            int row, col, value;
            std::cin >> name >> row >> col >> value;
            matrices[name].set(row, col, value);
        } else if (command == "get") {
            std::string name;
            int row, col;
            std::cin >> name >> row >> col;
            std::cout << matrices[name].get(row, col) << std::endl;
        } else if (command == "add") {
            std::string a, b, c;
            std::cin >> a >> b >> c;
            matrices[c] = matrices[a] + matrices[b];
        } else if (command == "mul") {
            std::string a, b, c;
            std::cin >> a >> b >> c;
            matrices[c] = matrices[a] * matrices[b];
        } else if (command == "print") {
            std::string name;
            std::cin >> name;
            std::cout << matrices[name] << std::endl;
        } else if (command == "error") {
            std::string name;
            std::cin >> name;
            printErrorCode(matrices[name].getErrorCode());
        }
    }

    return 0;
}
