from collections import deque
import sys 
input=sys.stdin.readline
N=int(input())
world=[]
for i in range(N):
    world.append(list(map(int,input().rstrip())))
#print(world)
dx=[1,-1,0,0]
dy=[0,0,1,-1]
ans=[]
visited=[]
for i in range(N):
    visited.append([0 for _ in range(N)])
#print(visited)
ans=[]
def num(world,x,y,visited):
    q=deque()
    q.append((x,y))
    dp=[]
    visited[x][y]=1
    while q:
        x,y=q.popleft()
       
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]                       
            if 0<=nx<N and 0<=ny<N and world[nx][ny]==1 :
                if visited[nx][ny]==False:                                                  
                    q.append((nx,ny))
                    dp.append((nx,ny))
                    visited[nx][ny]=True
    ans.append(len(dp)+1)
   # print(world)
dp=[]
for i in range(N):
    for j in range(N):
        if world[i][j]==1 and visited[i][j]==False:
            #print(i,j)
            num(world,i,j,visited)
ans.sort()
print(len(ans))
for i in range(len(ans)):
    print(ans[i])
#56%?53%? 메모리초과