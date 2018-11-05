#include <iostream>
#include <vector>
#include <utility> //pair
#include <algorithm>

using std::vector;

double get_optimal_value(int capacity, vector<int> weights, vector<int> values) {
  double value = 0.0;

  // write your code here
  // Sort the valuePerWeight array
  using myPair = std::pair<double, size_t>;
  size_t numberOfValues = weights.size();
  std::vector<myPair> vpw(numberOfValues);
  for (size_t i = 0; i < weights.size(); i++)
  {
    vpw.push_back(std::make_pair(double(values[i])/weights[i], i));
  }
  std::sort(vpw.begin(), vpw.end(), [](const myPair& a, const myPair& b){
    return a.first > b.first;
  });

  
  int rw(capacity), cw; //remaining weight, current weight
  size_t vpwIndex(0);
  while (rw>0 && (vpwIndex < numberOfValues))
  {
    size_t wAvIndex = vpw[vpwIndex].second;
    cw = std::min(rw, weights[wAvIndex]);
    value += cw * vpw[vpwIndex].first;
    rw -= cw;
    vpwIndex++;
  }

  return value;
}


int main() {
  int n;
  int capacity;
  std::cin >> n >> capacity;
  vector<int> values(n);
  vector<int> weights(n);
  for (int i = 0; i < n; i++) {
    std::cin >> values[i] >> weights[i];
  }

  double optimal_value = get_optimal_value(capacity, weights, values);

  std::cout.precision(10);
  std::cout << optimal_value << std::endl;
  return 0;
}
