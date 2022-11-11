n = int(input())
ord = []
dp = [1 for _ in range(n+1)]
for i in range(n):
    ord.append(int(input()))

for i in range(n):
    for j in range(i):
        if ord[j] < ord[i]:
            dp[i+1] = max(dp[i+1], dp[j+1]+1)

maxi = 0
for i in range(1, n+1):
    maxi=max(maxi, dp[i])

print(n-maxi)