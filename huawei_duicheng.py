import sys
import copy


def in_put():
    line = sys.stdin.readline()
    tmp = line.strip('\n')
    n = len(tmp)
    res = []
    for i in tmp:
        res.append(i)
    return res


def duicheng(rawsample):
    n = len(rawsample)
    maxl = 0
    for i in range(n):
        sample = copy.copy(rawsample[i:])
        start = 0
        end = len(sample) - 1
        while start < end:
            if sample[start] == sample[end]:
                start += 1
                end -= 1
            else:
                sample = sample[:-1]
                start = 0
                end = len(sample) - 1
        maxl = max([len(sample), maxl])
    return maxl



if __name__ == '__main__':
    print(duicheng(in_put()))