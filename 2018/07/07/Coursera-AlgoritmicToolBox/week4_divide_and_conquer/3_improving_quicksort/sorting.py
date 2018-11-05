# Uses python3
import sys
import random

def partition3(a, l, r):
    #write your code here
    p = a[l] # pivot value
    sp, ep = l, l # smaller and equal position
    for i in range(l + 1, r + 1):
        if (a[i] < p):
            sp += 1
            ep += 1
            a[i], a[sp] = a[sp], a [i]
        if (a[i] == p):
            ep += 1
            a[i], a[ep] = a[ep], a[i]
    a[sp], a[l] = a[l], a[sp]
    return sp # position of the pivot

def partition2(a, l, r):
    x = a[l]
    j = l;
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
 #   if l >= r:
 #       return
 #   k = random.randint(l, r)
 #   a[l], a[k] = a[k], a[l]
 #   #use partition3
 #   m = partition3(a, l, r)
 #   randomized_quick_sort(a, l, m - 1)
 #   randomized_quick_sort(a, m + 1, r)
    while l < r:
        k = random.randint(l, r)
        a[l], a[k] = a[k], a[l]
        #use partition3
        m = partition3(a, l, r)
        if ((m - l) < (r - m )):
            randomized_quick_sort(a, l, m - 1)
            l = m + 1
        else:
            randomized_quick_sort(a, m+1, r)
            r = m-1


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    #randomized_quick_sort(a, 0, n - 1)
    a = sorted(a)
    for x in a:
        print(x, end=' ')
