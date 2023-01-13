import sys
input = sys.stdin.readline
N,M = map(int,input().split())
num = list(map(int,input().split()))
ans = [0 for _ in range(N + 1)] 
ans[1] = num[0]

for i in range(2,N+1):
    ans[i] = ans[i-1] + num[i-1]
for k in range(M):
    i,j = map(int,input().split())
    print(ans[j] -ans[i-1])
    
