#include "stats.h"

#include <cstddef>
#include <iostream>
#include <vector>

int main() {
    std::cout << "How many numbers? ";
    int n;
    if (!(std::cin >> n) || n <= 0) {
        std::cerr << "expected a positive count\n";
        return 1;
    }

    std::vector<int> values(n);
    std::cout << "Enter " << n << " integers: ";
    for (int i = 0; i < n; ++i) {
        std::cin >> values[i];
    }

    std::cout << "count  = " << values.size() << '\n';
    std::cout << "mean   = " << mean(values) << '\n';
    std::cout << "median = " << median(values) << '\n';
    std::cout << "spread = " << spread(values) << '\n';

    return 0;
}
