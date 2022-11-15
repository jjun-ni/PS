import sys

sys.setrecursionlimit(10**8)

input = sys.stdin.readline

res = []

def hanoei(n, start, end, sub):
    if n == 1:
        res.append((start, end))
    else:
        hanoei(n-1, start, sub, end)
        res.append((start, end))
        hanoei(n-1, sub, end, start)

n = int(input())
print(2**n-1)
hanoei(n, 1, 3, 2)
for start, end in res:
    print(start, end)