#include <iostream>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    cin >> n >> k;

    int* a = new int[n + 1];

    for (int i = 1; i <= n; ++i) {
        cin >> a[i];
    }

    long long rounds = 0;
    int target = a[k];

    for (int i = 1; i < k; ++i) {
        rounds += (a[i] < target ? a[i] : target);
    }

    rounds += target;

    for (int i = k + 1; i <= n; ++i) {
        int bound = target - 1;
        rounds += (a[i] < bound ? a[i] : bound);
    }

    cout << rounds * 2 << '\n';

    delete[] a;

    return 0;
}
