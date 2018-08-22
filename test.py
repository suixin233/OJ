import sys

def in_put():
    lines = sys.stdin.readlines()
    res = []
    for line in lines:
        sample = line.strip('\n').split(' ')
        sample = [int(i) for i in sample]
        res.append(sample)
    return res

if __name__ == '__main__':
    samples = in_put()
    for sample in samples:
        print(str(sample[0]+sample[1]))