# 魔法王国一共有n个城市,编号为0~n-1号,n个城市之间的道路连接起来恰好构成一棵树。
# 小易现在在0号城市,每次行动小易会从当前所在的城市走到与其相邻的一个城市,小易最多能行动L次。
# 如果小易到达过某个城市就视为小易游历过这个城市了,小易现在要制定好的旅游计划使他能游历最多的城市,请你帮他计算一下他最多能游历过多少个城市(注意0号城市已经游历了,游历过的城市不重复计算)。
# 输入描述:
# 输入包括两行,第一行包括两个正整数n(2 ≤ n ≤ 50)和L(1 ≤ L ≤ 100),表示城市个数和小易能行动的次数。
# 第二行包括n-1个整数parent[i](0 ≤ parent[i] ≤ i), 对于每个合法的i(0 ≤ i ≤ n - 2),在(i+1)号城市和parent[i]间有一条道路连接。
#
#
# 输出描述:
# 输出一个整数,表示小易最多能游历的城市数量。
#
# 输入例子1:
# 5 2
# 0 1 2 3
#
# 输出例子1:
# 3
import sys
import math

def in_put():
    global par
    global n
    lines = sys.stdin.readlines()
    str1 = lines[0].strip('\n').split(' ')
    par = lines[1].strip('\n').split(' ')
    n = str1[0]
    L = str1[1]
    # print(str(n) + str(L) + str(str2))
    return [n, L, par]


def travel(parameter):
    [n, L, par] = parameter
    # 寻找最长路径
    maxdepth = fine_root('0', 1)
    if int(L) < maxdepth:
        return int(L)+1
    else:
        sum = int(maxdepth + math.floor((int(L) - maxdepth + 1)/2))
        if sum > int(n):
            return int(n)
        else:
            return sum

def fine_root(currentNode, currentLayer):
    nextNodeList = []

    for i in range(len(par)):
        if par[i] == currentNode:
            nextNodeList.append(str(i+1))

    if nextNodeList == []:
        return currentLayer
    else:
        depth = []
        for nextNode in nextNodeList:
            depth.append(fine_root(nextNode, currentLayer+1))
        return max(depth)


if __name__=='__main__':
    print(travel(in_put()))