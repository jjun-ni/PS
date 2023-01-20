N = int(input())
array = []
for i in range(N):
    a = list(map(int,input().split()))
    array.append(a)
array.sort()
dp = [0] * N
dp[0] = 1
for i in range(N):
    a = [0]
    for j in range(0,i):
        if array[j][1] < array[i][1]:
            a.append(dp[j])      
    dp[i] = max(a) + 1
print(N - max(dp))
