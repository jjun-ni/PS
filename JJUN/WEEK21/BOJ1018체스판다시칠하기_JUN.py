n, m = map(int, input().split())
board = []
for i in range(n):
    board.append(input())
sample = [[' ']*8 for _ in range(8)]

for i in range(8):
    for j in range(8):
        if (i+j)%2==0:
            sample[i][j]='B'
        else:
            sample[i][j]='W'
change=[]
for i in range(n-7):
    for j in range(m-7):
        count = 0
        for k in range(8):
            for l in range(8):
                if board[i+k][j+l]==sample[k][l]:
                    count += 1
        change.append(min(count, 64 - count))
print(min(change))

