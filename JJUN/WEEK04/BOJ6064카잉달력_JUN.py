import sys
input = sys.stdin.readline
T = int(input())

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def lcm(x, y):
    k = gcd(x, y)
    a = x//k
    b = y//k
    return (a*b*k)

def year(M, N, x, y):
    l = lcm(M, N)
    k = False
    if M > N:
        gap = M - N
        t = y
        cnt = 0
        while cnt*N + y <= l:
            if t == x:
                print(cnt*N+y)
                k = True
                break
            t -= gap
            if t <= 0:
                t = M + t
            cnt += 1
    else:
        gap = N - M
        t = x
        cnt = 0
        while cnt*M + x <= l:
            if t == y:
                print(cnt*M + x)
                k = True
                break
            t -= gap
            if t <= 0:
                t = N + t
            cnt += 1
    if k == False:
        print(-1)

for i in range(T):
    M, N, x, y = map(int, input().split())
    year(M, N, x, y)

