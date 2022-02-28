import sys
from itertools import combinations
import math
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    point = []
    for _ in range(n):
        x, y = map(int, input().split())
        point.append((x,y))
    start_points = list(combinations(range(n),n//2))
    res = 1e9
    for s in start_points:
        start_x = 0
        start_y = 0
        end_x = 0
        end_y = 0
        for i in range(n):
            if i in s:
               start_x += point[i][0]
               start_y += point[i][1]
            else:
                end_x += point[i][0]
                end_y += point[i][1]
        xx = start_x - end_x
        yy = start_y - end_y
        tmp = math.sqrt(xx**2 + yy**2)
        if tmp < res:
            res = tmp
    print(res) 
