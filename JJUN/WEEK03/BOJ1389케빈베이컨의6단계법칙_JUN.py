import sys
INF = int(1e9)
input = sys.stdin.readline
N, M = map(int, input().split())
graph = [[INF] * (N+1) for _ in range(N+1)]
for a in range(1, N+1):
    for b in range(1, N+1):
        if a == b:
            graph[a][b] = 0
for i in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

for k in range(1, N+1):
   for a in range(1, N+1):
       for b in range(1, N+1):
           graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])
kevin = []
for i in range(1, N+1):
    kevin_bacon = 0
    for j in range(1, N+1):
        kevin_bacon += graph[i][j]
    kevin.append(kevin_bacon)
minimum = min(kevin)
print(kevin.index(minimum)+1)