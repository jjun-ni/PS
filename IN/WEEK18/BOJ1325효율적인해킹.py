import sys
from collections import deque

input = sys.stdin.readline


n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    start, end = map(int, input().split())
    graph[end].append(start)

def bfs(v):
    visited = [False] * (n+1)
    visited[v] = True
    need_visit = deque([v])
    count = 1
    while need_visit:
        current = need_visit.popleft()
        for next in graph[current]:
            if not visited[next]:
                need_visit.append(next)
                visited[next] = True
                count += 1
    return count

max_ind = []
max_count = -1
for i in range(1, n+1):
    cnt = bfs(i)
    if cnt == max_count:
        max_ind.append(i)
    elif cnt > max_count:
        max_count = cnt
        max_ind = [i]
max_ind.sort()
for i in max_ind:
    print(i, end=" ")