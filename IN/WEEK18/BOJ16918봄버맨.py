import sys

input = sys.stdin.readline

r, c, n = map(int, input().split())

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

world = [[0] * c for _ in range(r)]
timer = [[0] * c for _ in range(r)]

for i in range(r):
    tmp = input().rstrip()
    for j in range(len(tmp)):
        if tmp[j] == ".":
            world[i][j] = 0
        else:
            world[i][j] = 1
            timer[i][j] = 2 

n -= 1

while n > 0:
    for i in range(r):
        for j in range(c):
            if world[i][j] == 0:
                world[i][j] = 1
                timer[i][j] = 3
            else:
                timer[i][j] -= 1
    n -= 1
    if n == 0:
        break
    boom = []
    for i in range(r):
        for j in range(c):
            if world[i][j] == 1:
                timer[i][j] -= 1
                if timer[i][j] == 0:
                    boom.append((i,j))
    while boom:
        i, j = boom.pop()
        for k in range(4):
            y, x = i+dy[k], j+dx[k]
            if 0 <= y < r and 0 <= x < c:
                world[y][x] = 0
                timer[y][x] = 0
        world[i][j] = 0
        timer[i][j] = 0
    n -= 1
    
for i in range(r):
    for j in range(c):
        if world[i][j] == 1:
            print("O", end="")
        else:
            print(".", end="")
    print()