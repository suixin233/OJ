# 携程旅行网 2018春招 大数据分析在线考试
# 编程题 | 20.0分1/1
# 最长路径问题
# 时间限制：C/C++语言 1000MS；其他语言 3000MS
# 内存限制：C/C++语言 65536KB；其他语言 589824KB
# 题目描述：
# 现有A、B、C、D、E五个字符，以及M个字符串，每个字符串由这五个字符和1-9的整数间隔组成，如：A2B3D，表示存在A->B和B->D的路径，且路径长度为2和3，可以推出A->D的一条路径长度为5；
#
# 求最长的一条路径的长度，如果任何一处路径出现环(即出现A->...->A, B->...->B, C->...->C, D->...->D, E->...->E的路径)，返回-1。
#
# 输入
# 第一行 为字符串的个数M
#
# 第二行 开始为M个字符串
#
# 输出
# 最长的一条路径的长度，如果出现环，返回-1
#
#
# 样例输入
# 4
# A5B3D
# A4C2E
# A5D
# C3B
#
# 样例输出
# 10



#!/bin/python
import sys
import os


# 请完成下面这个函数，实现题目要求的功能
# 当然，你也可以不按照下面这个模板来作答，完全按照自己的想法来 ^-^
# ******************************开始写代码******************************


def calculate(M, strs):
    ListofABCDE = ['A', 'B', 'C', 'D', 'E']
    sumL = []
    for i in range(M):
        path = strs[i]
        L = len(path)
        DL = set()
        sum = 0
        for j in range(L):
            if path[j] in ListofABCDE:
                if path[j] not in DL:
                    DL.add(path[j])
                else:
                    return -1
            elif int(path[j]) > 0:
                sum = sum + int(path[j])
        sumL.append(sum)
    return max(sumL)



# ******************************结束写代码******************************


_M = int(input())

_strs_cnt = _M
_strs_i = 0
_strs = []
while _strs_i < _strs_cnt:
    try:
        _strs_item = input()
    except:
        _strs_item = None
    _strs.append(_strs_item)
    _strs_i += 1

res = calculate(_M, _strs)

print(str(res) + "\n")