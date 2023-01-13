import sys
from itertools import permutations

input = sys.stdin.readline

k = int(input())
compare = list(input().split())

max_num = 0
min_num = int(1e11)

candidates = permutations(range(10), k+1)

for candidate in candidates:
    cnt = 0
    for i in range(k):
        num = candidate[i]
        next_num = candidate[i+1]
        if compare[i] == ">":
            if num < next_num:
                break
            else:
                cnt += 1
        else:
            if num > next_num:
                break
            else:
                cnt += 1
    if cnt == k:
        int_num = 0
        for n in candidate:
            int_num = int_num * 10 + n
        max_num = max(max_num, int_num)
        min_num = min(min_num, int_num)

print(max_num)
if len(str(max_num)) != len(str(min_num)):
    print("0" + str(min_num))
else:
    print(min_num)