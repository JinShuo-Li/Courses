#include <iostream>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long W;
    cin >> n >> W;

    long long* t = new long long[n + 1];

    int left = 1;

    for (int i = 1; i <= n; ++i) {
        cin >> t[i];

        while (t[left] < t[i] - W) {
            ++left;
        }

        cout << i - left + 1 << '\n';
    }

    delete[] t;

    return 0;
}
