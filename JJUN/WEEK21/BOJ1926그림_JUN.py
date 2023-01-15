import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n, m = map(int, input().split())
paint = []
num = [0 for _ in range((max(n, m)**2))]
for i in range(n):
    paint.append(list(map(int, input().split())))

def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if paint[x][y] == 1:
        paint[x][y] = 0
        num[result] += 1
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1
if result == 0:
    print(0)
    print(0)
else:
    size = 0
    for i in range(result):
        if num[i] > size:
            size = num[i]
    print(result)
    print(size)