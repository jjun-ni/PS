A = input()
B = input()
a = len(A)
b = len(B)
dp = [[0] * (b+1) for _ in range(a+1)]
for i in range(a):
    for j in range(b):
        if A[a-1-i] == B[b-1-j]:
            dp[a-1-i][b-1-j] = dp[a-i][b-j]+1
        else:
            dp[a-1-i][b-1-j] = max(dp[a-1-i][b-j],dp[a-i][b-j-1])
print(dp[0][0])