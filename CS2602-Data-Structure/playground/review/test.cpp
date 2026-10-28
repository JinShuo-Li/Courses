#include <iostream>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long W;
    cin >> n >> W;

    long long* t = new long long[n + 1];
    long long* r = new long long[n + 1];

    for (int i = 1; i <= n; ++i) {
        cin >> t[i];
    }

    int left = 1;

    for (int i = 1; i <= n; ++i) {
        while (t[left] < t[i] - W) {
            ++left;
        }

        r[i] = i - left + 1;
    }

    for (int i = 1; i <= n; ++i) {
        cout << r[i] << '\n';
    }

    delete[] t;
    delete[] r;

    return 0;
}
