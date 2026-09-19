#include <algorithm>
#include <cstddef>
#include <iostream>
#include <vector>

long long factorial(int n) {
    if (n <= 1) return 1;
    return n * factorial(n - 1);
}

int main() {
    int n;
    std::cout << "How many numbers? ";
    std::cin >> n;

    std::vector<int> values(n);
    std::cout << "Enter " << n << " integers: ";
    for (int i = 0; i < n; ++i) {
        std::cin >> values[i];
    }

    std::sort(values.begin(), values.end());

    std::cout << "Sorted:";
    for (std::size_t i = 0; i < values.size(); ++i) {
        std::cout << ' ' << values[i];
    }
    std::cout << '\n';

    int target;
    std::cout << "Search for: ";
    std::cin >> target;
    std::cout << target << (std::binary_search(values.begin(), values.end(), target) ? " found" : " not found") << '\n';

    int k;
    std::cout << "Factorial of: ";
    std::cin >> k;
    std::cout << k << "! = " << factorial(k) << '\n';

    return 0;
}
