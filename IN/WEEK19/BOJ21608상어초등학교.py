import sys

input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

n = int(input())

room = [[0] * n for _ in range(n)]
friendship = [list(map(int, input().split())) for _ in range(n*n)]

def check_friend(y, x, friends):
    friend_cnt = 0
    blank = 0
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if room[ny][nx] in friends:
                friend_cnt += 1
            elif room[ny][nx] == 0:
                blank += 1
    return friend_cnt, blank 

for i in range(len(friendship)):
    student, friends = friendship[i][0], friendship[i][1:]
    candidate = []
    max_near_friend = 0
    max_near_blank = 0
    nothing = True
    for y in range(n):
        for x in range(n):
            if room[y][x] != 0:
                continue
            near_friend, near_blank = check_friend(y,x,friends)
            if near_friend > max_near_friend:
                max_near_friend = near_friend
                max_near_blank = near_blank
                candidate = (y, x)
                nothing = False
            elif near_friend == max_near_friend:
                if near_blank > max_near_blank:
                    max_near_friend = near_friend
                    max_near_blank = near_blank
                    candidate = (y, x)
                    nothing = False
            if nothing:
                candidate = (y, x)
                nothing = False
    y, x = candidate
    room[y][x] = student
    friendship[i].append((y,x))

satisfaction = 0
for i in range(len(friendship)):
    student = friendship[i][0]
    friends = friendship[i][1:5]
    pos = friendship[i][5]
    near_friend, _ = check_friend(pos[0], pos[1], friends)
    if near_friend == 1:
        satisfaction += 1
    elif near_friend == 2:
        satisfaction += 10
    elif near_friend == 3:
        satisfaction += 100
    elif near_friend == 4:
        satisfaction += 1000
print(satisfaction)