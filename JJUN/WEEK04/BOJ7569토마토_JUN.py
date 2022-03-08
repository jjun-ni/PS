import sys
from collections import deque
input = sys.stdin.readline
M, N, H= map(int, input().split())
graph = [[] for i in range(H)]
tomato = deque()
for i in range(H):
    for j in range(N):
        graph[i].append(list(map(int, input().split())))
        for k in range(M):
            if graph[i][j][k] == 1:
                tomato.append((i, j, k))
def bfs():
    cnt = 0
    dx = [-1, 1, 0, 0, 0, 0]
    dy = [0, 0, -1, 1, 0, 0]
    dz = [0, 0, 0, 0, -1, 1]
    while tomato:
        cnt += 1
        for _ in range(len(tomato)):
            z, x, y = tomato.popleft()
            for i in range(6):
                nx = x + dx[i]
                ny = y + dy[i]
                nz = z + dz[i]
                if 0 <= nx < N and 0 <= ny < M and 0 <= nz < H and graph[nz][nx][ny] == 0:
                    graph[nz][nx][ny] = graph[nz][nx][ny] + 1
                    tomato.append((nz, nx, ny))
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if graph[i][j][k] == 0:
                    return -1
    return cnt-1
print(bfs())