# Uses python3
import sys

# Get the cloest index of x in list a
# useful hint: https://www.coursera.org/learn/algorithmic-toolbox/discussions/all/threads/QJ1jK9wNEeWdPBL2iFTrAw/replies/Ihiw4txhEeWK5g7mfcS2Xw/comments/oyAMaeIiEeWyqwpvChh66Q

# https://codereview.stackexchange.com/questions/190145/find-the-closest-number-in-a-sorted-list-to-a-given-target-number
def fast_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    values = [(0,"a")] * (len(starts) + len(ends) + len(points))
    # Add starts, ends and points to values and sort it
    valuesIndex = 0
    for i in range(len(starts)):
        values[valuesIndex] = (starts[i], "l")
        valuesIndex += 1
    for i in range(len(ends)):
        values[valuesIndex] = (ends[i], "r")
        valuesIndex += 1
    for i in range(len(points)):
        values[valuesIndex] = (points[i], "p" + str(i))
        valuesIndex += 1
    values.sort()
    #print("values =", values)
    #write your code here
    segCount = 0
    for i in range(len(values)):
        status = values[i][1]
        if (status == "l"): segCount += 1
        elif (status == "r"): segCount -= 1
        elif (status[0] == "p"): cnt[int(status[1:])] = segCount
    return cnt

def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    #use fast_count_segments
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')
