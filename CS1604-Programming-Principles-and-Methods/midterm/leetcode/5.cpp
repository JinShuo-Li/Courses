#include <iostream>
#include <string>
#include <sstream>
#include <vector>

using namespace std;

bool find_duplicate(vector<int> vec, int k) {
    bool is_duplicate = false;
    bool is_in_distance = false;
	for (int i = 0; i < vec.size(); i++) {
		for (int j = i + 1; j < vec.size(); j++) {
            if (vec[i] == vec[j]) {
                is_duplicate = true;
                if (abs(i - j) <= k) {
                    is_in_distance = true;
                }
            }
		}
	}
    if (is_duplicate && is_in_distance) return true;
    else return false;
}

int main() {
    string line;
    getline(cin, line);
    string k_str;
    cin >> k_str;
    int k = stoi(k_str);
    stringstream ss(line);
    vector<int> vec;
    int num;
    while (ss >> num) {
        vec.push_back(num);
    }
    cout << (find_duplicate(vec, k) ? "true" : "false") << endl;
    return 0;
}