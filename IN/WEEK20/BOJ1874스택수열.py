import sys

input = sys.stdin.readline

N = int(input())
target = []
for i in range(N):
    target.append(int(input()))
stack = [1]
i = 2
operation = ["+"]
conflict = 0

for tar in target:
    if len(stack) == 0 and i > N:
        conflict = 1
        break
    if not stack:
        stack.append(i)
        operation.append("+")
        i += 1
    while stack[-1] < tar:
        stack.append(i)
        operation.append("+")
        i += 1
    while stack[-1] >= tar:
        tmp = stack.pop()
        operation.append("-")
        if tmp == tar:
            break
        if not stack:
            conflict = 1
            break

    if conflict:
        break

if conflict:
    print("NO")
else:
    for j in range(len(operation)):
        print(operation[j])

