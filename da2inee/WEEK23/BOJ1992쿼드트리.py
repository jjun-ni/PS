N = int(input())
world = []
for i in range(N):
    world.append(list(input()))
ans = [] 
def picture(size,x,y):
    global ans
    point = world[x][y]
    for i in range(x,x + size):
        for j in range(y,y + size):
            if world[i][j] != point:
                new_size = size//2
                ans.append("(")
                picture(new_size, x, y)
                picture(new_size, x, y + new_size)
                picture(new_size, x + new_size, y)
                picture(new_size, x + new_size, y + new_size)
                ans.append(")")
                return           
    ans.append(point)
picture(N,0,0)
print(''.join(map(str,ans)))
