import sys

input = sys.stdin.readline

n = int(input())

sell_list = {}

for _ in range(n):
    name = input().rstrip()
    if name in sell_list.keys():
        sell_list[name] += 1
    else:
        sell_list[name] = 1

cnt = 0
max_name = ""

for key in sell_list.keys():
    if sell_list[key] > cnt:
        cnt = sell_list[key]
        max_name = key
    elif sell_list[key] == cnt:
        if max_name > key:
            max_name = key
print(max_name)