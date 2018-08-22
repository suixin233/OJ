import sys

def in_put():
    lines = sys.stdin.readlines()
    n = int(lines[0].strip('\n'))
    words = []
    for i in range(n):
        words.append(lines[i+1].strip('\n'))
    return words


def xunhuandanci_judge(words):
    n = len(words)
    store = []
    for i in range(n):
        word = words[i]
        doubleWord = word + word
        if len(store) == 0:
            store.append(doubleWord)
            continue
        count = 0
        for dw in store:
            if word in dw and len(word) == int(len(dw)/2):
                count = count + 1
                break
        if count == 0:
            store.append(doubleWord)
    return len(store)


if __name__ == '__main__':
    print(xunhuandanci_judge(in_put()))