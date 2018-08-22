# 爬山
# 时间限制：C / C + +语言
# 2000
# MS；其他语言
# 4000
# MS
# 内存限制：C / C + +语言
# 65536
# KB；其他语言
# 589824
# KB
# 题目描述：
# 冬木市西边的园藏山是著名的旅游圣地。从空中俯瞰，园藏山可以看成一个
# n * m
# 的矩阵，我们把行从上往下按
# 1
# 到
# n
# 编号，把列从左往右按
# 1
# 到
# m
# 编号，那么(i, j)
# 就表示矩阵第
# i
# 行第
# j
# 列的位置。我们用ℎi, j, 表示位置(i, j)
# 的海拔高度。
#
#
#
# 初始时，Saber
# 在(sx, sy)
# 这个位置，她想前往更高的地方。每一次她可以选择向上、下、左、右其中一个方向走，但不能走出这个矩阵；同时，作为大不列颠的王，孤傲的
# Saber
# 不愿意走到比她当前所在的位置海拔要低的位置，也就是说在移动的过程中，每一步她都只能向海拔不低于她当前所在的位置的那些位置移动。请你帮忙计算出她所能走到的最高高度。
#
# 输入
# 第一行包含两个整数n, m, 表示矩阵的规模1 ≤n, m≤ 200
#
# 第二行包含两个整数sx, sy
# 表示初始时
# Saber
# 的位置1 ≤ sx≤n, 1 ≤ sy≤m
#
# 接下来n行每行包含m个数字，0 ≤ ℎi, j ≤109 ，表示位置(i, j)
# 的海拔高度。
#
# 输出
# 输出
# Saber
# 能够移动到的最高高度。
#
#
# 样例输入
# 2
# 2
#
# 1
# 1
#
# 2
# 1
#
# 1
# 3
#
# 样例输出
# 2
#
# Hint
# input
# sample
# 2
# 23
# 11
# 152
# 04
# 9
# output
# sample
# 2
# 5



import sys

def in_put():
    lines = sys.stdin.readlines()
    nm = lines[0].strip('\n').split(' ')
    nm = [int(i) for i in nm]
    sxy = lines[1].strip('\n').split(' ')
    sxy = [int(i) for i in sxy]
    global matrix
    matrix = []
    for i in range(nm[0]):
        tmp = lines[i+2].strip('\n').split(' ')
        tmp = [int(i) for i in tmp]
        matrix.append(tmp)
    return nm, sxy, matrix


def pashan(nm, sxy, matrix):
    global n
    global m
    n = nm[0]
    m = nm[1]
    sx = sxy[0]-1
    sy = sxy[1]-1
    global dpM
    dpM = [[0 for row in range(m)] for col in range(n)]
    dpM[sx][sy] = matrix[sx][sy]
    run(sx, sy)
    maxh = 0
    for i in range(n):
        maxh = max(max(dpM[i]), maxh)
    return maxh


def run(sx, sy):
    if sx < 0 or sx > n-1 or sy < 0 or sy > m-1:
        return 0
    curh = matrix[sx][sy]
    road = []
    maxL = []
    if curh < matrix[sx-1][sy] and sx - 1 >= 0:
        road.append([sx-1,sy])
        maxL.append(matrix[sx-1][sy])
    elif sx + 1 < n and curh < matrix[sx+1][sy]:
        road.append([sx+1,sy])
        maxL.append(matrix[sx+1][sy])
    elif curh < matrix[sx][sy-1] and sy - 1 >= 0:
        road.append([sx,sy-1])
        maxL.append(matrix[sx][sy-1])
    elif sy + 1 < m and curh < matrix[sx][sy+1]:
        road.append([sx,sy+1])
        maxL.append(matrix[sx][sy+1])
    maxL.append(dpM[sx][sy])
    dpM[sx][sy] = max(maxL)
    for i in road:
        run(i[0],i[1])



if __name__ == '__main__':
    [nm, sxy, matrix] = in_put()
    print(pashan(nm, sxy, matrix))