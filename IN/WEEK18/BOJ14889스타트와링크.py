import sys
from itertools import combinations

input = sys.stdin.readline

n = int(input())
power = []

for _ in range(n):
    power.append(list(map(int, input().split())))

teams = combinations(range(n), n//2)
min_diff = int(1e9)
for start in teams:
    link = []
    power_s = 0
    power_l = 0
    for i in range(n):
        if i not in start:
            link.append(i)
    for i in start:
        for j in start:
            power_s += power[i][j]
    for i in link:
        for j in link:
            power_l += power[i][j]
    diff = abs(power_s - power_l)
    min_diff = min(min_diff, diff)
print(min_diff)