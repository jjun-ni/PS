while True:
    word = list(input())
    stack = []
    if word[0] == '.':
        break
    for i in range(len(word)):
        if word[i] == '(' or word[i] == '[':
            stack.append(word[i])
        elif word[i] ==']':
            if len(stack) != 0 and stack[-1] == '[':
                stack.pop()
            elif len(stack) == 0 or stack[-1] != '[':
                stack.append('.')
                break
        elif word[i] ==')':
            if len(stack) != 0 and stack[-1] =='(':
                stack.pop()
            elif len(stack) == 0 or stack[-1] !='(':
                stack.append('.')
                break
    if len(stack) == 0:
        print('yes')
    else:
        print('no')

