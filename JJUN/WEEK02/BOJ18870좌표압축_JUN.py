import sys
input = sys.stdin.readline
N = int(input())
k = list(map(int, input().split()))
K = sorted(set(k))
dict = {i:v for v, i in enumerate(K)}
for i in k:
    print(dict[i])