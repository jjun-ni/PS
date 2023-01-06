N = int(input())
array = list(map(int,input().split()))
stack = []
ans = [-1 for i in range(N)] 
for i in range(N):
   while stack and stack[-1][0] < array[i]:
      ans[stack[-1][1]] = array[i]
      stack.pop()
   stack.append([array[i],i])
print(*ans)