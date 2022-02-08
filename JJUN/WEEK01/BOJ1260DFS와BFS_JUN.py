from collections import deque
import sys
input = sys.stdin.readline
N, M, V = map(int, input().split())
graph = [[] for N in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in graph:
    i.sort()
def dfs(graph, v, dfsvisit):
    dfsvisit[v] = True
    print(v, end =' ')
    for i in graph[v]:
        if not dfsvisit[i]:
            dfs(graph, i, dfsvisit)
def bfs(graph, start, bfsvisit):
    queue = deque([start])
    bfsvisit[start]= True
    while queue:
        v = queue.popleft()
        print(v, end =' ')
        for i in graph[v]:
            if not bfsvisit[i]:
                queue.append(i)
                bfsvisit[i] = True
dfsvisit = [False] * (N+1)
bfsvisit = [False] * (N+1)
dfs(graph, V, dfsvisit)
print()
bfs(graph, V, bfsvisit)