import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    price = list(map(int, input().split()))
    gain = 0
    max_price = 0
    for i in reversed(range(n)):
        if price[i] < max_price:
            gain += max_price - price[i]
        else:
            max_price = price[i]
    print(gain)