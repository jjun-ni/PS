from itertools import combinations
N, M = map(int,input().split())
world = list(list(map(int,input().split())) for _ in range(N))
chicken = []
house = []
for i in range(N):
    for j in range(N):
        if world[i][j] == 2:
            chicken.append([i,j])
        elif world[i][j] ==1:
            house.append([i,j])
print(house)
def distance():
    final = int(10e9)
    for i in combinations(chicken,M):
       
        a= 0 
        for k in house:
            ans = int(10e9)
            for j in range(M):
                ans = min(ans,abs(k[0]-i[j][0]) + abs(k[1]-i[j][1]))
            a += ans
        final = min(final,a)
    return final
print(distance())

