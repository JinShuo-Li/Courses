#include <iostream>
#include <vector>

using namespace std;

bool deter_pow_two(int n) {
	vector<int> vec;
	vec.push_back(1);
	int curr = 1;
	while (vec[vec.size()-1] < n) {
		vec.push_back(curr * 2);
		curr *= 2;
	}
	if (n == vec[vec.size() - 1]) return true;
	else return false;
}

int main() {
	for (int i = 1; i <= 100; i++) {
		cout << i << ". " << (deter_pow_two(i) ? "true" : "false") << endl;
	}
	return 0;
}