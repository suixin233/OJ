import sys

def in_put():
    line = sys.stdin.readline()
    tmp = line.strip('\n').split(' ')
    res = [int(i) for i in tmp]
    return res


def sum_gcd(res):
    N = res[0]
    n = res[1]
    m = res[2]
    p = res[3]
    A = [p]
    for i in range(1,N):
        A.append(int((A[-1] + 153) % p))
    res_sum = 0
    for i in range(n):
        print(i)
        for j in range(m):
            res_sum = res_sum + A[gcd_chu(i+1,j+1)-1]
    return res_sum


def gcd(x, y):
    if x == y:
        return y
    elif x < y:
        tmp = y
        y = x
        x = tmp
    if x - y == y or y == 1:
        return y
    else:
        tmp = x
        x = y
        y = tmp - x
        return gcd(x,y)


def gcd_chu(x,y):
    if x < y:
        tmp = y
        y = x
        x = tmp
    if x % y == 0:
        return y
    else:
        tmp = int(x % y)
        x = y
        y = tmp
        return gcd_chu(x,y)


if __name__ == '__main__':
    res = in_put()
    print(sum_gcd(res))