#include <array>

struct point {
  double x;
  double y;
};

int main() {
  constexpr int maxsize = 100000;

  std::array<point, maxsize> a;
  std::array<point, maxsize> b;
  std::array<point, maxsize> c;

  for (int i=0; i<maxsize; ++i) {
    a[i].x = b[i].x + c[i].x;
    a[i].y = b[i].y + c[i].y;
  }
}
