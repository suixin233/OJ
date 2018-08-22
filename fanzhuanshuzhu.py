# 翻转数组
#
# 题目描述
#
# 给定一个长度为n的整数数组a，元素均不相同，问数组是否存在这样一个片段，只将该片段翻转就可以使整个数组升序排列。其中数组片段[l, r]
# 表示序列a[l], a[l + 1], ..., a[r]。原始数组为
#
# a[1], a[2], ..., a[l - 2], a[l - 1], a[l], a[l + 1], ..., a[r - 1], a[r], a[r + 1], a[r + 2], ..., a[n - 1], a[n]，
#
# 将片段[l, r]
# 反序后的数组是
#
# a[1], a[2], ..., a[l - 2], a[l - 1], a[r], a[r - 1], ..., a[l + 1], a[l], a[r + 1], a[r + 2], ..., a[n - 1], a[n]。
#
#
#
# 输入
# 第一行数据是一个整数：n(1≤n≤105)，表示数组长度。
#
# 第二行数据是n个整数a[1], a[2], ..., a[n](1≤a[i]≤109)。
#
# 样例输入
# 4
#
# 2
# 1
# 3
# 4
#
# 输出
# 输出“yes”，如果存在；否则输出“no”，不用输出引号。
#
# 样例输出
# yes
#
# 时间限制
# C / C + +语言：1000
# MS其它语言：3000
# MS
# 内存限制
# C / C + +语言：65536
# KB其它语言：589824
# KB



import sys

def in_put():
    n = sys.stdin.readline()
    n = n.strip('\n')
    if n == '':
        return 0,0
    n = int(n)
    line = sys.stdin.readline()
    line = line.strip('\n').split(' ')
    line = [int(i) for i in line]
    return n,line

def fanzhuanshuzhu(n, L):
    a = L
    b = sorted(a)
    c = [a[i] for i in range(n) if a[i] != b[i]]
    start = a.index(c[0])
    end = a.index(c[-1])
    if a[:start] + list(reversed(a[start:end + 1])) + a[end + 1:] == b:
        return "yes"
    else:
        return "no"

if __name__ == '__main__':
    while 1:
        [n, line] = in_put()
        if n != 0:
            print(fanzhuanshuzhu(n, line))
        else:
            break
