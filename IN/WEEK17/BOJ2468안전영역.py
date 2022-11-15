import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

n = int(input())
world = [list(map(int, input().split())) for _ in range(n)]

def safe_zone(x, y, visited, height):
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if world[ny][nx] > height:
                if not visited[ny][nx]:
                    visited[ny][nx] = True
                    safe_zone(nx, ny, visited, height)

max_safe_zone = 0
for i in range(max(max(world))):
    height = i
    visited = [[False] * n for _ in range(n)]
    cnt = 0
    for y in range(n):
        for x in range(n):
            if world[y][x] > height and not visited[y][x]:
                visited[y][x] = True
                cnt += 1
                safe_zone(x, y, visited, height)
    if cnt > max_safe_zone:
        max_safe_zone = cnt
print(max_safe_zone)
