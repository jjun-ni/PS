N=int(input())
A=list(map(int,input().split()))
#print(A)
dp=[0]*N
dp[0]=1

for i in range(N):
    a=[0]
    for j in range(0,i):
        if A[j]<A[i]:
            a.append(dp[j])
    dp[i]=max(a)+1
print(dp)
print(max(dp))

