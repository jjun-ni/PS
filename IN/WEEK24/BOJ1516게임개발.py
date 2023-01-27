import sys

input = sys.stdin.readline

n = int(input())

graph = [[] for _ in range(n+1)]
time = [0] * (n+1)
inorder = [0] * (n+1)
total_time = [0] * (n+1)

for i in range(n):
    info = list(map(int, input().split()))
    j = 1
    while info[j] != -1:
        graph[info[j]].append(i+1)
        inorder[i+1] += 1
        j += 1
    time[i+1] = info[0]
    
def build(num):
    total_time[num] += time[num]
    for next_node in graph[num]:
        inorder[next_node] -= 1
        total_time[next_node] = max(total_time[next_node], total_time[num])
        if inorder[next_node] == 0:
            build(next_node)

root = []
for i in range(1, n+1):
    if inorder[i] == 0:
        root.append(i)

for node in root:
    build(node)

for i in range(1, n+1):
    print(total_time[i])