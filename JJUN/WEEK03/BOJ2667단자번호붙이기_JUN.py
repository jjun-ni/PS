import sys
import heapq
input = sys.stdin.readline
N = int(input())
graph = []
num = [0 for _ in range(N**2)]
for i in range(N):
    graph.append(list(map(int, input().strip())))
def dfs(x, y):
    if x <= -1 or x >= N or y <= -1 or y >= N:
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

result = 0
for i in range(N):
    for j in range(N):
        if dfs(i, j) == True:
            result += 1
print(result)
heap = []
for i in range(result):
    heapq.heappush(heap, num[i])
for i in range(result):
    print(heapq.heappop(heap))