import sys

input = sys.stdin.readline

target = input().rstrip()

size = len(target)
min_change = int(1e9)
cnt_a = target.count('a')

for i in range(size):
    cnt = 0
    for j in range(i, i+cnt_a):
        idx = j % size
        if target[idx] == 'b':
            cnt += 1
    min_change = min(min_change, cnt)

print(min_change)