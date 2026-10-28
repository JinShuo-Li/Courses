#include <iostream>
#include <string>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;

    if (!(cin >> s)) {
        return 0;
    }

    int len = s.size();
    char* stack = new char[len + 1];
    int top = 0;
    bool valid = true;

    for (int i = 0; i < len; ++i) {
        char c = s[i];

        if (c == '(' || c == '[' || c == '{') {
            stack[top++] = c;
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
