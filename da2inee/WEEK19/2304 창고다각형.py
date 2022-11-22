N = int(input())
world = []
for i in range(N):
    a, b = map(int,input().split())
    world.append([a,b])
world.sort()
h = [0] * (world[-1][0]+1)
for i in world:
    h[i[0]] = i[1]
print(h)
m = max(h)
idx = h.index(m)
print(idx)
total = 0
s = 0
for i in range(0,idx+1):
    if h[i] > s:
        s = h[i]
    total +=s
    print(total)
s = 0
for i in range(len(h)-1,idx,-1):
    if h[i] > s:
        s = h[i]
    total +=s
    print(total)
print(total)

