N = int(input())
M = int(input())
vip = [0]
for i in range(M):
    vip.append(int(input()))
vip.append(N+1)
dp = [0] * (N+1)
dp[0] = 1
dp[1] = 1
ans = 1
for i in range(2,N+1):
    dp[i] = dp[i-2] + dp[i-1] 
if M >= 1:
    for i in range(1,len(vip)):
        ans *= dp[vip[i]-vip[i-1]-1]
    print(ans)
else:
    print(dp[N])
    
