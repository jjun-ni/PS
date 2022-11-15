import sys
n, c = list(map(int, sys.stdin.readline().split()))
house = []
for _ in range(n):
    house.append(int(sys.stdin.readline()))
house.sort()
# minInterval = house[1] - house[0] -> minInterval이 항상 house[1] - house[0]이 아닐 수도 있음.
minInterval = house[-1] - house[0]
for i in range(1, n):
    if house[i] - house[i-1] < minInterval:
        minInterval = house[i] - house[i-1]
maxInterval = house[-1] - house[0]
result = 0

while minInterval <= maxInterval:
    midInterval = (minInterval + maxInterval) // 2
    pos_antenna = house[0]
    count = 1
    for i in range(1, n):
        if house[i] >= pos_antenna + midInterval:
            pos_antenna = house[i]
            count += 1
    if count >= c:
        minInterval = midInterval + 1
        result = midInterval
    else:
        maxInterval = midInterval - 1
print(result)

