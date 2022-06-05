import sys
input = sys.stdin.readline
a, b = map(int, input().split())
n, m = map(int, input().split())
board = [[0] * a for _ in range(b)]
direction = {'N' : 0, 'E' : 1, 'S' : 2, 'W' : 3}
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
robot = []
for i in range(n):
    p, q, r = input().split()
    robot.append([b - int(q), int(p) - 1, direction[r]])
    board[b-int(q)][int(p)-1] = i+1
t = True
for i in range(m):
    e, f, g = input().split()
    num = int(e)-1
    cnt = int(g)
    r, c, d = robot[num]
    if f == 'L' or f == 'R':
        new_d = (d + cnt) % 4
        if cnt % 2:
            if f == 'L':
                new_d = (new_d + 2) % 4
        robot[num] = [r, c, new_d]
    else:
        nx = dx[d]
        ny = dy[d]
        for j in range(cnt):
            if 0 <= r + nx < b and 0 <= c + ny < a:
                if board[r+nx][c+ny]:
                    t = False
                    print(f'Robot {board[r][c]} crashes into robot {board[r+nx][c+ny]}')
                    break
                else:
                    board[r][c] = 0
                    r, c = r + nx, c + ny
                    board[r][c] = num + 1
                    robot[num] = [r, c, d]
            else:
                t = False
                print(f'Robot {board[r][c]} crashes into the wall')
                break
    if t == False:
        break

if t == True:
    print("OK")