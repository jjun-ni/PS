import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
T = int(input())
for t in range(T):
    M, N, K = map(int, input().split())
    graph = [[0]*M for i in range(N)]
    for i in range(K):
        j, k = map(int, input().split())
        graph[k][j] = 1
    caterpillar = 0
    def dfs(x, y):
        if x <= -1 or x >= N or y <= -1 or y >= M:
            return False
        if graph[x][y] == 1:
            graph[x][y] = 0
            dfs(x-1, y)
            dfs(x, y+1)
            dfs(x+1, y)
            dfs(x, y-1)
            return True
        return False
    for b in range(N):
        for a in range(M):
            if dfs(b, a) == True:
                caterpillar += 1
    print(caterpillar)