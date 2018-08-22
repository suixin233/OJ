# 小Q和牛博士合唱一首歌曲,这首歌曲由n个音调组成,每个音调由一个正整数表示。
# 对于每个音调要么由小Q演唱要么由牛博士演唱,对于一系列音调演唱的难度等于所有相邻音调变化幅度之和, 例如一个音调序列是8, 8, 13, 12, 那么它的难度等于|8 - 8| + |13 - 8| + |12 - 13| = 6(其中||表示绝对值)。
# 现在要对把这n个音调分配给小Q或牛博士,让他们演唱的难度之和最小,请你算算最小的难度和是多少。
# 如样例所示: 小Q选择演唱{5, 6}难度为1, 牛博士选择演唱{1, 2, 1}难度为2,难度之和为3,这一个是最小难度和的方案了。
# 输入描述:
# 输入包括两行,第一行一个正整数n(1 ≤ n ≤ 2000) 第二行n个整数v[i](1 ≤ v[i] ≤ 10^6), 表示每个音调。
#
#
# 输出描述:
# 输出一个整数,表示小Q和牛博士演唱最小的难度和是多少。
#
# 输入例子1:
# 5
# 1 5 6 2 1
#
# 输出例子1:
# 3

import sys

def in_put():
    lines = sys.stdin.readlines()
    n = lines[0].strip('\n')
    VL = lines[1].strip('\n').split(' ')
    VL = [int(i) for i in VL]
    return VL


def sing(VL):
    n = len(VL)
    dp = [[100 for row in range(n)] for col in range(n)]
    dp[0][0] = 0
    dp[1][0] = 0
    for i in range(2,n):
        dp[i][0] = dp[i-1][0] + abs(VL[i] - VL[i-1])
    for i in range(2,n):
        dp[i][i-1] = dp[i-1][i-2] + abs(VL[i-1] - VL[i-2])
    for i in range(1,n):
        for j in range(i-1):
            dp[i][j] = dp[i-1][j] + abs(VL[i]-VL[i-1])
        L = []
        for k in range(i-1):
            L.append(dp[i-1][k] + abs(VL[i]-VL[k]))
        L.append(dp[i][i-1])
        if len(L) > 0:
            dp[i][i-1] = min(L)
    return min(dp[n-1][:-1])


def calculateD(x):
    sum = 0
    for i in range(len(x)-1):
        sum = sum + abs(x[i]-x[i+1])
    return sum


if __name__ == '__main__':
    print(sing(in_put()))