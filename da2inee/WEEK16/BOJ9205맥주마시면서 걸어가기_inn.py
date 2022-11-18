
t=int(input())
from collections import deque
def beer():
    queue=deque()
    queue.append(start) 
    visited=[False]*n
    while queue:
        x,y=queue.popleft()
        if abs(x-end[0])+abs(y-end[1])<=1000:
            return True
        for i in range(n):
            if visited[i]==False:
                nx,ny=market[i]
                if abs(x-nx)+abs(y-ny)<=1000:
                    visited[i]=True
                    queue.append([nx,ny])
            print(visited)
            print(market)
            print(queue)
    return False
for i in range(t):
    market=[]
    n=int(input())
    start=list(map(int,input().split()))
    for j in range(n):
        market.append(list(map(int,input().split())))
    end=list(map(int,input().split()))
    beer()
    if beer()==True:
        print("happy")
    else:
        print("sad")
   
    





    

