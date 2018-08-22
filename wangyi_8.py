# 小易正在玩一款新出的射击游戏,这个射击游戏在一个二维平面进行,小易在坐标原点(0,0),平面上有n只怪物,每个怪物有所在的坐标(x[i], y[i])。小易进行一次射击会把x轴和y轴上(包含坐标原点)的怪物一次性消灭。
# 小易是这个游戏的VIP玩家,他拥有两项特权操作:
# 1、让平面内的所有怪物同时向任意同一方向移动任意同一距离
# 2、让平面内的所有怪物同时对于小易(0,0)旋转任意同一角度
# 小易要进行一次射击。小易在进行射击前,可以使用这两项特权操作任意次。
# 小易想知道在他射击的时候最多可以同时消灭多少只怪物,请你帮帮小易。
#
# 如样例所示:
#
# 所有点对于坐标原点(0,0)顺时针或者逆时针旋转45°,可以让所有点都在坐标轴上,所以5个怪物都可以消灭。
#
# 输入描述:
# 输入包括三行。
# 第一行中有一个正整数n(1 ≤ n ≤ 50),表示平面内的怪物数量。
# 第二行包括n个整数x[i](-1,000,000 ≤ x[i] ≤ 1,000,000),表示每只怪物所在坐标的横坐标,以空格分割。
# 第二行包括n个整数y[i](-1,000,000 ≤ y[i] ≤ 1,000,000),表示每只怪物所在坐标的纵坐标,以空格分割。
#
#
# 输出描述:
# 输出一个整数表示小易最多能消灭多少只怪物。
#
# 输入例子1:
# 5
# 0 -1 1 1 -1
# 0 -1 -1 1 1
#
# 输出例子1:
# 5

import sys

def in_put():
    global x,y
    lines = sys.stdin.readlines()
    n = int(lines[0].strip('\n'))
    x = lines[1].strip('\n').split(' ')
    x = [int(i) for i in x]
    y = lines[2].strip('\n').split(' ')
    y = [int(i) for i in y]
    return n,x,y


def destroy(n,x,y):
    All = []
    for i in range(n):
        for j in range(i+1, n):
                for k in range(n):
                    if k != i and k != j:
                        if threePP(i,j,k) == 0:
                            sum = 0
                            for l in range(n):
                                if l != i and l != j and l!= k:
                                    if threePP(i,j,l) == 1:
                                        sum = sum + 1
                                        continue
                                    elif twoLineP(i,j,k,l) == 1:
                                        sum = sum + 1
                                        continue
                            All.append(sum)
    for i in range(n-2):
        if threePP(i,i+1,i+2) == 1:
            if i == n-3:
                All.append(n-3)
        else:
            break

    if len(All) == 0:
        if n > 3:
            return 3
        else:
            return n
    else:
        return max(All) + 3


def threePP(i,j,k):
    if (y[k]-y[i])*(x[k]-x[j])-(y[k]-y[j])*(x[k]-x[i]) == 0:
        return 1
    else:
        return 0


def twoLineP(i,j,k,l):
    if (x[i]-x[j])*(x[k]-x[l])+(y[i]-y[j])*(y[k]-y[l]) == 0:
        return 1
    else:
        return 0


if __name__ == '__main__':
    [n,x,y] = in_put()
    print(destroy(n,x,y))