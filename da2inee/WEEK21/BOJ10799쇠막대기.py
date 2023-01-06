array = list(input())

answer = 0
stack = []
for i in range(len(array)):
    if array[i] == '(':
        stack.append('(')
    elif array[i] == ')':
        if array[i-1] == '(':
            stack.pop()
            answer += len(stack)
        else:
            stack.pop()
            answer += 1
print(answer)

