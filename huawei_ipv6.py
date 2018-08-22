import sys
import copy


def in_put():
    line = sys.stdin.readline()
    tmp = line.strip('\n').split(':')
    res = []
    zero = bin(int('0000',16))
    if '' in tmp:
        inx = tmp.index('')
        if tmp[0] == '':
            for i in range(7):
                res.append(zero)
            res.append(bin(int(tmp[2],16)))
            return res
        else:
            fill0 = 8 - len(tmp) + 1
            res = res + [bin(int(i, 16)) for i in tmp[:inx]]
            for i in range(fill0):
                res.append(zero)
                res = res + [bin(int(i, 16)) for i in tmp[inx+1:]]
            return res
    for i in tmp:
        res.append(bin(int(i,16)))
    return res

def ipv6(sample):
    fir = sample[0]
    n = len(sample)
    if n != 8:
        return 'Error'
    for i in range(n):
        if i < 7:
            if sample[i] == '0b0':
                continue
            else:
                break
        elif i == 7 and sample[i] == '0b0':
            return 'Unspecified'
        elif i == 7 and sample[i] == '0b1':
            return 'Loopback'

    if fir[2:12] == '1111111010':
        return 'LinkLocal'
    elif fir[2:12] == '1111111011':
        return 'SiteLocal'
    elif fir[2:10] == '11111111':
        return 'Multicast'
    elif fir != '0b0':
        return 'GlobalUnicast'
    else:
        return 'Error'



if __name__ == '__main__':
    print(ipv6(in_put()))