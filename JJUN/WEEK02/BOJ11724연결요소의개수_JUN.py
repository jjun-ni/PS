import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())
graph = [[] for i in range(N+1)]
visit = [0 for i in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
connection = 0
def bfs(graph, start, visit):
    queue = deque([start])
    visit[start] = 1
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if visit[i] == 0:
                queue.append(i)
                visit[i] = 1
    return 0
for i in range(1, N+1):
    if visit[i] == 0:
        connection += 1
        bfs(graph, i, visit)
print(connection)