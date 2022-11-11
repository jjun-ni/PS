from collections import deque
import sys 
input=sys.stdin.readline
M,N=map(int,input().split())
world=[]
for i in range(N):
    world.append(list(map(int,input().split())))
Q=deque()
for i in range(M):
    for j in range(N):
        if world[j][i]==1:   
            Q.append((i,j))
dx=[-1,0,1,0]
dy=[0,-1,0,1]

def tomato():
    while Q:
        x,y=Q.popleft()

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or ny<0 or nx>=M or ny>=N:
                continue
            elif world[ny][nx]==-1:
                continue
            elif world[ny][nx]==0:
                world[ny][nx]=1+world[y][x]
                Q.append((nx,ny))
            
tomato()

cnt = 0
success = True
for i in world:
    for j in i:
        if cnt < j:
            cnt = j
        if j==0:
            success = False

if success:
    print(cnt - 1)
else:
    print("-1")









