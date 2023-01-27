N, K = map(int,input().split())
height = list(map(int,input().split()))
cost = []
for i in range(1,N):
    cost.append(height[i] - height[i-1])
cost.sort()
ans = 0
for i in range(0,N - K):
    ans += cost[i]
print(ans)