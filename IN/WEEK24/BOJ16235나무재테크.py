import sys
from collections import deque

input = sys.stdin.readline

dx = [0, 1, 0, -1, 1, -1, 1, -1]
dy = [1, 0, -1, 0, 1, -1, -1, 1]

n, m, k = map(int, input().split())

world = [[5] * n for _ in range(n)]
feed = [list(map(int, input().split())) for _ in range(n)]

trees = [[deque() for _ in range(n)] for _ in range(n)]
insert = [[[] for _ in range(n)] for _ in range(n)]

for _ in range(m):
    y, x, age = map(int, input().split())
    insert[y-1][x-1].append(age)

for i in range(n):
    for j in range(n):
        insert[i][j].sort()
        
for i in range(n):
    for j in range(n):
        for z in insert[i][j]:
            trees[i][j].append((z,1))

for year in range(1, k+1):
    die = []
    fall = []

    for i in range(n):
        for j in range(n):
            while trees[i][j]:
                age, cur = trees[i][j].popleft()
                if cur > year:
                    trees[i][j].appendleft((age, cur))
                    break
                if age > world[i][j]:
                    die.append((age, i, j))
                else:
                    world[i][j] -= age
                    trees[i][j].append((age+1, cur+1))
                    if (age+1) % 5 == 0:
                        fall.append((i, j, cur+1))
    while die:
        age, y, x = die.pop()
        world[y][x] += age // 2
        
    while fall:
        y, x, cur = fall.pop()
        for i in range(8):
            ny, nx = y+dy[i], x+dx[i]
            if 0 <= ny < n and 0 <= nx < n:
                trees[ny][nx].appendleft((1, cur))
        
    for i in range(n):
        for j in range(n):
            world[i][j] += feed[i][j]

cnt = 0
for i in range(n):
    for j in range(n):
        cnt += len(trees[i][j])

print(cnt)