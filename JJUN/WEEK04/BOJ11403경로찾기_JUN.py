import sys
input = sys.stdin.readline
INF = 1e9
N = int(input())
method = [[INF] * (N) for _ in range(N)]
for i in range(N):
    k = list(map(int, input().split()))
    for j in range(N):
        if k[j] == 1:
            method[i][j] = 1
for i in range(N):
    for j in range(N):
        for k in range(N):
            method[j][k] = min(method[j][k], method[j][i]+method[i][k])
for i in range(N):
    for j in range(N):
        if method[i][j] != INF:
            method[i][j] = 1
        else:
            method[i][j] = 0
for i in range(N):
    for j in range(N):
        print(method[i][j], end=' ')
    print()