# 小易有一个长度为N的正整数数列A = {A[1], A[2], A[3]..., A[N]}。
# 牛博士给小易出了一个难题:
# 对数列A进行重新排列,使数列A满足所有的A[i] * A[i + 1](1 ≤ i ≤ N - 1)都是4的倍数。
# 小易现在需要判断一个数列是否可以重排之后满足牛博士的要求。
# 输入描述:
# 输入的第一行为数列的个数t(1 ≤ t ≤ 10),
# 接下来每两行描述一个数列A,第一行为数列长度n(1 ≤ n ≤ 10^5)
# 第二行为n个正整数A[i](1 ≤ A[i] ≤ 10^9)
#
#
# 输出描述:
# 对于每个数列输出一行表示是否可以满足牛博士要求,如果可以输出Yes,否则输出No。
#
# 输入例子1:
# 2
# 3
# 1 10 100
# 4
# 1 2 3 4
#
# 输出例子1:
# Yes
# No

import sys
import math

def in_put():
    lines = sys.stdin.readlines()
    sampleNumber = int(lines[0].strip('\n'))
    sampleList = []
    for i in range(sampleNumber):
        N = int(lines[2*i+1].strip('\n'))
        array = lines[2*i+2].strip('\n').split(' ')
        sample = [N, array]
        sampleList.append(sample)
    # print(str(n) + str(L) + str(str2))
    return sampleNumber, sampleList

def yi(SN, SL):
    J = []
    for sample in SL:
        number = sample[0]
        arr = sample[1]
        judge = {'NO':0, 'OK2':0, 'OK4':0}
        for n in arr:
            n = int(n)
            if n % 4 == 0:
                judge['OK4'] += 1
            elif n % 2 == 0:
                judge['OK2'] += 1
            else:
                judge['NO'] += 1
        if judge['OK2'] > 0:
            judge['OK4'] -= 1
        if judge['NO'] > (judge['OK4'] + 1):
            J.append('No')
        else:
            J.append('Yes')
    return J

if __name__=='__main__':
    [sampleNumber, sampleList] = in_put();
    for i in yi(sampleNumber, sampleList):
        print(i)