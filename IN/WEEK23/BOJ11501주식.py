import sys

input = sys.stdin.readline

n = int(input())

top = list(map(int, input().split()))

stack = []

res = [0]

stack.append((top[0],1))

for i in range(1,n):
    receive = 0
    while stack:
        height, idx = stack.pop()
        if height < top[i]:
            continue
        else:
            receive = idx
            stack.append((height, idx))
            break
    res.append(receive)
    stack.append((top[i], i+1))

for i in res:
    print(i, end=" ")