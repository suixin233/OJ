import sys
import copy

def in_put():
    lines = sys.stdin.readlines()
    n = int(lines[0].strip('\n'))
    line = lines[1].strip('\n').split(' ')
    line = [int(i) for i in line]
    return n,line


def caozuo(n, line):
    seq = copy.copy(line)
    seqb = []
    for i in range(n):
        seqb.append(seq[i])
        n = len(seqb)
        tmp = []
        for j in reversed(seqb):
            tmp.append(j)
        seqb = copy.copy(tmp)
    return seqb


if __name__ == '__main__':
    [n, line] = in_put()
    seqb = caozuo(n, line)
    for i in range(n):
        if i == n-1:
            print(str(seqb[i]))
        else:
            print(str(seqb[i]),end=' ')

