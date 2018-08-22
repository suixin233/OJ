# 如果我们有面值为1元、3元和5元的硬币若干枚，如何用最少的硬币凑够11元？ (表面上这道题可以用贪心算法，但贪心算法无法保证可以求出解，比如1元换成2元的时候)

want = 20
coin = [1, 3, 5]
score = [10000 for col in range(want + 1)]

score[0] = 0
for i in range(want + 1):
    for j in range(len(coin)):
        if coin[j] <= i and score[i - coin[j]] + 1 < score[i]:
            score[i] = score[i - coin[j]] + 1

for i in range(len(score)):
    print(str(i) + ' ' + str(score[i]))