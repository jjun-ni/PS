from collections import deque
T = int(input())
def chess(size,x,y,x_f,y_f):
    world = [[0 for _ in range(size)]for _ in range(size)]
    visited =[[0 for _ in range(size)]for _ in range(size)]
    q = deque()
    q.append((x,y))
    visited[x][y] = 1
    dx = [1,1,2,2,-1,-2,-1,-2]
    dy = [2,-2,1,-1,2,1,-2,-1]
    while q:
        x,y = q.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < size and 0 <= ny < size and visited[nx][ny] == 0:
                if nx == x_f and ny == y_f:
                    world[nx][ny] = world[x][y] + 1
                    return world[nx][ny]
                else:
                    world[nx][ny] = world[x][y] + 1
                    visited[nx][ny] = 1
                    q.append((nx,ny))
for _ in range(T):
    case = []
    size = int(input())
    case.append(list(map(int,input().split())))
    case.append(list(map(int,input().split())))
    if case[0][0] == case[1][0] and case[0][1] == case[1][1]:
        print(0)
    else:
        print(chess(size,case[0][0],case[0][1],case[1][0],case[1][1]))
    


        

