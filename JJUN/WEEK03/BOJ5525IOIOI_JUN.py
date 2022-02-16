import sys
input = sys.stdin.readline
N = int(input())
L = int(input())
S = input()
lis = []
stack = 0
for i in range(L):
    if stack == 0:
        if S[i] == 'I':
            stack += 1
    else:
        if S[i] != S[i-1]:
            stack += 1
            if i == L-1:
                lis.append(stack)
        else:
            if (stack%2) == 1:
                lis.append(stack)
                stack = 1
            else:
                lis.append(stack-1)
                stack = 0
count = 0
for i in lis:
    if i >= (2*N+1):
        count += int((i-(2*N+1))/2 + 1)
print(count)