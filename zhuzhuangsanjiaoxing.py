import sys

def in_put():
    lines = sys.stdin.readlines()
    n = int(lines[0].strip('\n'))
    L = lines[1].strip('\n').split(' ')
    L = [int(i) for i in L]
    return L


def zhuzhuang_sanjiaoxing(nl):
    n = len(nl)
    tl = []
    for i in range(n-2):
        for j in range(i+1,n-1):
            minL = max(0, abs(nl[i]-nl[j]))
            maxL = nl[i] + nl[j]
            for k in range(j+1,n):
                if nl[k] < maxL and nl[k] > minL:
                    tl.append([nl[i],nl[j],nl[k]])
    return len(tl)



if __name__ == '__main__':
    print(zhuzhuang_sanjiaoxing(in_put()))