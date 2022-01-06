N = int(input())
t = False
for i in range(1, N):
    M = str(i)
    c = i
    for j in M:
        c += int(j)
    if N == c:
        print(i)
        t = True
        break

if t == False:
    print(int(0))