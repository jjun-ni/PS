from collections import deque
N = int(input())
world = []
for i in range(N):
    world.append(list(input()))

dx = [1,-1,0,0]
dy = [0,0,-1,1]

def color(a,b,visited):
    q = deque()
    q.append((a,b))
    visited[a][b] = 1
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<N:
                if visited[nx][ny] == 0 and world[nx][ny] == world[x][y]:
                    q.append((nx,ny))
                    visited[nx][ny] = 1
cnt = 0
visited = [[0]*N for i in range(N)]
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0 :
            color(i,j,visited)
            cnt +=1
print(cnt,end = " ")

for i in range(N):
    for j in range(N):
        if world[i][j] =="R":
            world[i][j] = "G"
visited = [[0]*N for i in range(N)]
cnt = 0
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0 :
            color(i,j,visited)
            cnt +=1
print(cnt)


