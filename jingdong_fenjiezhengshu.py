import sys
import copy


def in_put():
    lines = sys.stdin.readlines()
    n = len(lines)
    start = 0
    all_result = []
    while start < n:
        remain = lines[start:]
        count = int(remain[0].strip('\n'))
        res = []
        for i in range(1,count+1):
            tmp = remain[i].strip('\n')
            res.append(int(tmp))
        all_result.append(res)
        start = start + count + 1
    return all_result


def fenjiezhengshu(zs):
    if zs % 2 == 1:
        return 'No'
    res = int(zs / 2)
    start = 3
    while start < res:
        if res % start == 0:
            return [start, int(zs/start)]
        else:
            start = start + 2
    return [int(zs/2), 2]



if __name__ == '__main__':
    zsl = in_put()
    for i in zsl:
        for j in i:
            res = fenjiezhengshu(j)
            if res == 'No':
                print(res)
            elif len(res) == 2:
                print(res[0], end=' ')
                print(res[1])