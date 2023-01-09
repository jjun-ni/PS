import sys

input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
n, m = map(int, input().split())

office = [list(map(int, input().split())) for _ in range(n)]

cctv = []
state = [[0] * m for _ in range(n)]
zero_cnt = 0
for i in range(n):
    for j in range(m):
        if office[i][j] != 0 and office[i][j] != 6:
            cctv.append((i, j))
            state[i][j] = 1
        elif office[i][j] == 0:
            zero_cnt += 1
            

def count_blind(num_cctv):
    res = 0
    if num_cctv == len(cctv):
        return 0
    y, x = cctv[num_cctv]
    if office[y][x] == 1:
        for i in range(4):
            cnt = 0
            j = 1
            not_blind = []
            ny = y + j * dy[i]
            nx = x + j * dx[i]
            while 0 <= ny < n and 0 <= nx < m and office[ny][nx] != 6:
                if office[ny][nx] == 0:
                    if state[ny][nx] == 0:
                        cnt += 1
                        state[ny][nx] = 1 
                        not_blind.append((ny, nx))
                j += 1
                ny = y + j * dy[i]
                nx = x + j * dx[i]
            cnt += count_blind(num_cctv+1)
            for yy, xx in not_blind:
                state[yy][xx] = 0
            res = max(res, cnt)
    elif office[y][x] == 2:
        for i in range(2):
            cnt = 0
            j = 1
            k = 1
            not_blind = []
            ny = y + j * dy[i]
            nx = x + j * dx[i]
            while 0 <= ny < n and 0 <= nx < m and office[ny][nx] != 6:
                if office[ny][nx] == 0:
                    if state[ny][nx] == 0:
                        cnt += 1
                        state[ny][nx] = 1 
                        not_blind.append((ny, nx))
                j += 1
                ny = y + j * dy[i]
                nx = x + j * dx[i]
            ny = y - k * dy[i]
            nx = x - k * dx[i]
            while 0 <= ny < n and 0 <= nx < m and office[ny][nx] != 6:
                if office[ny][nx] == 0:
                    if state[ny][nx] == 0:
                        cnt += 1
                        state[ny][nx] = 1 
                        not_blind.append((ny, nx))
                k += 1
                ny = y - k * dy[i]
                nx = x - k * dx[i]
            cnt += count_blind(num_cctv+1)
            for yy, xx in not_blind:
                state[yy][xx] = 0
            res = max(res, cnt)
    elif office[y][x] == 3:
        for i in range(4):
            cnt = 0
            j = 1
            k = 1
            not_blind = []
            ny = y + j * dy[i]
            nx = x + j * dx[i]
            while 0 <= ny < n and 0 <= nx < m and office[ny][nx] != 6:
                if office[ny][nx] == 0:
                    if state[ny][nx] == 0:
                        cnt += 1
                        state[ny][nx] = 1 
                        not_blind.append((ny, nx))
                j += 1
                ny = y + j * dy[i]
                nx = x + j * dx[i]
            ny = y + k * dy[(i+1)%4]
            nx = x + k * dx[(i+1)%4]
            while 0 <= ny < n and 0 <= nx < m and office[ny][nx] != 6:
                if office[ny][nx] == 0:
                    if state[ny][nx] == 0:
                        cnt += 1
                        state[ny][nx] = 1 
                        not_blind.append((ny, nx))
                k += 1
                ny = y + k * dy[(i+1)%4]
                nx = x + k * dx[(i+1)%4]
            cnt += count_blind(num_cctv+1)
            for yy, xx in not_blind:
                state[yy][xx] = 0
            res = max(res, cnt)
    elif office[y][x] == 4:
        for i in range(4):
            cnt = 0
            j = 1
            k = 1
            z = 1
            not_blind = []
            ny = y + j * dy[i]
            nx = x + j * dx[i]
            while 0 <= ny < n and 0 <= nx < m and office[ny][nx] != 6:
                if office[ny][nx] == 0:
                    if state[ny][nx] == 0:
                        cnt += 1
                        state[ny][nx] = 1 
                        not_blind.append((ny, nx))
                j += 1
                ny = y + j * dy[i]
                nx = x + j * dx[i]
            ny = y + k * dy[(i+1)%4]
            nx = x + k * dx[(i+1)%4]
            while 0 <= ny < n and 0 <= nx < m and office[ny][nx] != 6:
                if office[ny][nx] == 0:
                    if state[ny][nx] == 0:
                        cnt += 1
                        state[ny][nx] = 1 
                        not_blind.append((ny, nx))
                k += 1
                ny = y + k * dy[(i+1)%4]
                nx = x + k * dx[(i+1)%4]
            ny = y + z * dy[(i-1)%4]
            nx = x + z * dx[(i-1)%4]
            while 0 <= ny < n and 0 <= nx < m and office[ny][nx] != 6:
                if office[ny][nx] == 0:
                    if state[ny][nx] == 0:
                        cnt += 1
                        state[ny][nx] = 1 
                        not_blind.append((ny, nx))
                z += 1
                ny = y + z * dy[(i-1)%4]
                nx = x + z * dx[(i-1)%4]
            cnt += count_blind(num_cctv+1)
            for yy, xx in not_blind:
                state[yy][xx] = 0
            res = max(res, cnt)
    elif office[y][x] == 5:
        cnt = 0
        not_blind = []
        for i in range(4):
            j = 1
            ny = y + j * dy[i]
            nx = x + j * dx[i]
            while 0 <= ny < n and 0 <= nx < m and office[ny][nx] != 6:
                if office[ny][nx] == 0:
                    if state[ny][nx] == 0:
                        cnt += 1
                        state[ny][nx] = 1 
                        not_blind.append((ny, nx))
                j += 1
                ny = y + j * dy[i]
                nx = x + j * dx[i]
        cnt += count_blind(num_cctv+1)
        for yy, xx in not_blind:
            state[yy][xx] = 0
        res = max(res, cnt)
    return res

print(zero_cnt - count_blind(0))