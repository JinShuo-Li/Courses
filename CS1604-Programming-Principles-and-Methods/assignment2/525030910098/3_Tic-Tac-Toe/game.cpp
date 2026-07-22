#include "game.h"

#include <iostream>
#include <string>
#include <cmath>

using namespace std;

string encoder(string index) {
    // encodes the 9-digits 3-based index into a single integer code
    int code = 0;
    for (size_t i = 0; i < index.length(); i++) {
        code += (index[i] - '0') * pow(3, index.length() - 1 - i);
    }
    return to_string(code);
}

string decoder(string code) {
    // decodes the integer code back into the 9-digits 3-based index
    int c = stoi(code);
    string index = "";
    for (int i = 0; i < 9; i++) {
        index = to_string(c % 3) + index;
        c /= 3;
    }
    return index;
}

// Remark: all the conversions above are unique. All the I/O types are strings to avoid overflow issues.

int play(int code, int player, int x, int y) {
    int n = 8 - (3 * (x - 1) + (y - 1));
    string code_str = decoder(to_string(code));
    code_str[n] = (player == 1) ? '1' : '2';
    return stoi(encoder(code_str));
}

void print(int code) {
    string code_str = decoder(to_string(code));
    for (int i = 0; i < 9; ++i) {
        if (code_str[i] == '0') code_str[i] = '-';
        if (code_str[i] == '1') code_str[i] = 'X';
        if (code_str[i] == '2') code_str[i] = 'O';
    }
    cout << code_str[8] << " " << code_str[7] << " " << code_str[6] << " \n";
    cout << code_str[5] << " " << code_str[4] << " " << code_str[3] << " \n";
    cout << code_str[2] << " " << code_str[1] << " " << code_str[0] << " ";
}

int check_winner(int code) {
    string code_str = decoder(to_string(code));
    int index = 0;
    while (index < 2) {
        index++;
        char c = index + '0';
        // check rows
        if (code_str[0] == c && code_str[1] == c && code_str[2] == c) return index;
        if (code_str[3] == c && code_str[4] == c && code_str[5] == c) return index;
        if (code_str[6] == c && code_str[7] == c && code_str[8] == c) return index;
        // check columns
        if (code_str[0] == c && code_str[3] == c && code_str[6] == c) return index;
        if (code_str[1] == c && code_str[4] == c && code_str[7] == c) return index;
        if (code_str[2] == c && code_str[5] == c && code_str[8] == c) return index;
        // check diagonals
        if (code_str[0] == c && code_str[4] == c && code_str[8] == c) return index;
        if (code_str[2] == c && code_str[4] == c && code_str[6] == c) return index;
    }
    return 0;
}