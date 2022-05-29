import sys
input = sys.stdin.readline
n = int(input())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, c):
    global pin_num, cnt
    if pin_num == 0 or pin_num > c:
        pin_num = c
        cnt = num - c

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx > 4 or ny > 8:
            continue
        elif board[nx][ny] == 'o':
            nnx = nx + dx[i]
            nny = ny + dy[i]
            if nnx < 0 or nny < 0 or nnx > 4 or nny > 8:
                continue
            elif board[nnx][nny] == '.':
                board[x][y] = board[nx][ny] = '.'
                board[nnx][nny] = 'o'
                for j in range(5):
                    for k in range(8):
                        if board[j][k] == 'o':
                            dfs(j, k, c-1)
            board[x][y] = board[nx][ny] = 'o'
            board[nnx][nny] = '.'


for i in range(n-1):
    pin_num, cnt = 0, 0
    pin = 0
    board = [[] for _ in range(5)]
    for j in range(5):
        board[j] = list(input().strip())
    b = input()
    for k in range(5):
        for l in range(8):
            if board[k][l] == 'o':
                pin += 1
    num = pin
    for k in range(5):
        for l in range(8):
            if board[k][l] == 'o':
                dfs(k, l, pin)
    print(pin_num, cnt)

for i in range(1):
    pin_num, cnt = 0, 0
    pin = 0
    board = [[] for _ in range(5)]
    for j in range(5):
        board[j] = list(input().strip())
    for k in range(5):
        for l in range(8):
            if board[k][l] == 'o':
                pin += 1
    num = pin
    for k in range(5):
        for l in range(8):
            if board[k][l] == 'o':
                dfs(k, l, pin)
    print(pin_num, cnt)