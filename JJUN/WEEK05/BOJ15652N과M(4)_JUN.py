import sys
n, m = map(int, sys.stdin.readline().split())
arr = [0 for i in range(m)]
seq = [0 for i in range(n)]

def func(k):
    if k == m:
        for i in arr:
            print(i, end = ' ')
        print()
        return
    for i in range(n):
        if seq[i] < m:
            if k == 0 or arr[k - 1] <= i + 1:
                arr[k] = i + 1
                seq[i] += 1
                func(k + 1)
                seq[i] = 0

func(0)