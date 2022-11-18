N=int(input())
count=0
dp=[5001]*(N+1)
dp[3]=1
if N>=5:
    dp[5]=1

for i in range(3,N+1):
    if i>3:
        if dp[i-3]!=5001:
            dp[i]=min(dp[i],dp[i-3]+1)
for i in range(6,N+1):
    if dp[i-5]!=5001:
        dp[i]=min(dp[i],dp[i-5]+1)
if dp[N]==5001:
    print("-1")
else:
    print(dp[N])