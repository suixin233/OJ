# 牛牛从生物科研工作者那里获得一段字符串数据s,牛牛需要帮助科研工作者从中找出最长的DNA序列。DNA序列指的是序列中只包括'A','T','C','G'。牛牛觉得这个问题太简单了,就把问题交给你来解决。
# 例如: s = "ABCBOATER"中包含最长的DNA片段是"AT",所以最长的长度是2。
# 输入描述:
# 输入包括一个字符串s,字符串长度length(1 ≤ length ≤ 50),字符串中只包括大写字母('A'~'Z')。
#
#
# 输出描述:
# 输出一个整数,表示最长的DNA片段
#
# 输入例子1:
# ABCBOATER
#
# 输出例子1:
# 2

import sys


def in_put():
    line = sys.stdin.readline()
    tmp = line.strip('\n')
    n = len(tmp)
    res = []
    for i in tmp:
        res.append(i)
    return res


def DNA(sample):
    cl = ['A', 'T', 'C', 'G']
    longestlist = []
    longestlength = 0
    for i in sample:
        if i in cl:
            longestlist.append(i)
        else:
            longestlength = max([longestlength, len(longestlist)])
            longestlist = []
        if i == sample[-1] and longestlist != []:
            longestlength = max([longestlength, len(longestlist)])
    return longestlength


if __name__ == '__main__':
    sample = in_put()
    print(DNA(sample))