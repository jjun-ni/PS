import sys
input = sys.stdin.readline
n = int(input())
box = list(map(int, input().split()))
box.insert(0, 0)
dy = [0] * (n+1)
dy[1] = 1
res = 0
for i in range(2, n+1):
    maximum = 0
    for j in range(i-1, 0, -1):
        if box[j] < box[i] and dy[j] > maximum:
            maximum = dy[j]
    dy[i] = maximum+1
    if dy[i] > res:
        res = dy[i]
if n == 1:
    print(1)
else:
    print(res)