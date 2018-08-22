import sys

def in_put():
    lines = sys.stdin.readlines()
    n = int(lines[0].strip('\n'))
    nl = []
    for i in range(n):
        nl.append(int(lines[i+1].strip('\n')))
    return nl


def tongjijishu(number):
    length = len(str(number))
    res = number - (10**(length-1) - 1)
    sum = 0
    for i in range(1,length):
        sum = sum + i * ((10**(i-1)) * 9)
    sum = sum + res * length
    return sum

if __name__ == '__main__':
    nl = in_put()
    for i in nl:
        print(tongjijishu(i))