#include <iostream>
#include <vector>
#include <string>
#include "utilities.h"

using namespace std;

void visit_url(vector<string>& backward_record, vector<string>& forward_record, string new_url) {
    backward_record.push_back(new_url);
    forward_record.clear();
}

void backward_dir(vector<string>& backward_record, vector<string>& forward_record) {
    size_t pointer_back = backward_record.size();
    if (pointer_back <= 1) {
        return;
    }
    else {
        string url = backward_record[pointer_back-1];
        backward_record.pop_back();
        forward_record.push_back(url);
    }
}

void forward_dir(vector<string>& backward_record, vector<string>& forward_record) {
    size_t pointer_for = forward_record.size();
    if (pointer_for == 0) {
        return;
    }
    else {
        string url = forward_record[pointer_for-1];
        forward_record.pop_back();
        backward_record.push_back(url);
    }
}

void current(vector<string>& backward_record) {
    size_t pointer = backward_record.size();
    cout << backward_record[pointer-1] << endl;
}

int main() {
    int n;
    if (!(cin >> n)) return 0;
    cin.ignore();

    vector<string> backward_record;
    vector<string> forward_record;

    for (int i = 0; i < n; i++) {
        string line;
        if (!getline(cin, line)) break;
        if (line.empty()) continue;

        if (line.substr(0, 5) == "visit") {
            string url = line.substr(6);
            visit_url(backward_record, forward_record, url);
        } 
        else if (line == "back") {
            backward_dir(backward_record, forward_record);
        } 
        else if (line == "forward") {
            if (!forward_record.empty()) {
                string url = forward_record.back();
                forward_record.pop_back();
                backward_record.push_back(url);
            }
        } 
        else if (line == "current") {
            if (!backward_record.empty()) {
                cout << backward_record.back() << endl;
            }
        }
    }

    return 0;
}