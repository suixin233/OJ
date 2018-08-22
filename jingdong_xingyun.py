import sys
import copy


def in_put():
    lines = sys.stdin.readlines()
    n = int(lines[0].strip('\n'))
    line = lines[1].strip('\n').split(' ')
    result = []
    for i in range(n):
        time = line[i].split(':')
        result.append(time)
    return result


def xingyun(res):
    count = 0
    for time in res:
        if time[0] == time[1]:
            count = count + 1
        elif time[0][0] == time[0][1] and time[1][0] == time[1][1]:
            count = count + 1
        elif time[0][0] == time[1][1] and time[0][1] == time[1][0]:
            count = count + 1
    return count


if __name__ == '__main__':
    print(xingyun(in_put()))