import sys

input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    par, child = map(int, input().split())
    graph[par].append(child)
    graph[child].append(par)
    
visited = [0] * (n+1)
def solve(now, target, dist):
    if now == target:
        return True, dist
    for next in graph[now]:
        if not visited[next]:
            visited[next] = True
            find, distance = solve(next, target, dist+1)
            if find:
                return find, distance
    return False, -1

visited[a] = True
print(solve(a,b,0)[1])