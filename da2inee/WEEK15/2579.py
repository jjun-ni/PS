
N=int(input())
num=[]
for i in range(N):
    num.append(int(input()))
print(num)
dp=[0]*(N)
dp[0]=num[0]
if N>1:
    dp[1]=num[0]+num[1]
    for i in range(2,N):
        dp[i]=max(dp[i-3]+num[i-1]+num[i],dp[i-2]+num[i])
print(dp[N-1])