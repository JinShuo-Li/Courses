#include <iostream>
#include <string>
#include <cmath>

using namespace std;

string add_digit(string str) {
	if (str.size() <= 1) return str;
	int number = stoi(str);
	int sum = 0;
	int num = 0;
	for (int i = str.size(); i > 0; i--) {
		num = number/(pow(10, i-1));
		sum += num;
		number -= num * (pow(10, i-1));
	}
	return add_digit(to_string(sum));
}

int main() {
	string inp;
	cin >> inp;
	cout << add_digit(inp) << endl;
}