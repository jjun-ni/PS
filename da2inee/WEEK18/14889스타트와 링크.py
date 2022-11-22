import itertools
N = int(input())
world = [] 
for i in range(N):
    world.append(list(map(input().split())))
print(world)
com = itertools.combinations(world,2)

print(com)


    