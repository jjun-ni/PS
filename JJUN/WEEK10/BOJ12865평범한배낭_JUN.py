import sys
input = sys.stdin.readline

def knapsack(W, wt, val, n): # W : 무게한도, wt : 물건 무게, val : 물건 가치, n : 물건 수
    dp = [[0] * (W+1) for _ in range(n+1)]
    for i in range(n+1):
        for j in range(W+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif wt[i-1] <= j:
                dp[i][j] = max(val[i-1]+dp[i-1][j-wt[i-1]], dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n][W]

wt = []
val = []
n, k = map(int, input().split()) # n : 물품의 수, k : 준서가 버틸 수 있는 무게
for i in range(n):
    w, v = map(int, input().split())
    wt.append(w)
    val.append(v)
print(knapsack(k, wt, val, n))