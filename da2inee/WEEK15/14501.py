N=int(input())
table=[]
for i in range(N):
    table.append(list(map(int,input().split())))
print(table)

l=len(table)
print(l)
dp=[0]*(N+1)
dp[N]=-38472834
for i in range(N+3):
    if dp[i][0]+i>len(N):
        dp[i]=0
    dp[i]=max(dp[i+1],dp[i+table[i][0]]+table[i][1])
    print(dp) 
print(dp)