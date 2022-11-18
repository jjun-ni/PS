from collections import deque
N = int(input())
world = []
for i in range(N):
    world.append(input())
print(world)
visited = [[0]*N for i in range(N)]
dx = [1,-1,0,0]
dy = [0,0,-1,1]
q = deque()
def color(a,b,visited):
    q.append((a,b))
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = 

