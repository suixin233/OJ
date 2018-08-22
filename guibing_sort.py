import sys
import math

def in_put():
    line = sys.stdin.readline()
    N = line.strip('\n').split(' ')
    NL = [int(i) for i in N]
    return NL


def guibing_sort(NL):
    L = len(NL)
    middle = int(L / 2)
    Left = NL[:middle]
    Right = NL[middle:]
    while L > 1:
        return compare(guibing_sort(Left), guibing_sort(Right))
    if L == 1:
        return NL



def compare(Left, Right):
    NL = len(Left)
    NR = len(Right)
    i = 0
    j = 0
    result = []
    while i < NL and j < NR:
        if Left[i] < Right[j]:
            result.append(Left[i])
            i = i + 1
        else:
            result.append(Right[j])
            j = j + 1
    if i > (NL - 1):
        result = result + Right[j:]
    if j > (NR - 1):
        result = result + Left[i:]
    return result

if __name__=='__main__':
    print(guibing_sort(in_put()))