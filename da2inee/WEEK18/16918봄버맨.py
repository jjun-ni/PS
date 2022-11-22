R,C,N = map(int,input().split())
world = [[0]*C for i in range(R)]
array = [list(map(str, list(input()))) for _ in range(R)]
cnt =[[0]*C for i in range(R)]
for i in range(R):
    for j in range(C):
        if array[i][j] == "O":
            world[i][j] = 1
            cnt[i][j] = 2
dx = [0,0,-1,1]
dy = [1,-1,0,0]
N -= 1
while N > 0:
    for i in range(R):
        for j in range(C):
            if world[i][j] == 0:
                world[i][j] = 1
                cnt[i][j] = 3
            else:
                cnt[i][j] -= 1
    N -= 1
    if N == 0:
        break
    for i in range(R):
        for j in range(C):
            cnt[i][j] -= 1
            if cnt[i][j] == 0:
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    world[i][j] = 0
                    if 0<=nx<R and 0<=ny<C:
                        world[nx][ny] = 0
    N-=1
for i in range(R):
    for j in range(C):
        if world[i][j] == 1:
            print("O", end = "")
        else:
            print(".", end = "")
    print()



        



