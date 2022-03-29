import sys
input = sys.stdin.readline
T = int(input())
def max_point(k):
    global dp
    for i in range(1, k+1):
        dp[i][0] = max(dp[i-1][1], dp[i-1][2]) + sticker[0][i-1]
        dp[i][1] = max(dp[i-1][0], dp[i-1][2]) + sticker[1][i-1]
        dp[i][2] = max(dp[i-1])
    return max(dp[k])
for i in range(T):
    n = int(input())
    sticker = []
    for _ in range(2):
        sticker.append(list(map(int, input().split())))
    dp = [[0] * 3 for _ in range(n + 1)]
    print(max_point(n))