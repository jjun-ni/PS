import sys
from collections import deque
input = sys.stdin.readline
T = int(input())
def test(k):
    global x, t, rev
    if k == 'R':
        if rev:
            rev = False
        else:
            rev = True
    else:
        if len(x) == 0:
            t = False
            print('error')
            return False
        else:
            if rev:
                x.popleft()
            else:
                x.pop()
    return True

def makelist(x):
    L = len(x)
    num = ''
    z = deque()
    for i in range(L):
        if x[i] == '[':
            continue
        elif x[i] == ',':
            z.append(int(num))
            num = ''
            continue
        elif x[i] == ']':
            if num != '':
                z.append(int(num))
        else:
            num += x[i]
    return z

for i in range(T):
    p = input().rstrip()
    n = int(input())
    x = input().rstrip()
    x = makelist(x)
    l = len(p)
    t = True
    rev = True
    for j in range(l):
        success = test(p[j])
        if not success:
            break
    if t == True:
        if rev:
            print("[", end="")
            while x:
                if len(x) == 1:
                    print(x.popleft(), end="")
                else:
                    print(x.popleft(), end=",")
            print(']')
        else:
            print("[", end="")
            while x:
                if len(x) == 1:
                    print(x.pop(), end="")
                else:
                    print(x.pop(), end=",")
            print(']')