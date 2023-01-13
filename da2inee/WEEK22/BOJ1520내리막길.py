## 나중에 다시풀기
M,N = map(int,input().split())
world = []
for i in range(M):
    world.append(list(map(int,input().split())))
dp = [[-1] * N for _ in range(M)]
dx = [0,0,-1,1]
dy = [1,-1,0,0]
def dfs(x,y):
    if x == M-1 and y == N-1:
        return 1
    if dp[x][y] != -1:
        return dp[x][y]
    else:
        dp[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < M and 0<= ny < N and world[nx][ny] < world[x][y]:
                dp[x][y] += dfs(nx,ny)
    return dp[x][y]
print(dfs(0,0))