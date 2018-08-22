# 一个由小写字母组成的字符串可以看成一些同一字母的最大碎片组成的。例如,"aaabbaaac"是由下面碎片组成的:'aaa','bb','c'。牛牛现在给定一个字符串,请你帮助计算这个字符串的所有碎片的平均长度是多少。
#
# 输入描述:
# 输入包括一个字符串s,字符串s的长度length(1 ≤ length ≤ 50),s只含小写字母('a'-'z')
#
#
# 输出描述:
# 输出一个整数,表示所有碎片的平均长度,四舍五入保留两位小数。
#
# 如样例所示: s = "aaabbaaac"
# 所有碎片的平均长度 = (3 + 2 + 3 + 1) / 4 = 2.25
#
# 输入例子1:
# aaabbaaac
#
# 输出例子1:
# 2.25
import sys

def input():
    num = sys.stdin.readline()
    return num


def zifu(inp):
    L = 1
    TL = []
    count = 0
    for i in range(1, len(inp)):
        if inp[i] == inp[i-1]:
            L = L + 1
            continue
        else:
            TL.append(L)
            count = count + 1
            L = 1

    sum1 = sum(TL) / float(count)

    return "%.2f" % sum1

if __name__=='__main__':
    print(zifu(input()))