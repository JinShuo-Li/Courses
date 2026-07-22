#include <iostream>
#include <vector>
using namespace std;

bool match(int x1, int x2) { return ((x1 + 10) ^ 0xaaa) > ((x2 + 10) ^ 0xaaa); }

int main() {
    int n;
    cin >> n;
    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    int winner = a[0];

    for (int i = 1; i < n; i++) {
        if (match(winner, a[i])) {
            winner = winner;
        }

        else winner = a[i];
    }
    cout << winner << endl;
    return 0;

}