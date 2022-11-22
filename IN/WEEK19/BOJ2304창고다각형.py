import sys

input = sys.stdin.readline

n = int(input())

world = [0] * 1001

for _ in range(n):
    pos, height = map(int, input().split())
    world[pos] = height

flag1 = 0
flag2 = 1000
left = 0
right = 0
top = world.index(max(world))

area = 0
while flag1 < top:
    if left < world[flag1]:
        left = world[flag1]
    area += left
    flag1 += 1
    
while flag2 >= top:
    if right < world[flag2]:
        right = world[flag2]
    area += right
    flag2 -= 1
print(area)