import sys
input = sys.stdin.readline
n, m = map(int, input().split())
array = list(map(int, input().split()))
array1 = list(set(array))
array.sort()
array1.sort()
l = len(array1)
arr = [0 for i in range(m)]
seq = [-1 for i in range(l)]
for i in range(l):
    for j in range(n):
        if array[j] == array1[i]:
            seq[i] += 1
def func(k):
    if k == m:
        for i in arr:
            print(i, end = ' ')
        print()
        return

    for i in range(l):
        if seq[i] >= 0:
            arr[k] = array1[i]
            seq[i] -= 1
            func(k+1)
            seq[i] += 1

func(0)