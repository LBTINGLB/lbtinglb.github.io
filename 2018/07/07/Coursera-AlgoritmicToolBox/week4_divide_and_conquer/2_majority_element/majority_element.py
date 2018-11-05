# Uses python3
import sys

def get_majority_element(a, left, right):
#    if left == right:
#        return -1
#    if left + 1 == right:
#        return a[left]
#    #write your code here
#    middle = (left + right)//2
#    leftResult = get_majority_element(a,left, middle)
#    rightResult = get_majority_element(a,middle+1, right)
#    if (leftResult == rightResult): return leftResult
#    if (a[left:(left+middle+1)].count(leftResult) > a[(middle+1):right+1].count(rightResult)):
#        return leftResult
#    elif (a[left:(left+middle+1)].count(leftResult) <
#            a[(middle+1):right+1].count(rightResult)):
#        return rightResult
#    else: return -1
    a = sorted(a)
    if (len(a) == 0): return -1
    count = 1
    value = a[0]
    for i in range(1, len(a)):
        if (count == 0):
            count += 1
            value = a[i]
        elif (a[i] == value):
            count += 1
            if ( count*2 > len(a)):
                return a[i]
        else:
            count -= 1
    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n-1) != -1:
        print(1)
    else:
        print(0)
