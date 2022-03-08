import sys
from collections import deque
INF = 1e9
input = sys.stdin.readline
n, m = map(int, input().split())
snake = {}
ladder = {}
for i in range(n):
    x, y = map(int, input().split())
    ladder[x] = y
for i in range(m):
    x, y = map(int, input().split())
    snake[x] = y
dp = [INF for _ in range(101)]
dp[1] = 0
queue = deque()
queue.append((1, 0))
while queue:
    position, count = queue.popleft()
    for i in range(1, 7):
        next = position + i
        if next <= 100:
            if next in snake.keys():
                next = snake[next]
            if next in ladder.keys():
                next = ladder[next]
            if dp[next] > count + 1:
                dp[next] = count + 1
                queue.append((next, count + 1))
print(dp[100])