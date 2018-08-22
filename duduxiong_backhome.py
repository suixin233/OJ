import sys
import copy

def in_put():
    lines = sys.stdin.readlines()
    n = int(lines[0].strip('\n'))
    line = lines[1].strip('\n').split(' ')
    line = [int(i) for i in line]
    return n,line


def backhome(n, line):
    minL = 0
    for i in range(1,n-1):
        tmp = copy.copy(line)
        del tmp[i]
        length = distance_count(tmp)
        if i == 1:
            minL = length
        else:
            minL = min(length, minL)
    return minL

def distance_count(path):
    n = len(path)
    count = 0
    for i in range(n-1):
        count = count + abs(path[i] - path[i+1])
    return count


if __name__ == '__main__':
    [n, line] = in_put()
    print(backhome(n, line))