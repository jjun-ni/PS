N =  int(input())
world = []
for i in range(N):
    world.append(list(map(int,input().split())))
cnt_white = 0
cnt_blue = 0
def paper(size,x,y):
    global cnt_blue
    global cnt_white
    ans = world[x][y]
    for i in range(x,x + size):
        for j in range(y,y + size):
            if world[i][j] != ans:
                new_size = size//2
                paper(new_size,x,y)
                paper(new_size,x+new_size,y)
                paper(new_size,x,y+new_size)
                paper(new_size,x+new_size,y+new_size)
                return
    if ans == 1:
        cnt_blue += 1
    else:
        cnt_white += 1
paper(N,0,0)
print(cnt_white)
print(cnt_blue)
