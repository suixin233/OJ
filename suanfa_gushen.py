# 题目描述
#
# 有股神吗？
#
# 有，小赛就是！
# 
# 经过严密的计算，小赛买了一支股票，他知道从他买股票的那天开始，股票会有以下变化：第一天不变，以后涨一天，跌一天，涨两天，跌一天，涨三天，跌一天...依此类推。
#
# 为方便计算，假设每次涨和跌皆为1，股票初始单价也为1，请计算买股票的第n天每股股票值多少钱？
#
#
#
# 输入
# 输入包括多组数据；
#
# 每行输入一个n，1 <= n <= 10 ^ 9 。
#
# 样例输入
# 1
#
# 2
#
# 3
#
# 4
#
# 5
#
# 输出
# 请输出他每股股票多少钱，对于每组数据，输出一行。
#
# 样例输出
# 1
#
# 2
#
# 1
#
# 2
#
# 3


import sys

def in_put():
    lines = sys.stdin.readlines()
    out_put = []
    for i in range(len(lines)):
        tmp = lines[i].strip('\n')
        out_put.append(int(tmp))
    return out_put


def gushen(n):
    day = int(n) - 1
    price = 1
    up = 1
    while day >= up + 1:
        price = price + up - 1
        day = day - 1 - up
        up = up + 1
    price = price + day
    return price


if __name__ == '__main__':
    sample = in_put()
    for i in sample:
        print(gushen(i))