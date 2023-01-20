N = int(input())
top = list(map(int,input().split()))
ans = [0 for _ in range(N)]
stack = []
stack.append([0,top[0]])
for i in range(1,N):
    m = top[i]
    while stack and stack[-1][1] < m:
        stack.pop()
    if len(stack) == 0:
        stack.append([i,top[i]]) 
    if stack and stack[-1][1] > m:
        ans[i] = stack[-1][0] + 1
        stack.append([i,top[i]])
print(*ans)
