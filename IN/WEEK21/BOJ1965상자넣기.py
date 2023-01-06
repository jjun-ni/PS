import sys
from bisect import bisect_left

input = sys.stdin.readline

n = int(input())

boxes = list(map(int, input().split()))

dp = [boxes[0]]

for i in range(1, n):
    if boxes[i] > dp[-1]:
        dp.append(boxes[i])
    elif boxes[i] < dp[-1]:
        idx = bisect_left(dp, boxes[i])
        dp[idx] = boxes[i]

print(len(dp))