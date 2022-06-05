##아이디어 찾아봄
T=int(input())
n=[]
for i in range(T):
    n.append(int(input()))
#print(n)
dp=[1,2,4]
for i in range(7):
    dp.append(1)
#print(dp)

for i in range(3,10):
        dp[i]=dp[i-1]+dp[i-2]+dp[i-3]
#print(dp)
for i in range(T):
    idx=n[i]
    print(dp[idx-1])