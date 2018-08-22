import sys
import math

def in_put():
    line = sys.stdin.readline()
    N = line.strip('\n').split(' ')
    NL = [int(i) for i in N]
    return NL


def quick_sort(a, left, right):
    if left < right:
        p = partition(a, left, right)
        quick_sort(a, left, p-1)
        quick_sort(a, p+1, right)
    return a


def partition(a,left,right):
    key = a[left]
    while left < right:
        while left < right and a[right] >= key:
            right = right - 1
        a[left] = a[right]
        while left < right and a[left] <= key:
            left = left + 1
        a[right] = a[left]
        a[left] = key
    return left


if __name__=='__main__':
    sample = in_put()
    n = len(sample)
    print(quick_sort(sample, 0, n-1))