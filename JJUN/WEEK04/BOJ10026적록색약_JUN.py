import sys
sys.setrecursionlimit(10**9)
from collections import deque
input = sys.stdin.readline
N = int(input())
grid = []
for i in range(N):
    grid.append(list(map(str, input().strip())))
visited = [[False] * N for _ in range(N)]
ab_visited = [[False] * N for _ in range(N)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
def normal(x, y):
    k = grid[x][y]
    if visited[x][y] == False:
        visited[x][y] = True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and grid[nx][ny] == k:
                normal(nx, ny)
        return True
    return False

def abnormal(x, y):
    k = grid[x][y]
    if ab_visited[x][y] == False:
        ab_visited[x][y] = True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if k == 'R' or k == 'G':
                    if grid[nx][ny] == 'R' or grid[nx][ny] == 'G':
                        abnormal(nx, ny)
                else:
                    if 0 <= nx < N and 0 <= ny < N and grid[nx][ny] == k:
                        abnormal(nx, ny)
        return True
    return False

normal_result, abnormal_result = 0, 0
for i in range(N):
    for j in range(N):
        if normal(i, j) == True:
            normal_result += 1
for i in range(N):
    for j in range(N):
        if abnormal(i, j) == True:
            abnormal_result += 1
print(normal_result, abnormal_result)