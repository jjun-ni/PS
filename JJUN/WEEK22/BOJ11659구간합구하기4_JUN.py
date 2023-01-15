import sys
input = sys.stdin.readline
N, M = map(int, input().split())
li = list(map(int, input().split()))
l = len(li)
sum = [0]
sum[0] = li[0]
for i in range(1, l):
    sum.append(sum[i-1]+li[i])
for k in range(M):
    i, j = map(int, input().split())
    if i == 1:
        print(sum[j-1])
    else:
        print(sum[j-1]-sum[i-2])