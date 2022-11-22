H, W, X, Y = map(int,input().split())
world = []
for i in range(H+X):
    world.append(list(map(int,input().split())))
check = [[0] * (W + Y) for i in range(H + X)]
ans = [[0] * (W) for i in range(H)]
for i in range(H):
    for j in range(W):
        check[i][j] += 1
        check[i+X][j+Y] += 1
for i in range(H+X):
    for j in range(W+Y):
        if 0<=i<H and 0<=j<W and check[i][j] == 1:
            ans[i][j] = world[i][j]
        elif 0<=i<H and 0<=j<W and check[i][j] == 2:
            ans[i][j] = world[i][j] - ans[i-X][j-Y]
        elif H<=i<H+X and W<=j<W+Y and check[i][j] ==1:
            ans[i-X][j-Y] = world[i][j]
for i in range(len(ans)):
    print(*ans[i])
