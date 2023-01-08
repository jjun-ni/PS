import sys
from itertools import combinations
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
INF = int(1e10)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

state = [list(map(int, input().split())) for _ in range(n)]

enable_virus = []
cnt_zero = 0
for i in range(n):
    for j in range(n):
        if state[i][j] == 2:
            enable_virus.append((i, j))
        elif state[i][j] == 0:
            cnt_zero += 1
            
active_virus = combinations(enable_virus, m)
min_time = INF

for active in active_virus:
    visited = [[INF] * n for _ in range(n)]
    deq = deque()
    for y, x in active:
        visited[y][x] = 0
        deq.append((y, x, 0))
    expand_zero = 0
    local_time = 0 
    while deq:
        y, x, t = deq.popleft()
        if state[y][x] == 0:
            expand_zero += 1
            local_time = max(local_time, t)
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if 0 <= ny < n and 0 <= nx < n:
                if state[ny][nx] != 1:
                    if visited[ny][nx] == INF:
                        visited[ny][nx] = t+1
                        deq.append((ny, nx, t+1))
    if expand_zero == cnt_zero:
        min_time = min(local_time, min_time)
print(min_time) if min_time < INF else print(-1)