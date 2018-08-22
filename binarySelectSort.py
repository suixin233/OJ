import sys
import math

def in_put():
    line = sys.stdin.readline()
    N = line.strip('\n').split(' ')
    NL = [int(i) for i in N]
    return NL

def binarySelectSort(NL):
    n = len(NL)
    for i in range(int(n/2)):
        max = i
        min = i
        for j in range(i+1, n-i):
            if NL[j] < NL[min]:
                min = j
            if NL[j] > NL[max]:
                max = j

        if max == i and min != n-1-i:
            tmpmax = NL[n - 1 - i]
            NL[n - 1 - i] = NL[max]
            NL[max] = tmpmax
            tmpmin = NL[i]
            NL[i] = NL[min]
            NL[min] = tmpmin
        elif max ==i and min == n-1-i:
            tmpmax = NL[n - 1 - i]
            NL[n - 1 - i] = NL[max]
            NL[max] = tmpmax
        else:
            tmpmin = NL[i]
            NL[i] = NL[min]
            NL[min] = tmpmin
            tmpmax = NL[n - 1 - i]
            NL[n - 1 - i] = NL[max]
            NL[max] = tmpmax
    return NL

if __name__=='__main__':
    print(binarySelectSort(in_put()))