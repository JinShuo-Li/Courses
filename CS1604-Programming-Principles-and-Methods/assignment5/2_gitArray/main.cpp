#include "gitArray.h"

#include <iostream>
#include <string>

int main() {
    int length;
    if (!(std::cin >> length)) {
        return 0;
    }

    GitArray history(length);
    std::string command;

    while (std::cin >> command) {
        if (command == "print") {
            std::cout << history.toString() << std::endl;
        } else if (command == "set") {
            int index, value;
            std::cin >> index >> value;
            history.set(index, value);
        } else if (command == "get") {
            int index, version;
            std::cin >> index >> version;
            std::cout << history.get(index, version) << std::endl;
        } else if (command == "undo") {
            history.undo();
        } else if (command == "redo") {
            history.redo();
        } else if (command == "branch") {
            std::string branchName;
            std::cin >> branchName;
            history.branch(branchName);
        } else if (command == "checkout") {
            std::string branchName;
            std::cin >> branchName;
            history.checkout(branchName);
        }
    }

    return 0;
}
