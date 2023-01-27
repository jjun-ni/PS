import sys

input = sys.stdin.readline

n, k = map(int, input().split())

students = list(map(int, input().split()))

diff = []
for i in range(1,n):
    diff.append(students[i] - students[i-1])
    
total_cost = 0
diff.sort(reverse=True)

for i in range(k-1, n-1):
    total_cost += diff[i]

print(total_cost)