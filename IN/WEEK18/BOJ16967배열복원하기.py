import sys

input = sys.stdin.readline

h, w, x, y = map(int, input().split())
array = []
for _ in range(h+x):
    array.append(list(map(int, input().split())))

a = [[0] * w for _ in range(h)]
for i in range(h):
    for j in range(w):
        if i < x:
            a[i][j] = array[i][j]
        else:
            if j >= y:
                a[i][j] = array[i][j] - a[i-x][j-y]
            else:
                a[i][j] = array[i][j]
            
for i in a:
    for j in i:
        print(j, end=" ")
    print()