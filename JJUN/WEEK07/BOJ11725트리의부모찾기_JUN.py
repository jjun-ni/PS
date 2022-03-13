import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
graph = [[] for _ in range(N+1)]
for i in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
queue = deque()
queue.append((1, 1))
tree = [[] for _ in range(N+1)]
while queue:
    ch, par = queue.popleft()
    for i in graph[ch]:
        if i == par:
            continue
        else:
            tree[i] = ch
            queue.append((i, ch))

for i in range(2, N+1):
    print(tree[i])