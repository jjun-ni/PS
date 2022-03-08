import sys
input = sys.stdin.readline
n, m = map(int, input().split())
array = list(map(int, input().split()))
array.sort()
arr = [0 for i in range(m)]
seq = [0 for i in range(n)]
def func(k):
    if k == m:
        for i in arr:
            print(i, end=' ')
        print()
        return

    for i in range(n):
        if seq[i] == 0:
                arr[k] = array[i]
                seq[i] = 1
                func(k+1)
                seq[i] = 0

func(0)