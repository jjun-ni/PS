import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
arr.insert(0, 0)
dy = [0] * (N+1)
dy[1] = 1
res = 0
for i in range(2, N+1):
    maximum = 0
    for j in range(i-1, 0, -1):
        if arr[j] < arr[i] and dy[j] > maximum:
            maximum = dy[j]
    dy[i] = maximum+1
    if dy[i] > res:
        res = dy[i]
if N == 1:
    print(1)
else:
    print(res)