import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
superior = list(map(int, input().split()))
INF = int(1e9)

graph = [[] for _ in range(n)]
sub_num = [0] * n
time = [INF] * n

for i, sup in enumerate(superior):
    if sup == -1:
        continue
    graph[sup].append(i)
    
time[0] = 0

def count_sub(now):
    if len(graph[now]) == 0:
        sub_num[now] = 0 
        return 0
    res = 0 
    candidate = []
    for next in graph[now]:
        candidate.append(count_sub(next))
    candidate.sort(reverse=True)
    num_child = 1 
    for sub in candidate:
        res = max(num_child + sub, res)    
        num_child += 1
    sub_num[now] = res
    return sub_num[now]

count_sub(0)
deq = deque()
deq.append((0,0))

while deq:
    t, now = deq.popleft() 
    next_list = []
    for next in graph[now]:
        next_list.append((sub_num[next], next))    
    next_list.sort(reverse=True)
    next_t = t+1
    for _, next in next_list:
        time[next] = next_t
        deq.append((next_t, next))
        next_t += 1

print(max(time))