#include <iostream>
#include <string>
#include <sstream>
#include <vector>

using namespace std;

bool find_duplicate(vector<int> vec) {
	for (int i = 0; i < vec.size(); i++) {
		for (int j = i + 1; j < vec.size(); j++) {
			if (vec[i] == vec[j]) return true;
		}
	}
	return false;
}

int main() {
    string line;
    getline(cin, line);
    stringstream ss(line);
    vector<int> vec;
    int num;
    while (ss >> num) {
        vec.push_back(num);
    }
    cout << (find_duplicate(vec) ? "true" : "false") << endl;
    return 0;
}