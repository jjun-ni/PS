M,N = map(int,input().split())
world = []
for i in range(M):
    world.append(list(input()))

cnt = []
for i in range(M-7):
    for j in range(N-7):
        num1 = 0
        num2 = 0
        for k in range(i,i+8):
            for l in range(j,j+8):
                if (k+l) % 2 == 0:
                    if world[k][l] != 'W':
                        num1 += 1
                    elif world[k][l] != 'B':
                        num2 += 1
                else:
                    if world[k][l] != 'B':
                        num1 += 1
                    elif world[k][l] != 'W':
                        num2 += 1
        cnt.append(num1)
        cnt.append(num2)
print(min(cnt))
                        
                    