import sys

input = sys.stdin.readline

T = int(input())

dp = [[0] * 31 for _ in range(31)]

def find_comb(m,n):
    if dp[m][n] != 0:
        return dp[m][n]
    if n == 1:
        dp[m][n] = m
        return m
    if m == n:
        dp[m][n] = 1
        return 1
    dp[m-1][n-1] = find_comb(m-1,n-1)
    dp[m-1][n] = find_comb(m-1,n)
    return dp[m-1][n-1] + dp[m-1][n] 

for _ in range(T):
    n, m = map(int, input().split())
    print(find_comb(m,n))