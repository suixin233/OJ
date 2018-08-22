
A = [[1, 2, 1, 0, 2],
     [0, 0, 3, 1, 2],
     [1, 4, 5, 2, 3]]
S = [[0 for row in range(5)] for col in range(3)]

S[0][0] = A[0][0]
for i in range(3):
    for j in range(5):
        if i == 0 and j != 0:
            S[i][j] = A[i][j] + S[i][j-1]
        elif i!= 0 and j==0:
            S[i][j] = A[i][j] + S[i-1][j]
        else:
            S[i][j] = A[i][j] + max([S[i][j-1], S[i-1][j]])

print(S)