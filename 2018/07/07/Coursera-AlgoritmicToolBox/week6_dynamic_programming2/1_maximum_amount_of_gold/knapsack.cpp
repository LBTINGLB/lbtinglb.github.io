#include <iostream>
#include <vector>

using std::vector;

int optimal_weight(int W, const vector<int> &w) {
  //write your code here
  //int current_weight = 0;
  //for (size_t i = 0; i < w.size(); ++i) {
  //  if (current_weight + w[i] <= W) {
  //    current_weight += w[i];
  //  }
  //}
  //return current_weight;
  // A matrix of optimal result with respect to weight and numberOfGoldBars
  std::vector<std::vector<int>> matrix(W+1, std::vector<int>(w.size()+1));
  size_t itemNum = w.size();
  for (size_t currentWeight = 0; currentWeight <= W; currentWeight++)
  {
    for (size_t currentItemNum = 0; currentItemNum <= itemNum; currentItemNum++)
    {
      //std::cout << "currentWeight=" << currentWeight << " currentItemNum="
      //  << currentItemNum << std::endl;
      if (currentWeight ==0 || currentItemNum ==0) continue;
      else if(w[currentItemNum -1] <= currentWeight)
      {

        matrix[currentWeight][currentItemNum] = std::max(
            w[currentItemNum-1] + matrix[currentWeight-w[currentItemNum-1]][currentItemNum-1],
            matrix[currentWeight][currentItemNum-1]);
      }
      else
      {
        matrix[currentWeight][currentItemNum] = matrix[currentWeight][currentItemNum-1];
      }
      //std::cout << "  set matrix value to be" << matrix[currentWeight][currentItemNum]<<std::endl;
    }
  }
  return matrix[W][w.size()];
}

int main() {
  int n, W;
  std::cin >> W >> n;
  vector<int> w(n);
  for (int i = 0; i < n; i++) {
    std::cin >> w[i];
  }
  std::cout << optimal_weight(W, w) << '\n';
}
