#include <array>

constexpr int maxsize = 100000;

struct points {
  std::array<double, maxsize> x;
  std::array<double, maxsize> y;
};

int main() {
  points a{}, b{}, c{}; // Default init

  for (int i=0; i<maxsize; ++i) {
    a.x[i] = b.x[i] + c.x[i];
    a.y[i] = b.y[i] + c.y[i];
  }
}
