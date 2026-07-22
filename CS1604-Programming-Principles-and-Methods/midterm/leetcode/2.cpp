#include <iostream>
#include <vector>
#include <string>

using namespace std;

vector<int> find_primes(int n) {
	vector<int> record;
	int i = 2;
	bool is_prime = true;
	while (i < n) {
		for (int j = 2; j < i; j++) {
			if (i % j == 0) {
				is_prime = false;
				break;
			}
		}
		if (is_prime) {
			record.push_back(i);
		}
		is_prime = true;
		i++;
	}
	return record;
}

int main() {
	string n_str;
	cin >> n_str;
	int n = stoi(n_str);
	vector<int> rec = find_primes(n);
	cout << rec.size() << endl;
	for (int i = 0; i < rec.size()-1; i++) {
		cout << rec[i] << " ";
	}
	cout << rec[rec.size() - 1] << endl;
	return 0;
}