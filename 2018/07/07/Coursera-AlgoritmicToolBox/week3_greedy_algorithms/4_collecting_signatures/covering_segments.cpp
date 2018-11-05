#include <algorithm>
#include <iostream>
#include <climits>
#include <vector>

using std::vector;

struct Segment {
  int start, end;
};

vector<int> optimal_points(vector<Segment> &segments) {
  vector<int> points;
  // write your code here
  std::sort(segments.begin(), segments.end(), [](const Segment& left,const Segment& right){
    if (left.start == right.start)
    {
      return left.end < right.end;
    }
    return left.start < right.start;
  });
  size_t i(0),nos(segments.size());
  //std::cout << "After sort: " <<std::endl;
  //for(auto& seg: segments)
  //{
  //  std::cout << seg.start << " " << seg.end <<std::endl;
  //}
  while (i < nos)
  {
    //std::cout << "i=" << i <<std::endl;
    int cS = segments[i].start;
    int cE = segments[i].end;
    int pointTBI = segments[i++].start;
    // update i
    while (i < nos && segments[i].start <= cE)
    {
      pointTBI = segments[i].start;
      // shrink the cE if needed
      cE = std::min(cE, segments[i].end);
      i++;
    }
    //std::cout << "i=" << i << " value=" << pointTBI <<std::endl;
    points.push_back(pointTBI);
  }
  return points;
}

int main() {
  int n;
  std::cin >> n;
  vector<Segment> segments(n);
  for (size_t i = 0; i < segments.size(); ++i) {
    std::cin >> segments[i].start >> segments[i].end;
  }
  vector<int> points = optimal_points(segments);
  std::cout << points.size() << "\n";
  for (size_t i = 0; i < points.size(); ++i) {
    std::cout << points[i] << " ";
  }
}
