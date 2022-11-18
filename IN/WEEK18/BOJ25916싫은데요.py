import sys

input = sys.stdin.readline

n, m = map(int, input().split())
hole = list(map(int, input().split()))
sum_hole = [0] * (n+1)
sum_hole[1] = hole[0]
for i in range(1,n):
    sum_hole[i+1] = sum_hole[i] + hole[i]

flag1 = 1 
flag2 = 0 
max_size = 0
while flag1 <= n and flag2 <= n:
    if flag1 <= flag2:
        flag1 += 1
        continue
    hole_size = sum_hole[flag1] - sum_hole[flag2]
    if hole_size <= m:
        if max_size < hole_size:
            max_size = hole_size
        flag1 += 1
    else:
        flag2 += 1
print(max_size)