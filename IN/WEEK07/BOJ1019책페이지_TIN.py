import sys

input = sys.stdin.readline

n = int(input())

cnt = [0] * 10

def update_cnt(n, p):
    while n > 0:
        cnt[n%10] += p
        n //= 10

def solve(n1, n2, p):
    while n1 % 10 != 0 and n1 <= n2:
        update_cnt(n1, p)
        n1 += 1
    if n1 > n2:
        return
    while n2 % 10 != 9 and n1 <= n2:
        update_cnt(n2, p)
        n2 -= 1
    if n1 > n2:
        return
    for i in range(10):
        cnt[i] += (n2 // 10 - n1 // 10 + 1) * p
    solve(n1 // 10, n2 // 10, 10 * p)
    
solve(1, n, 1)
for i in cnt:
    print(i, end=" ")