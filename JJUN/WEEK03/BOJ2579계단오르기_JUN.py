import sys
input = sys.stdin.readline
n = int(input())
point = [0]
for i in range(n):
    point.append(int(input()))
dp = [0] * (n+1)
dp[0] = [0, 0]
if n >= 1:
    dp[1] = [point[1], point[1]]
if n >= 2:
    dp[2] = [point[2], point[1]+point[2]]
if n >= 3:
    dp[3] = [point[1]+point[3], point[2]+point[3]]
if n >= 4:
    for i in range(4, n+1):
        dp[i] = [point[i]+point[i-2]+max(dp[i-3][0],max(dp[i-4][0], dp[i-4][1])), point[i]+point[i-1]+max(dp[i-3][0], dp[i-3][1])]
print(max(dp[n][0], dp[n][1]))