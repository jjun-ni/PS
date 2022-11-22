import sys

input = sys.stdin.readline

n, m = map(int, input().split())

num = 0
keyword = {}

for i in range(n):
    word = input().rstrip()
    keyword[word] = num
    num += 1
    
isUsed = [0] * (num)
cnt = 0
for i in range(m):
    words = list(input().rstrip().split(","))
    for word in words:
        if word not in keyword.keys():
            continue
        if isUsed[keyword[word]] == 0:
            cnt += 1
            isUsed[keyword[word]] = 1
    print(num - cnt)