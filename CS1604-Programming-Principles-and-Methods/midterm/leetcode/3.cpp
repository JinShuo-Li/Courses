#include <iostream>
#include <string>

using namespace std;

bool determine_iso(string str1, string str2) {
	if (str1.size() != str2.size()) return false;
	else {
		for (int i = 0; i < str1.size(); i++) {
			char ele_maj = str1[i];
			char ele_min = str2[i];
			for (int j = i + 1; j < str1.size(); j++) {
				if (str1[j] == ele_maj && str2[j] != ele_min) {
					return false;
				}
			}
		}
		return true;
	}
}

int main() {
	string s, t;
	cin >> s;
	cin >> t;
	if (determine_iso(s, t)) cout << "true" << endl;
	else cout << "false" << endl;
	return 0;
}