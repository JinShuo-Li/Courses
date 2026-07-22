#include <iostream>
#include <string>
#include <vector>

using namespace std;

bool matchstart(const string& regexp, const string& text);
bool matchstar(char c, const string& regexp, const string& text);

/* match: search for regexp anywhere in text */
bool match(const string& regexp, const string& text) {
    if (regexp[0] == '^') {
        return matchstart(regexp.substr(1), text);
    }
    else {for (size_t i = 0; i <= text.size(); i++) {
        if (matchstart(regexp, text.substr(i))) {
            return true;
        }
    }
    return false;
    }
}

/* matchhere: search for regexp at beginning of text */
bool matchstart(const string& regexp, const string& text) {
    if (regexp.empty()) {
        return true;
    }
    if (regexp.size() > 1 && regexp[1] == '*') {
        return matchstar(regexp[0], regexp.substr(2), text);
    }
    if (regexp[0] == '$' && regexp.size() == 1) {
        return text.empty();
    }
    if (!text.empty() && (regexp[0] == '.' || regexp[0] == text[0])) {
        return matchstart(regexp.substr(1), text.substr(1));
    }
    return false;
}

/* matchstar: search for c*regexp at beginning of text */
bool matchstar(char c, const string& regexp, const string& text) {
    for (size_t i = 0; i <= text.size(); i++) {
        if (matchstart(regexp, text.substr(i))) {
            return true;
        }
        if (i == text.size() || (text[i] != c && c != '.')) {
            break;
        }
    }
    return false;
}

int main() {
    string regexp;
    if (!(cin >> regexp)) return 0;

    int n;
    cin >> n;

    vector<string> texts;
    string text;
    
    for (int i = 0; i < n; ++i) {
        if (cin >> text) {
            texts.push_back(text);
        }
    }

    for (const auto& t : texts) {
        if (match(regexp, t)) {
            cout << "matched" << endl;
        }
        else {
            cout << "unmatched" << endl;
        }
    }
    return 0;
}