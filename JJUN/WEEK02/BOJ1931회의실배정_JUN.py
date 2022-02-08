import sys
input = sys.stdin.readline
N = int(input())
x = []
for i in range(N):
    s, f = map(int, input().split())
    x.append([s, f])
x.sort(key = lambda x:x[0])
x.sort(key = lambda x:x[1])
count = 1
end_time = x[0][1]
for i in range(1, N):
    if x[i][0] >= end_time:
        count += 1
        end_time = x[i][1]
print(count)