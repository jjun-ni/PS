R,C,K = map(int,input().split())
world = []
for i in range(R):
    world.append(input())
print(world)
dx = [0,0,-1,1]
dy  = [-1,1,0,0]
visited = [[0]*C for i in range(R)]
ans = 0 
