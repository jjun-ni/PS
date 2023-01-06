from collections import deque
n,m = map(int,input().split())
world = []
check = []
for i in range(n):
    a = list(map(int,input().split()))
    world.append(a)
    check.append(a)
ans = [0]
nx = [-1,1,0,0]
ny = [0,0,1,-1]
def bfs(x,y):
    cnt = 1
    q = deque()
    q.append((x,y))
    check[x][y] = 0
    while q:
        a,b = q.popleft()
        for i in range(4):
            dx = a + nx[i]
            dy = b + ny[i]
            if 0<=dx<n and 0<=dy<m and check[dx][dy] ==1:
                cnt +=1
                q.append((dx,dy))
                check[dx][dy] = 0 
    ans.append(cnt) 
 
for i in range(n):
    for j in range(m):
        if check[i][j] ==1:
            bfs(i,j)
print(len(ans)-1)
print(max(ans))