N,M = map(int,input().split())
x,y,direction = map(int,input().split())
world = []
for i in range(N):
    world.append(list(map(int,input().split())))
dx = [0,1,0,-1]
dy = [-1,0,1,0]

direction = 3 - direction
world[x][y] = 2
while 1:
    flag = 0
    for k in range(1,5):
        d = (direction + k) % 4
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx <  N and 0 <= ny < M:
            if world[nx][ny] == 0:
                world[nx][ny] = 2
                x = nx
                y = ny
                direction = d
                flag = 1
                break
    if flag == 0:
        if world[x + dx[(d+2)%4]][y + dy[(d+2)%4]] == 1:
            break
        else:
            x = x + dx[(d+2)%4]
            y = y + dy[(d+2)%4]
cnt = 0
for i in range(N):
    for j in range(M):
        if world[i][j] == 2:
            cnt +=1
print(cnt)



