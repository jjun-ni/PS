import sys
from collections import deque
input = sys.stdin.readline
T = int(input())
def D(n):
    n *= 2
    n %= 10000
    return n
def S(n):
    if n == 0:
        return 9999
    return n-1
def L(n):
    return (n%1000)*10 + n//1000
def R(n):
    return (n%10)*1000 + n//10
def solve(s, t):
    queue = deque()
    visited = [False for _ in range(10000)]
    queue.append((s, ""))
    visited[s] = True
    while queue:
        x, oper = queue.popleft()
        if x == t:
            print(oper)
            break
        tmp = D(x)
        if not visited[tmp]:
            visited[tmp] = True
            queue.append((tmp, oper+'D'))
        tmp = S(x)
        if not visited[tmp]:
            visited[tmp] = True
            queue.append((tmp, oper+'S'))
        tmp = L(x)
        if not visited[tmp]:
            visited[tmp] = True
            queue.append((tmp, oper+'L'))
        tmp = R(x)
        if not visited[tmp]:
            visited[tmp] = True
            queue.append((tmp, oper+'R'))
for i in range(T):
    A, B = map(int, input().split())
    solve(A, B)