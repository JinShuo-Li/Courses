#include <iostream>
#include <vector>
#include <string>

using namespace std;

bool matchstring(const vector<char>& str, const vector<char>& sub, const size_t& n) {
	if (str.size() < n + 1 + sub.size()) { return false;}
	for (int i = 0; i < sub.size(); i++) {
		if (sub[i] == str[n + i]) { continue; }
		else { return false; }
	}
	return true;
}

int findString(const vector<char>& str, const vector<char>& sub) {
	int length = str.size();
	for (int i = 0; i < length; i++) {
		if (matchstring(str, sub, i)) { return i; }
		else { continue; }
	}
	return -1;
}

int main() {
	string str, sub;
	vector<char> str_vec, sub_vec;
	getline(cin, str);
	getline(cin, sub);
	for (int i = 0; i < str.size(); i++) {
		str_vec.push_back(str[i]);
	}
	for (int j = 0; j < sub.size(); j++) {
		sub_vec.push_back(sub[j]);
	}
	int n = findString(str_vec, sub_vec);
	cout << "the input string is " << str << endl;
	cout << "the substring to find is " << sub << endl;
	cout << "the result is " << n << "." << endl;
	return 0;
}