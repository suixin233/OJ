# 牛牛喜欢彩色的东西,尤其是彩色的瓷砖。牛牛的房间内铺有L块正方形瓷砖。每块砖的颜色有四种可能:红、绿、蓝、黄。给定一个字符串S, 如果S的第i个字符是'R', 'G', 'B'或'Y',那么第i块瓷砖的颜色就分别是红、绿、蓝或者黄。
# 牛牛决定换掉一些瓷砖的颜色,使得相邻两块瓷砖的颜色均不相同。请帮牛牛计算他最少需要换掉的瓷砖数量。
# 输入描述:
# 输入包括一行,一个字符串S,字符串长度length(1 ≤ length ≤ 10),字符串中每个字符串都是'R', 'G', 'B'或者'Y'。
#
#
# 输出描述:
# 输出一个整数,表示牛牛最少需要换掉的瓷砖数量
#
# 输入例子1:
# RRRRRR
#
# 输出例子1:
# 3

import sys
import random

def in_put():
    line = sys.stdin.readline()
    tmp = line.strip('\n')
    n = len(tmp)
    res = []
    for i in tmp:
        res.append(i)
    return res


def caise(sample):
    n = len(sample)
    color = {'R', 'G', 'B', 'Y'}
    count = 0
    for i in range(1,n):
        if sample[i] == sample [i-1]:
            if i+1 <= n-1:
                if sample[i+1] == sample [i]:
                    sett = color - set(sample[i])
                    sample[i] = sett.pop()
                    count = count + 1
                else:
                    sett = color - set(sample[i]) - set(sample[i+1])
                    sample[i] = sett.pop()
                    count = count + 1
            else:
                sett = color - set(sample[i])
                sample[i] = sett.pop()
                count = count + 1
    return count



if __name__ == '__main__':
    sample = in_put()
    print(caise(sample))