import sys

input = sys.stdin.readline

n = int(input())

A = list(map(int, input().split()))

NGE = [-1] * n

stack = []

for i in range(n):
    if len(stack) > 0:
        if stack[-1][0] < A[i]:
            while len(stack) > 0 and stack[-1][0] < A[i]:
                num, idx = stack.pop()
                NGE[idx] = A[i]
    stack.append((A[i], i))

for i in NGE:
    print(i, end=" ")