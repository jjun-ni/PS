
##시간초과

n=int(input())
dp=[n]*(n+1)
dp[1]=1
dp[0]=0

num=[]
for j in range(1,int(n**(1/2)+1)):
        num.append(j**2)
for i in range(len(dp)):
    
    for m in num:
        if i>=m:
            dp[i]=min(dp[i],dp[i-m]+1)
    
print(dp[n])


    