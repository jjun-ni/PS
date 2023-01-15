import sys
from collections import deque
import heapq
input = sys.stdin.readline
m, n, k = map(int, input().split())
num = [0 for _ in range(max(n,m)**2)]
graph = [[1] * n for _ in range(m)]
dx = [0, 1]
dy = [1, 0]
def erase(a, b):
    rect = deque()
    rect.append((a, b))
    while rect:
        y, x = rect.popleft()
        graph[x][y] = 0
        for i in range(2):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= d or ny >= c:
                continue
            else:
                graph[nx][ny] = 0
                rect.append((ny, nx))

for i in range(k):
    a, b, c, d = map(int, input().split())
    erase(a, b)

def dfs(x, y):
    if x <= -1  or x >= m or y <= -1 or y >= n:
        return False
    if graph[x][y] == 1:
        num[result] += 1
        graph[x][y] = 0
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

print(graph)

result = 0
for i in range(m):
    for j in range(n):
        if dfs(i, j) == True:
            result += 1

heap = []
print(result)
for i in range(result):
    heapq.heappush(heap, num[i])
for i in range(result):
    print(heapq.heappop(heap))
