#include <iostream>
#include <string>
#include <cctype>

using namespace std;

int main() {
    string answer;
    cin >> answer;

    for (char &c : answer) {
        c = toupper(c);
    }

    for (int i = 0; i < 6; i++) {
        string guess;
        cin >> guess;

        for (char &c : guess) {
            c = toupper(c);
        }

        if (guess == answer) {
            cout << "ggggg" << endl;
            cout << "won" << endl;
            return 0;
        }

        string temp_answer = answer;
        string result = "nnnnn";

        for (int j = 0; j < 5; j++) {
            if (guess[j] == temp_answer[j]) {
                result[j] = 'g';
                temp_answer[j] = '*';
            }
        }

        for (int j = 0; j < 5; j++) {
            if (result[j] != 'g') {
                if (temp_answer.find(guess[j]) != string::npos) {
                    result[j] = 'y';
                }
            }
        }

        cout << result << endl;
    }

    cout << "The answer is " << answer << endl;
    return 0;
}