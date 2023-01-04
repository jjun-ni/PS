import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

n, m, k = map(int, input().split())

world = [[0] * m for _ in range(n)]
visited = [[0] * m for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for _ in range(k):       
    lx, ly, rx, ry = map(int, input().split())
    for i in range(ly, ry):
        for j in range(lx, rx):
            world[i][j] = 1

def find_conn(y, x):
    res = 1
    for i in range(4):
        ny, nx = y+dy[i], x+dx[i]
        if 0 <= ny < n and 0 <= nx < m:
            if world[ny][nx] == 0:
                if not visited[ny][nx]:
                    visited[ny][nx] = 1
                    res += find_conn(ny, nx)
    return res

cnt_drawing = 0
areas = []
                    
for i in range(n):
    for j in range(m):
        if world[i][j] == 0:
            if not visited[i][j]:
                cnt_drawing += 1
                visited[i][j] = 1
                areas.append(find_conn(i,j))
areas.sort()
print(cnt_drawing)
for i in areas:
    print(i, end=" ")