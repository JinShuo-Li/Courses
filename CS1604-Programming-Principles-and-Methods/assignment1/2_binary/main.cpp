#include <iostream>
#include <string>
using namespace std;

int main() {
    long long input;
    string output = "";
    cin >> input;
    
    if (input == 0) {
        output = "0";
    }
    
    while (input != 0) {
        if (input % 2 != 0) {
            output = "1" + output;
        } 
        else {
            output = "0" + output;
        }
        input /= 2;
    }
    
    cout << output << endl;
}