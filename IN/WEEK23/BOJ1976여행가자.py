import sys

input = sys.stdin.readline

def find_parent(paerent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_group(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N = int(input())
M = int(input())
parent = [0] * (N + 1)
for i in range(1, N + 1):
    parent[i] = i

for i in range(1, N + 1):
    tmp = list(map(int, input().split()))
    for j in range(len(tmp)):
        if tmp[j] == 1:
            union_group(parent, i, j + 1)

journey = list(map(int, input().split()))
parent_journey = [0] * len(journey)
for i in range(len(journey)):
    parent_journey[i] = find_parent(parent, journey[i])
if max(parent_journey) != min(parent_journey):
    print("NO")
else:
    print("YES")


