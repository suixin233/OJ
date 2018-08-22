stairs = 20

def climbstairs(n):
    dp = [1 for i in range(n+1)]
    dp[0] = 0
    for i in range(2,n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp

dp = climbstairs(stairs)
for i in range(len(dp)):
    print(str(i) + ' ' + str(dp[i]))