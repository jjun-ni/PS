import sys
from collections import deque
input = sys.stdin.readline
N, K = map(int, input().split())
queue = deque()
queue.append(N)
maximum = 100000
count = [0 for i in range(100001)]
while queue:
    now = queue.popleft()
    if now == K:
        print(count[now])
        break
    for next in (now+1, now-1, now*2):
        if 0 <= next <= maximum and not count[next]:
            count[next] = count[now]+1
            queue.append(next)