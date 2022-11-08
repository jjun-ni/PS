import sys

sys.setrecursionlimit(10**8)

input = sys.stdin.readline

MOD = 1000000000

n = int(input())

dp = [[0] * 10 for _ in range(n)]
for i in range(1, 10):
    dp[0][i] = 1
for i in range(1,n):
    for j in range(10):
        if j == 0:
            dp[i][j] = (dp[i][j] + dp[i-1][1]) % MOD
        elif j == 9:
            dp[i][j] = (dp[i][j] + dp[i-1][8]) % MOD
        else:
            dp[i][j] = (dp[i][j] + dp[i-1][j+1]) % MOD
            dp[i][j] = (dp[i][j] + dp[i-1][j-1]) % MOD
            
res = 0
for i in range(10):
    res = (res + dp[n-1][i]) % MOD
print(res)
