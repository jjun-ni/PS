import sys
import math
input = sys.stdin.readline
N, M = map(int, input().split())
print(int(math.factorial(N))//int(math.factorial(N-M)*math.factorial(M)))