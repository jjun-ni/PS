N = int(input())
M = int(input())
city = []
parent = [i for i in range(N)]
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]
def union(x,y):
    x = find(x) #1
    y = find(y) #0
    if x < y:
        parent[y] = x
    elif x > y:
        parent[x] = y
for i in range(N):
    city.append(list(map(int,input().split())))
for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            union(i,j)
            print(parent)
plan = list(map(int,input().split()))
for i in range(1,M):
    if parent[plan[i] - 1] != parent[plan[0]-1]:
        print("NO")
        break
else:
    print("YES")

# union-find 문제이다.