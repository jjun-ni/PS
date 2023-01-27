import sys
import heapq

input = sys.stdin.readline

n = int(input())

h = []

for _ in range(n):
    num_class, start, end = map(int, input().split())
    heapq.heappush(h, (start, end))
    
cnt_room = 0
empty_room = 0
end_time = []

while h:
    start, end = heapq.heappop(h)
    while end_time:
        t_end = heapq.heappop(end_time)
        if t_end <= start:
            empty_room += 1
        else:
            heapq.heappush(end_time, t_end)
            break
    heapq.heappush(end_time, end)
    if empty_room == 0:
        cnt_room += 1
    else:
        empty_room -= 1
print(cnt_room)