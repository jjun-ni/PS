from collections import deque
N,M = map(int,input().split())
world = []
for i in range(M):
    world.append(list(map(int,input().split())))
print(world)
visited = [[0]* N for _ in range(M)]
ans = [[10^6]* N for _ in range(M)]

dx = [0,0,-1,1]
dy = [1,-1,0,0]

def distance(a,b,visited):
    q = deque()
    q.append((a,b))
    visited[a][b] = 1
    ans[a][b] = 0
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < N and 0<=ny<M:
                if visited[nx][ny] == 0 and world[nx][ny] ==1:
                    for j in range(4):
                        xx = nx+dx[j]
                        yy = ny + dy[j]
                        if 0<= xx < N and 0<=yy<M:
                            ans[nx][ny] = min(ans[nx][ny],ans[xx][yy])+1
                            visited[nx][ny] = 1
                            q.append((nx,ny))
for i in range(M):
    for j in range(N):
        if world[i][j] == 2:
            distance(i,j,visited)
            print(ans)


