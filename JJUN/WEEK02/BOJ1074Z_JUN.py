import sys
input = sys.stdin.readline
N, r, c = map(int, input().split())
count = 0
def quadrant(N, a, b):
    global count
    l = 2**(N-1)
    square = (2**(N-1))**2
    if a >= l and b >= l:
        count += 3*square
    elif a >= l and b < l:
        count += 2*square
    elif a < l and b >= l:
        count += 1*square
    return N-1, a%l, b%l
while (N>=1):
    N, r, c = quadrant(N, r, c)
print(count)