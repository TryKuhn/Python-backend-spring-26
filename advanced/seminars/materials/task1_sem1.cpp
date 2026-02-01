#include <iostream>
#include <vector>

int max(int a, int b) {
    return a > b ? a : b;
}

int max(int n, std::vector<int> a) {
    int max = a[0];
    for (int i = 1; i < n; i++) {
        if (max < a[i]) {
            max = a[i];
        }
    }
    return max;
}

int main() {
    std::cout << max(3, 5) << '\n';

    std::vector<int> v = {1, 3, 7, 0, 4};

    std::cout << max(5, v) << '\n';
}