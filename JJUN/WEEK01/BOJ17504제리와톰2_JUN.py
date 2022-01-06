import sys
N = int(input())
numer = 1
denom = 0
def count(a, b):
    global numer, denom
    no = numer
    do = b
    numer = do
    denom = a*b+no
    return 0
li = list(map(int, sys.stdin.readline().split()))
for i in range(N-1, 0, -1):
    if i == N-1:
         count(li[i-1], li[i])
    else:
        count(li[i-1],denom)

print(denom-numer, denom)