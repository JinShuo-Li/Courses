#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
    string str;
    cin >> str;

    vector<string> all_rules;
    string command;
    while (cin >> command) {
        all_rules.push_back(command);
    }

    cout << str << endl;
    size_t index = 0;
    while (index < all_rules.size()) {
        string rule = all_rules[index];
        size_t pos = rule.find("=");
        string replacee = rule.substr(0, pos);
        string replacer = rule.substr(pos + 1);
        size_t found = str.find(replacee);
        if (found != string::npos) {
            str.replace(found, replacee.length(), replacer);
            index = 0;
            cout << str << endl;
        } else {
            index++;
        }
    }
    return 0;
}