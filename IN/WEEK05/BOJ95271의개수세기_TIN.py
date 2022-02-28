import sys
import heapq

input = sys.stdin.readline

a, b = map(int, input().split())

def find_one(num):
    target = bin(num)
    num_bit = len(target) - 3
    if num == 1:
        return 1
    if num == 0:
        return 0
    if num == 2:
        return 2
    return num_bit * (2 ** (num_bit-1)) + num - 2 ** num_bit + find_one(num - 2 ** num_bit) + 1
min = find_one(a-1)
max = find_one(b)
print(max - min)