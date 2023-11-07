#include <array>

int main(){
  constexpr int maxsize = 100000;

  std::array<float,maxsize> u;
  std::array<float,maxsize> v;
  std::array<float,maxsize> z;
  std::array<float,maxsize> t;

  for (int i=0; i<maxsize; ++i) {
    u[i] = z[i] + t[i];
  }
  for (int i=0; i<maxsize; ++i) {
    v[i] = u[i] + t[i];
  }
}
