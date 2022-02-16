import sys
from collections import deque
input = sys.stdin.readline
M, N = map(int, input().split())
graph = [[] for i in range(N)]
tomato = deque()
for i in range(N):
    graph[i] = list(map(int, input().split()))
    for j in range(M):
        if graph[i][j] == 1:
            x = i
            y = j
            tomato.append((x, y))
def bfs():
    cnt = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while tomato:
        cnt += 1
        for _ in range(len(tomato)):
            x, y = tomato.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0:
                    graph[nx][ny] = graph[nx][ny] + 1
                    tomato.append((nx, ny))
    for k in graph:
        if 0 in k:
            return -1
    return cnt-1
print(bfs())