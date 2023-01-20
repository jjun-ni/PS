import sys

input = sys.stdin.readline

while True:
    lines = input().rstrip()
    if lines == '.':
        break
    s = []
    for line in lines:
        if line == '.':
            if len(s) == 0:
                print("yes")
            else:
                print("no")
        if line in '([':
            s.append(line)
        elif line == ')':
            if len(s) == 0 or s[-1] != '(':
                print("no")
                break
            else:
                s.pop()
        elif line == ']':
            if len(s) == 0 or s[-1] != '[':
                print("no")
                break
            else:
                s.pop()