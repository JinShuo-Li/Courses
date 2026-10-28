#include <iostream>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    char* stack = new char[64];
    int capacity = 64;
    int top = 0;
    bool valid = true;

    int c;

    while ((c = getchar()) != EOF && c != '\n' && c != '\r' && c != ' ') {
        if (c == '(' || c == '[' || c == '{') {
            if (top == capacity) {
                capacity *= 2;
                char* bigger = new char[capacity];

                for (int i = 0; i < top; ++i) {
                    bigger[i] = stack[i];
                }

                delete[] stack;
                stack = bigger;
            }

            stack[top++] = static_cast<char>(c);
        } else if (c == ')' || c == ']' || c == '}') {
            char need = (c == ')') ? '(' : (c == ']' ? '[' : '{');

            if (top == 0 || stack[top - 1] != need) {
                valid = false;
                break;
            }

            --top;
        }
    }

    if (top != 0) {
        valid = false;
    }

    cout << (valid ? "YES" : "NO") << '\n';

    delete[] stack;

    return 0;
}
