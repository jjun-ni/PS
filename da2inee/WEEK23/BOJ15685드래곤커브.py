N = int(input())
world = [[0] * 101 for _ in range(101)]
dx = [1,0,-1,0]
dy = [0,-1,0,1]
for i in range(N):
    x,y,d,g = map(int,input().split())
    world[x][y] = 1
    curve = [d]
    for j in range(g):
        ans = []
        for k in range(len(curve)):
            ans.append((curve[-k-1] + 1) % 4)
        curve.extend(ans)
    for j in range(len(curve)):
        nx = x + dx[curve[j]]
        ny = y + dy[curve[j]]
        world[nx][ny] = 1
        x, y = nx, ny
cnt = 0
for i in range(100):
    for j in range(100):
        if world[i][j] == 1 and world[i+1][j] == 1 and world[i][j+1] and world[i+1][j+1]:
            cnt += 1
print(cnt) 
