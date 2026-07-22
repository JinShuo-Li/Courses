#include <iostream>
#include <string>

using namespace std;

bool is_anagram(string s, string t) {
	if (s.size() != t.size()) return false;
	size_t length = s.size();
	for (int i = 0; i < length; i++) {
		char current_char = s[i];
		int j = 0;
		while (j <= t.size()) {
			if (j==t.size()) {return false;}
			if (t[j] == current_char) {t.erase(j,1); break;}
			else j++;
		}
	}
	return true;
}

int main() {
	string s,t;
	cin >> s;
	cin >> t;
	if (is_anagram(s,t)) cout << "True" << endl;
    else cout << "False" << endl;
}