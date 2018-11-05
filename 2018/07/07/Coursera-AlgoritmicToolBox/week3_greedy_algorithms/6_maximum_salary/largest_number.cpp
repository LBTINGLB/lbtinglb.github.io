#include <algorithm>
#include <sstream>
#include <iostream>
#include <vector>
#include <string>

using std::vector;
using std::string;

/*
	50 
 9 10 3 10 7 5 7 1 7 5 1 4
 7 6 1 10 5 4 8 4 2 7 8 1
  1 7 4 1 1 9 8 6 5 9 9 3 
  7 6 3 10 8 10 7 2 5 1 1 9 
  9 5
 */
bool isGreatOrEqual(const std::string& left,
                          const std::string& right)
{
	// https://stackoverflow.com/questions/979759/operator-and-strict-weak-ordering
  size_t lS = left.size(), rS = right.size(), i(0);
  if (left == right) return true;
  while (lS > 0 && rS > 0)
  {
    if (left.at(i) == right.at(i))
    { // Compare next digit
      i++;
      lS--;
      rS--;
    }
    else
    {
      return (left[i]) > right[i];
    }
  }
  if (lS == 0 && rS == 0)
  {
    return left < right;
  }
  if (lS == 0)
  {
    return left[0] > right[i];
  }
  else if (rS == 0)
  {
    return left[i] > right[0];
  }
}

string largest_number(vector<string> a) {
  //write your code here
  std::sort(a.begin(), a.end(), isGreatOrEqual);
  std::stringstream ret;
  for (size_t i = 0; i < a.size(); i++) {
    ret << a[i];
  }
  string result;
  ret >> result;
  return result;
}

int main() {
  int n;
  std::cin >> n;
  vector<string> a(n);
  for (size_t i = 0; i < a.size(); i++) {
    std::cin >> a[i];
  }
  std::cout << largest_number(a);
}
