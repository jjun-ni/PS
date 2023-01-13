import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

n, m = map(int, input().split())

drawing = [list(map(int, input().split())) for _ in range(n)]

visited = [[0] * m for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def find_conn(y, x):
    res = 1
    for i in range(4):
        ny, nx = y+dy[i], x+dx[i]
        if 0 <= ny < n and 0 <= nx < m:
            if drawing[ny][nx] == 1:
                if not visited[ny][nx]:
                    visited[ny][nx] = 1
                    res += find_conn(ny, nx)
    return res

max_cnt = 0
drawing_cnt = 0
for i in range(n):
    for j in range(m):
        if drawing[i][j] == 1:
            if not visited[i][j]:
                visited[i][j] = 1
                drawing_cnt += 1
                cnt = find_conn(i,j)
                if cnt > max_cnt:
                    max_cnt = cnt
                    
print(drawing_cnt)
print(max_cnt)
            