import heapq
import sys
INF = int(1e9)
input = sys.stdin.readline
n, m, k, x = map(int, input().split())
city = [[] for _ in range(n+1)]
distance = [INF] * (n+1)
distance[0] = 0
for i in range(m):
    a, b = map(int, input().split())
    city[a].append(b)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in city[now]:
            cost = dist + 1
            if cost < distance[i]:
                distance[i] = cost
                heapq.heappush(q, (cost, i))

dijkstra(x)

t = True
for i in range(1, n+1):
    if distance[i] == k:
        print(i)
        t = False
if t:
    print(-1)