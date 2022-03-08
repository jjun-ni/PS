import sys
n, l = map(int, sys.stdin.readline().split())
arr = [0 for i in range(l)]
isused = [0 for i in range(n)]


def func(k):
    if k == l:
        for i in arr:
            print(i, end=' ')
        print()
        return

    for i in range(n):
        if isused[i] == 0:
            if k == 0 or arr[k-1] < i+1:
                arr[k] = i + 1
                isused[i] = 1
                func(k + 1)
                isused[i] = 0


func(0)