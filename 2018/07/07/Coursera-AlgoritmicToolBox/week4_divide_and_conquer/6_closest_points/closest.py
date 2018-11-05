#Uses python3
# Reference: https://medium.com/@andriylazorenko/closest-pair-of-points-in-python-79e2409fc0b2
import sys
import math

def dist(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def split_pair_find_closest(p_x, p_y, delta, best_pair):
    numberOfP = len(p_x)
    midP_x = p_x[numberOfP//2][0]
    # Create a subarray of p_y so that x falls within midP_x +- delta
    sub_p_y = [p for p in p_y if midP_x - delta <= p[0] <= midP_x + delta]
    for i in range(len(sub_p_y)-1):
        for j in range(i+1, min(i+7, len(sub_p_y))):
            if (sub_p_y[j][1] - sub_p_y[i][1] >= delta):
                continue
            currentD = dist(sub_p_y[i], sub_p_y[j])
            if (currentD < delta):
                best_pair = (sub_p_y[i], sub_p_y[j])
                delta = currentD
    return best_pair[0], best_pair[1], delta

def brute(points):
    minD = dist(points[0], points[1])
    p0 = points[0]
    p1 = points[1]
    nop = len(points)
    for i in range(nop-1):
        for j in range (i+1, nop):
            currentD = dist(points[i], points[j])
            if (currentD < minD):
                minD = currentD
                p0, p1 = points[i], points[j]
    return p0, p1, minD


def closest_pair(pointsX, pointsY):
    numberOfP = len(pointsX)
    # Base case
    if (numberOfP <= 3):
        return brute(pointsX) # Just use brutal force algorithm
    # Find middle point and split
    middlePIndex = numberOfP // 2
    lPointsX = pointsX[:middlePIndex]
    rPointsX = pointsX[middlePIndex:]
    lPointsY, rPointsY = [], []
    for pointY in pointsY:
        if (pointY[0] <pointsX[middlePIndex][0]):
            lPointsY.append(pointY)
        else:
            rPointsY.append(pointY)
#######################################################
#    print ("numberOfPoints={0} middle={1}".format(numberOfP, middlePIndex))
#    print("left: ", lPointsX, lPointsY)
#    print("right: ", rPointsX, rPointsY)
#######################################################
    # Get result of left and right side
    lp0, lp1, lminD = closest_pair(lPointsX, lPointsY)
    rp0, rp1, rminD = closest_pair(rPointsX, rPointsY)
#######################################################
#    print(" lp0={0} lp1={1} lminD={2}".format(lp0, lp1, lminD ))
#    print(" rp0={0} rp1={1} rminD={2}".format(rp0, rp1, rminD ))
#######################################################
    if (lminD < rminD):
        minD = lminD
        bestPoints = (lp0, lp1)
    else:
        minD = rminD
        bestPoints =  (rp0, rp1)
    # Generate and check the strips
    stripP0, stripP1, stripMinD = split_pair_find_closest(pointsX, pointsY, minD, bestPoints)
    # Calculate the best value
    if (stripMinD < minD):
        return stripP0, stripP1, stripMinD
    else:
        return bestPoints[0], bestPoints[1], minD

def minimum_distance(x, y):
    #write your code here
    xy = list(zip(x,y))
    sortedX = sorted(xy, key=lambda x: (x[0], x[1]))
    sortedY = sorted(xy, key=lambda x: (x[1], x[0]))
#######################################################
#    print (sortedX)
#    print (sortedY)
#######################################################
    p1, p2, minDistance = closest_pair(sortedX, sortedY)
#######################################################
#    print("p1 =",p1, "p2 =",p2, "minD =",minDistance)
#######################################################
    return minDistance

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
