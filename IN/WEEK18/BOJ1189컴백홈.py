import sys

input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

r, c, k = map(int, input().split())

world = []

for _ in range(r):
    world.append(input().rstrip())
    
ans = 0

visited = [[0] * c for _ in range(r)]
visited[r-1][0] = True
def find(y, x, k): 
    global ans
    if k == 1:
        if y == 0 and x == c-1:
            ans += 1
            return
        else:
            return
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < c and 0 <= ny < r:
            if world[ny][nx] != "T":
                if not visited[ny][nx]:
                    visited[ny][nx] = True
                    find(ny, nx, k-1)
                    visited[ny][nx] = False

find(r-1,0,k)
print(ans)