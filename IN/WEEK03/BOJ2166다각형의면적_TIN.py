import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

pointx = []
pointy = []

for _ in range(n):
    x, y = map(int, input().split())
    pointx.append(x)
    pointy.append(y)

sum = 0
for i in range(n-1):
    sum += pointx[i] * pointy[i+1]
sum += pointx[-1] * pointy[0]
for i in range(n-1):
    sum -= pointx[i+1] * pointy[i]
sum -= pointy[-1] * pointx[0]
sum = abs(sum)
sum /= 2
print(sum)