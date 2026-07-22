#include <iostream>
#include <string>
#include <vector>

using namespace std;

bool is_sorted(const vector<int> vec) {
	for (int i = 0; i < vec.size()-1; i++) {
		if (vec[i] < vec[i+1]) continue;
		else return false;
	}
	return true;
}

void swap(int& a, int& b) {
	int temp;
	temp = a;
	a = b;
	b = temp;
}

vector<int> sorting(vector<int> vec) {
	while (! is_sorted(vec)) {
		for (int j = 0; j < vec.size()-1; j++) {
			if (vec[j] > vec[j+1]) swap(vec[j], vec[j+1]);
			else continue;
		}
	}
	return vec;
}

int main() {
	vector<int> nums;
	int x;
	while (cin >> x) {
		nums.push_back(x);
	}

    vector<int> vec = sorting(nums);

	for (int i = 0; i < vec.size(); i++) {
		if (vec[i] != i) {
            cout << i << endl;
            return 0;
        }
		else continue;
	}
	cout << vec.size() << endl;
	return 0;
}