n = int(input())
m = int(input())
vip = []
for i in range(m):
    vip.append(int(input()))
dp = [0] * (41)

dp[0] = 1
dp[1] = 1
dp[2] = 2

for i in range(3, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

result = 1
if m >= 1:
    case = 0
    for i in range(m):
        result = result * dp[vip[i] - 1 - case]
        case = vip[i]
    result = result * dp[n - case]
else:
    result = dp[n]

print(result)