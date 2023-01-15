while True:
    x = input()
    if x == '.':
        break
    s = 0
    b = 0
    t = True
    li = [0]
    for i in x:
        if i == '(':
            s += 1
            li.append(')')
        elif i =='[':
            b += 1
            li.append(']')
        elif i == ')':
            s -= 1
            if i == li[-1]:
                li.pop()
            else:
                t = False
        elif i == ']':
            b -= 1
            if i == li[-1]:
                li.pop()
            else:
                t = False
        if s < 0 or b < 0:
            t = False
    if t:
        if s == b == 0:
            print('yes')
        else:
            print('no')
    else:
        print('no')

#가장 빠르고 간결한 풀이
from sys import stdin, stdout

def isvalid(s):
    stack = []
    for c in s:
        if c in '([':
            stack.append(c)
        elif c == ')':
            if not stack or stack.pop() != '(':
                return False
        elif c == ']':
            if not stack or stack.pop() != '[':
                return False
    return not stack

strings = stdin.readlines()
strings.pop()
for string in strings:
    stdout.write("yes\n" if isvalid(string) else "no\n")