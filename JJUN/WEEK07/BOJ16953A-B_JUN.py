from collections import deque
import sys
input = sys.stdin.readline
A, B = map(int, input().split())
queue = deque()
queue.append((B, 1))
answer = -1

while queue:
    n, cnt = queue.popleft()
    if n == A:
        answer = cnt
        break
    else:
        if n%2 == 0:
            if n != 0:
                queue.append((n//2, cnt+1))
            else:
                continue
        else:
            if n > 1 and str(n)[-1] == "1":
                queue.append((int(str(n)[:-1]), cnt+1))
print(answer)