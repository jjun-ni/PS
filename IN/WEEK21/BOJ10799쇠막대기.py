import sys

input = sys.stdin.readline

info = input().rstrip()

stack = []

open = 0
divide = 0
for i in range(len(info)):
    if info[i] == "(":
        open += 1
        stack.append(info[i])
    elif info[i] == ")":
        if len(stack) > 0:
            if stack[-1] == "(":
                open -= 1
                divide += open
                while len(stack) > 0 and stack[-1] == "(":
                    stack.pop()
        else:
            open -= 1
            divide += 1 
print(divide)
        