# Uses python3
import sys
import random

number_of_inversions = 0
def merge(A, B):
    global number_of_inversions
    if ((len(A) == 0) or (len(B) == 0)):
        return A+B
    else:
        if (A[0] < B[0]):
            return [A[0]] + merge(A[1:], B)
        else:
            for i in range(len(A)):
                if (A[i] > B[0]):
                    number_of_inversions += 1
            return [B[0]] + merge(A, B[1:])

def mergeSort(a):
    #write your code here
    if (len(a) < 2): return a
    else:
        mid = len(a) // 2
        left = mergeSort(a[:mid])
        right = mergeSort(a[mid:])
        return merge(left, right)
def naive_noi(a):
    count = 0
    for i in range(len(a)):
        for j in range(i, len(a)):
            if (a[i] > a[j]): count += 1
    return count

if __name__ == '__main__':
    inputs = sys.stdin.read()
    n, *a = list(map(int, inputs.split()))
    b = n * [0]
    mergeSort(a)
######
#    flag = True
#    while flag:
#        inputV = [random.randint(0,15) for _ in range(random.randint(0,15))]
#        number_of_inversions = 0
#        mergeSort(inputV)
#        if (number_of_inversions != naive_noi(inputV)):
#            print ("I'm wrong!")
#            print (inputV)
#            flag = False
#####
    print(number_of_inversions)

