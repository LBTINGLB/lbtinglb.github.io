#include <iostream>
#include <numeric>
#include <string>
#include <unordered_map>
#include <vector>

using std::vector;

bool subSum(vector<int> &items, int n, int a, int b, int c,
    std::unordered_map<std::string, bool>& lookup)
{
  // return true if subset is found
    if (a == 0 && b == 0 && c == 0)
        return true;

    // base case: no items left
    if (n < 0)
        return false;

    // construct a unique map key from dynamic elements of the input
    std::string key = std::to_string(a) + "-" + std::to_string(b) + "-" + std::to_string(c) +
                "-" + std::to_string(n);

    // if sub-problem is seen for the first time, solve it and
    // store its result in a map
    if (lookup.find(key) == lookup.end())
    {
        // Case 1. current item becomes part of first subset
        bool A = false;
        if (a - items[n] >= 0)
            A = subSum(items, n - 1, a - items[n], b, c, lookup);

        // Case 2. current item becomes part of second subset
        bool B = false;
        if (!A && (b - items[n] >= 0))
            B = subSum(items, n - 1, a, b - items[n], c, lookup);

        // Case 3. current item becomes part of third subset
        bool C = false;
        if ((!A && !B) && (c - items[n] >= 0))
            C = subSum(items, n - 1, a, b, c - items[n], lookup);

        // return true if we get solution
        lookup[key] = A || B || C;
    }

    // return the subproblem solution from the map
    return lookup[key];
}

int partition3(vector<int> &items) {
  //write your code here
  if (items.size() < 3)
    return 0;
  std::unordered_map<std::string, bool> lookup;
  int sum = std::accumulate(items.begin(), items.end(), 0);
  bool ableSeperatedBy3 = !(sum%3);
  //std::cout << "ableSeperatedBy3?" << ableSeperatedBy3 << std::endl;

  return ableSeperatedBy3 && subSum(items, items.size()-1, sum/3, sum/3, sum/3, lookup);
}

int main() {
  int n;
  std::cin >> n;
  vector<int> A(n);
  for (size_t i = 0; i < A.size(); ++i) {
    std::cin >> A[i];
  }
  std::cout << partition3(A) << '\n';
}
