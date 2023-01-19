import sys
from collections import deque

input = sys.stdin.readline

dx = [1, 1, 2, 2, -1, -1, -2, -2]
dy = [2, -2, 1, -1, 2, -2, 1, -1]

t = int(input())

for _ in range(t):
    l = int(input())
    sy, sx = map(int, input().split())
    ey, ex = map(int, input().split())
    visited = [[0] * l for _ in range(l)]
    visited[sy][sx] = 1
    deq = deque()
    deq.append((1, sy, sx))
    
    while deq:
        cnt, y, x = deq.popleft()
        if y == ey and x == ex:
            break
        for i in range(8):
            ny, nx = y+dy[i], x+dx[i]
            if 0 <= ny < l and 0 <= nx < l:
                if not visited[ny][nx]:
                    visited[ny][nx] = cnt + 1
                    deq.append((cnt+1, ny, nx))
                    
    print(visited[ey][ex] - 1)