N = int(input())
cards = list(map(int,input().split()))
dp = [0 for _ in range(N+1)]
dp[1] = cards[0]
for i in range(1,N+1):
    for k in range(1,i+1):
        dp[i] = max(dp[i-k] + cards[k-1],dp[i])
print(dp[-1])
    


