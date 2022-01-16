n = int(input())
def method(k):
    if k >= 4:
        return method(k-1) + method(k-2) + method(k-3)
    elif k == 3:
        return 4
    elif k == 2:
        return 2
    elif k == 1:
        return 1
for i in range(n):
    m = int(input())
    print(method(m))