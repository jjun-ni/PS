import heapq
N = int(input())
heap = []
for i in range(N):
    num, start, end = map(int,input().split())
    heapq.heappush(heap,[start,end])
start, end = heapq.heappop(heap)
q = []
heapq.heappush(q,end)
while heap:
    start, end = heapq.heappop(heap)
    if start >= q[0]:
        heapq.heappop(q)
    heapq.heappush(q,end)
print(len(q))