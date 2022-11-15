import sys

input = sys.stdin.readline

n, l = map(int, input().split())

leak = list(map(int, input().split()))
leak.sort()
cnt = 0
i = 0
while i < n:
    cnt += 1
    end = leak[i] + l
    for j in range(i, n):
        if leak[j] >= end:
            i = j
            break
        else:
            if j == n-1:
                i = n
                break
print(cnt)