import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        elif Map[nx][ny] < Map[x][y]:
            if visited[]


if __name__ == '__main__':
    n, m = map(int, input().split())
    Map = [[] for i in range(n)]
    for i in range(n):
        Map[i] = list(map(int, input().split()))
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    dp = [[0] * m for i in range(n)]
    visited = [[0] * m for i in range(n)]
    dfs(0, 0)
    print(dp[n-1][m-1])