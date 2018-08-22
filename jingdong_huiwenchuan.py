import sys

def in_put():
    line = sys.stdin.readline()
    result = line.strip('\n')
    return result


def huiwenchuan(res, pseq):
    global count
    global seq
    curseq = []
    if len(res) == 1:
        if pseq not in seq:
            count = count + 1
            seq.append(pseq)
        return
    for i in range(len(res)):
        remain = res[:i] + res[i+1:]
        restr = res[i]
        if panduan(remain) == 1 and restr not in curseq and pseq+restr not in seq:
            count = count + 1
            curseq.append(restr)
            seq.append(pseq+restr)
        huiwenchuan(remain, pseq+restr)
    return count


def panduan(strin):
    if len(strin) == 1:
        return 1
    start = 0
    end = len(strin) - 1
    while start < end:
        if strin[start] == strin[end]:
            start += 1
            end -= 1
        else:
            return 0
    if start == end or start == end + 1:
        return 1


if __name__ == '__main__':
    count = 0
    seq = []
    print(huiwenchuan(in_put(), ''))