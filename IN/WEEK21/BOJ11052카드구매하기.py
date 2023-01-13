import sys

input = sys.stdin.readline

n = int(input())

cost = [0] + list(map(int, input().split()))

dp = [0] * (n+1)

for i in range(len(cost)):
    dp[i] = cost[i]

for i in range(1,n+1):
    for j in range(1, i):
        dp[i] = max(dp[i], dp[j] + dp[i-j])
print(dp[n])