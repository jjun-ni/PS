import heapq
import sys
input = sys.stdin.readline
N = int(input())
pheap = []
mheap = []
for i in range(N):
    k = int(input())
    if k > 0:
        heapq.heappush(pheap, k)
    elif k < 0:
        heapq.heappush(mheap, -k)
    else:
        if len(pheap) == 0 and len(mheap) == 0:
            print(0)
        elif len(pheap) != 0 and len(mheap) == 0:
            print(heapq.heappop(pheap))
        elif len(pheap) == 0 and len(mheap) != 0:
            print(-heapq.heappop(mheap))
        else:
            p, m = heapq.heappop(pheap), heapq.heappop(mheap)
            if m == min(p,m):
                print(-m)
                heapq.heappush(pheap, p)
            else:
                print(p)
                heapq.heappush(mheap, m)
