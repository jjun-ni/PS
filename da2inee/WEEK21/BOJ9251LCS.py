array1 = list(input())
array2 = list(input())
l1 = len(array1)
l2 = len(array2)
world = [[0] * (l2 + 1) for _ in range(l1+1)]

for i in range(1,l1+1):
    for j in range(1,l2+1):
        if array1[i-1] == array2[j-1]:
            world[i][j] = world[i-1][j-1] + 1
        else:
            world[i][j] = max(world[i-1][j],world[i][j-1])
print(world[-1][-1])
