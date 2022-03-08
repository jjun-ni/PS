import sys
input = sys.stdin.readline
n = int(input())
dp = [[0]]
for i in range(1, n+1):
    dp.append([0 for j in range(i)])
triangle = [[0]]
for i in range(n):
    triangle.append(list(map(int, input().split())))
for i in range(1, n+1):
    for j in range(i):
        if j == 0:
            dp[i][j] = dp[i-1][0] + triangle[i][0]
        elif j == i-1:
            dp[i][j] = dp[i-1][j-1] + triangle[i][j]
        else:
            dp[i][j] = triangle[i][j] + max(dp[i-1][j-1], dp[i-1][j])
print(max(dp[n]))