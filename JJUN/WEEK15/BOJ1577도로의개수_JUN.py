import sys
import heapq
input = sys.stdin.readline
n, m = map(int, input().split())
k = int(input())
cantgo = [(m+1, n+1, 0)]
for i in range(k):
    a, b, c, d = map(int, input().split())
    if a == c:
        if b > d:
            if not (b, a, 0) in cantgo:
                if (b, a, 1) in cantgo:
                    cantgo.remove((b, a, 1))
                    heapq.heappush(cantgo, (b, a, 2))
                else:
                    heapq.heappush(cantgo, (b, a, 0))
        else:
            if not (d, c, 0) in cantgo:
                if (d, c, 1) in cantgo:
                    cantgo.remove((d, c, 1))
                    heapq.heappush(cantgo, (d, c, 2))
                else:
                    heapq.heappush(cantgo, (d, c, 0))
    elif b == d:
        if a > c:
            if not (b, a, 1) in cantgo:
                if (b, a, 0) in cantgo:
                    cantgo.remove((b, a, 0))
                    heapq.heappush(cantgo, (b, a, 2))
                else:
                    heapq.heappush(cantgo, (b, a, 1))
        else:
            if not (d, c, 1) in cantgo:
                if (d, c, 0) in cantgo:
                    cantgo.remove((d, c, 0))
                    heapq.heappush(cantgo (d, c, 2))
                else:
                    heapq.heappush(cantgo, (d, c, 1))
dp = [[0] * (n+1) for _ in range(m+1)]
dp[0][0] = 1
q, p, r = heapq.heappop(cantgo)
for i in range(m+1):
    for j in range(n+1):
        if i == 0:
            if j == 0:
                continue
            elif j==p and i==q:
                q, p, r = heapq.heappop(cantgo)
                continue
            else:
                dp[i][j] = dp[i][j-1]
        else:
            if j==p and i==q:
                if j != 0:
                    if r == 0:
                        dp[i][j] = dp[i][j-1]
                    elif r == 1:
                        dp[i][j] = dp[i-1][j]
                q, p, r = heapq.heappop(cantgo)
            else:
                if j == 0:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
print(dp[m][n])