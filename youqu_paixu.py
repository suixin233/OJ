import sys

def in_put():
    lines = sys.stdin.readlines()
    n = int(lines[0].strip('\n'))
    line = lines[1].strip('\n').split(' ')
    line = [int(i) for i in line]
    return n,line


def interesting_paixu(n, line):
    seq = []
    lineSort = sorted(line)
    seq.append(line.index(lineSort[0]))
    count = 0
    for i in range(1, n):
        seq.append(line.index(lineSort[i]))
        if seq[i] < seq[i-1]:
            count += 1
            seq[i] = seq[i-1]
    if max(line) == line[-1] and count > 0:
        count += 1
    return count


if __name__ == '__main__':
    [n, line] = in_put()
    print(interesting_paixu(n, line))