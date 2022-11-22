from collections import deque
N,M = map(int,input().split())
com = []
for i in range(M):
    a,b = map(int,input().split())
    com.append(list([a,b]))
array = []
for i in range(N + 1):
    array.append([])
for i in range(M):
    a, b = com[i]
    array[b].append(a)
ans = []
for i in range(N + 1):
    ans.append([])
def hacking(x):
    q = deque()
    q.append(x)
    while q:
        xx = q.popleft()
        ans[x].append(xx)
        for i in range(len(array[xx])):
            q.append(array[xx][i])
for i in range(1,len(array)):
    hacking(i)

cnt = []
for i in range(len(ans)):
    cnt.append(len(ans[i]))
num = []
for i in range(len(ans)):
    if cnt[i] == max(cnt):
        num.append(i)
num.sort()
for i in num:
    print(i,end = " ")




