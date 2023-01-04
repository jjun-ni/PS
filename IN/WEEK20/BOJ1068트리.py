import sys

input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n)]

connection = list(map(int, input().split()))

root = 0
for child, par in enumerate(connection):
    if par == -1:
        root = child
    else:
        graph[par].append(child)
    
remove = int(input())
def count_leaf(now):
    if now == remove:
        return 0
    if len(graph[now]) == 0:
        return 1
    res = 0
    for next in graph[now]:
        res += count_leaf(next)
    return 1 if res == 0 else res
print(count_leaf(root))