import sys
from bisect import bisect_left

input = sys.stdin.readline

n = int(input())

lines = []

for _ in range(n):
    a, b = map(int, input().split())
    lines.append((a, b))
    
lines.sort()
dp = []
dp.append(lines[0][1])

for i in range(1,n):
    num = lines[i][1]
    if dp[-1] < num:
        dp.append(num)
    else:
        idx = bisect_left(dp, num)
        dp[idx] = num
        
print(n-len(dp))