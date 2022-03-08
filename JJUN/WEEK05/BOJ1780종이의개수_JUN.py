import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))
def equal(sum):
    for i in range(1, 9):
        if sum[i] != sum[i-1]:
            return False
    if sum[0] == [1, 0, 0] or sum[0] == [0, 1, 0] or sum[0] == [0, 0, 1]:
        return True
    else:
        return False
def divide(x, y, N):
    if N == 1:
        if graph[x][y] == -1:
            return [1, 0, 0]
        elif graph[x][y] == 0:
            return [0, 1, 0]
        else:
            return [0, 0, 1]
    sum = [0 for _ in range(9)]
    dx = [x, x, x, x + N//3, x + N//3, x + N//3, x + 2*N//3, x + 2*N//3, x + 2*N//3]
    dy = [y, y + N//3, y + 2*N//3, y, y + N//3, y + 2*N//3, y, y + N//3, y + 2*N//3]
    for i in range(9):
        sum[i] = divide(dx[i], dy[i], N//3)
    if equal(sum):
        return sum[0]
    else:
        count1, count2, count3 = 0, 0, 0
        for i in range(9):
            count1 += sum[i][0]
            count2 += sum[i][1]
            count3 += sum[i][2]
        return [count1, count2, count3]

count1, count2, count3 = divide(0, 0, N)
print(count1)
print(count2)
print(count3)
