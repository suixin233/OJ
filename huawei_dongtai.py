import sys
import copy


def in_put():
    lines = sys.stdin.readlines()
    bag = int(lines[0].strip('\n'))
    weight = lines[1].strip('\n').split(' ')
    price = lines[2].strip('\n').split(' ')
    weight = [int(i) for i in weight]
    price = [int(i) for i in price]
    return bag, weight, price


def dp(bag, weight, price):
    w = [0] + weight
    p = [0] + price
    n = len(w) - 1
    m = bag

    x = []
    v = 0
    dpM = [[0 for col in range(m+1)] for row in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, m+1):
            if j>= w[i]:
                dpM[i][j] = max(dpM[i-1][j], dpM[i-1][j - w[i]] + p[i])
            else:
                dpM[i][j] = dpM[i-1][j]

    j = m
    for i in range(n, 0, -1):
        if dpM[i][j] > dpM[i-1][j]:
            x.append(i)
            j = j - w[i]
    v = dpM[n][m]
    return v,x



if __name__ == '__main__':
    [bag, weight, price] = in_put()
    [v,x] = dp(bag, weight, price)
    x = sorted(x)
    for i in range(len(x)):
        if i < len(x) - 1:
            print(str(x[i]), end=' ')
        elif i == len(x) - 1:
            print(str(x[i]))