from collections import deque
M,N,K = map(int,input().split())  
array = [[0] * M for _ in range(N)]
for i in range(K):
    x1,y1,x2,y2 = map(int,input().split())
    for j in range(x1,x2):
        for k in range(y1,y2):
            array[j][k] = 1

visited = [[0] * M for _ in range(N)]

dx = [0,0,-1,1]
dy = [1,-1,0,0]
ans = []
def bfs(x,y,visited):
    q = deque()
    q.append((x,y))
    visited[x][y] = 1
    cnt = 1
    while q: 
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<M:
                if array[nx][ny] == 0 and visited[nx][ny] == 0:
                    cnt += 1
                    visited[nx][ny] = 1
                    q.append((nx,ny))
    ans.append(cnt)
for i in range(N):
    for j in range(M):
        if array[i][j] == 0 and visited[i][j] == 0:
            bfs(i,j,visited)
ans.sort()
print(len(ans))
for i in ans:
    print(i, end = ' ')







