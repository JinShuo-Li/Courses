#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

bool def_happy_num(int n) {
	vector<int> record;
	while (true) {
		string n_str = to_string(n);
		int result = 0;
		for (int i = 0; i < n_str.size(); i++) {
			char c = n_str[i];
			int ever_char = c - '0';
			result += ever_char * ever_char;
		}
		if (find(record.begin(), record.end(), result) != record.end()) { return false; }
		else if (result == 1) { return true; }
		else {
			record.push_back(result);
			n = result;
		}
	}
}

int main() {
	string num;
	cin >> num;
	int num_int = stoi(num);
	if (def_happy_num(num_int)) { cout << "true" << endl; }
	else { cout << "false" << endl; }
	return 0;
}