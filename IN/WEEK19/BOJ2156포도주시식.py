import sys

input = sys.stdin.readline

n = int(input())

size = [0]
for _ in range(n):
    size.append(int(input()))
    
dp = [0] * (n+1)
dp[1] = size[1]
if n == 1:
    print(size[1])
else:
    dp[2] = size[1] + size[2]
    for i in range(3, n+1):
        dp[i] = max(size[i]+dp[i-2], size[i]+size[i-1]+dp[i-3], dp[i-1])
    print(max(dp))