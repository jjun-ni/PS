N,M,K = map(int,input().split())
array = []
for i in range(N):
    array.append(list(map(int,input().split())))
tree = []
for i in range(M):
    x,y,z = map(int,input().split())
    x -= 1
    y -= 1
    tree.append([x,y,z])

world = [[5] * 5 for _ in range(5)]

def grow(array,world,tree,M):
    stack = []
    for i in range(M):
        world[tree[i][0]][tree[i][1]] -= tree[i][2]
        tree[i][2] += 1
        if world[tree[i][0]][tree[i][1]] < 0:
            M -=1
            stack.append([])
            break
     
    


