#include <iostream>
#include <string>
using namespace std;

int grader(int num) {
    int index = 5;
    if (num == 42) index = 1;
    else if ((num % 3 == 0) && (num % 6 != 0)) index = 2;
    else if ((num % 2 != 0) && (num % 3 != 0) && (num % 5 == 0)) index = 4;
    return index;
}

int cmp(int num1, int num2) {
    int index1 = grader(num1);
    int index2 = grader(num2);

    if (index1 != index2) {
        return index1 < index2 ? 1 : -1;
    }

    if (num1 == num2) return 0;
    if (num1 % num2 == 0) return 1;
    if (num2 % num1 == 0) return -1;
    return num1 > num2 ? 1 : -1;
}

int main() {
    int num1, num2;
    cin >> num1 >> num2;
    cout << cmp(num1, num2) << endl;
    return 0;
}