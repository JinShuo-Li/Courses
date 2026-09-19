#include "stats.h"

#include <algorithm>
#include <cstddef>

double mean(const std::vector<int>& values) {
    double sum = 0;
    for (std::size_t i = 0; i < values.size(); ++i) {
        sum += values[i];
    }
    return sum / values.size();
}

double median(std::vector<int> values) {
    std::sort(values.begin(), values.end());
    std::size_t n = values.size();
    if (n % 2 == 1) {
        return values[n / 2];
    }
    return (values[n / 2 - 1] + values[n / 2]) / 2.0;
}

int spread(const std::vector<int>& values) {
    const auto minmax = std::minmax_element(values.begin(), values.end());
    return *minmax.second - *minmax.first;
}
