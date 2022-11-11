from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
cnt = 0
graph=[]
for i in range(n):
    graph.append(list(map(int, input().split())))
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs():
    d = deque()
    d.append([0, 0])
    ch = [[-1]*m for _ in range(n)]
    ch[0][0] = 0
    while d:
        x, y = d.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if ch[nx][ny] == -1:
                    if graph[nx][ny] >= 1:
                        graph[nx][ny] += 1
                    else:
                        ch[nx][ny] = 0
                        d.append([nx, ny])

while True:
    bfs()
    k = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] >= 3:
                graph[i][j] = 0
                k = 1
            elif graph[i][j] == 2:
                graph[i][j] = 1
    if k == 1:
        cnt += 1
    else:
        break

print(cnt)