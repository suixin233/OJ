l = [5, 3, 4, 8, 6, 7, 4, 3, 8, 9, 4, 4, 11, 12, 1, 20]
n = len(l)
d = [1 for i in l]

for i in range(n):
    for j in range(1, i):
        if l[j] <= l[i] and d[j] + 1 > d[i]:
            d[i] = d[j] + 1
        if d[i] > n:
            d[i] = n

for i in range(len(d)):
    print(str(i) + ' ' + str(d[i]))