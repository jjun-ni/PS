import sys

sys.setrecursionlimit(10**8)

input = sys.stdin.readline
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

r, c = map(int, input().split())

world = [input().rstrip() for _ in range(r)]

def search(y, x, visited):
    sheep = 0
    wolf = 0
    if world[y][x] == 'v': wolf += 1
    elif world[y][x] == 'o': sheep += 1
    for i in range(4):
        ny, nx = y+dy[i], x+dx[i]
        if 0 <= ny < r and 0 <= nx < c:
            if world[ny][nx] != '#':
                if not visited[ny][nx]:
                    visited[ny][nx] = True
                    n_sheep, n_wolf = search(ny, nx, visited)
                    sheep += n_sheep 
                    wolf += n_wolf
    return sheep, wolf 

visited = [[False] * c for _ in range(r)]
total_sheep = 0
total_wolf = 0
for i in range(r):
    for j in range(c):
        if world[i][j] != '#':
            if not visited[i][j]:
                visited[i][j] = True
                sheep, wolf = search(i, j, visited)
                if sheep > wolf:
                    total_sheep += sheep
                else:
                    total_wolf += wolf
print(total_sheep, total_wolf)