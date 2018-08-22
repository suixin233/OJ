

def in_put():
    num = input()
    num2 = num.split(' ')
    num3 = []
    for i in range(len(num2)):
        num3.append(num2[i])
    return num2


def out_put(x):
    s = " ".join(str(i) for i in x)
    return s

def in_put():
    num = int(sys.stdin.readline())
    return num

import sys

def in_put():
    lines = sys.stdin.readlines()
    n = int(lines[0].strip('\n'))
    line = lines[1].strip('\n').split(' ')
    line = [int(i) for i in line]
    return n,line


def in_put():
    lines = sys.stdin.readlines()
    n = int(lines[0].strip('\n'))
    nl = []
    for i in range(n):
        nl.append(int(lines[i+1].strip('\n')))
    return n,nl

if __name__ == '__main__':
    [n, line] = in_put()
    print()