#include <iostream>
#include <string>

using namespace std;

bool ugly_num(int num) {
	while (num % 2 == 0) {
		num /= 2;
	}
	while (num % 3 == 0) {
		num /= 3;
	}
	while (num % 5 == 0) {
		num /= 5;
	}
	if (num == 1) return true;
	else return false;
}

int main() {
	string inp;
	cin >> inp;
	if (ugly_num(stoi(inp))) cout << "true" << endl;
	else cout << "false" << endl;
	return 0;
}