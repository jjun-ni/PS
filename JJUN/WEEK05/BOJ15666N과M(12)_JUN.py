import sys
input = sys.stdin.readline
n, m = map(int, input().split())
array = list(map(int, input().split()))
array = list(set(array))
array.sort()
l = len(array)
arr = [0 for i in range(m)]
seq = [0 for i in range(l)]
def func(k):
    if k == m:
        for i in arr:
            print(i, end = ' ')
        print()
        return

    for i in range(l):
        if seq[i] < n:
            if k == 0 or arr[k-1] <= array[i]:
                arr[k] = array[i]
                seq[i] += 1
                func(k+1)
                seq[i] = 0

func(0)