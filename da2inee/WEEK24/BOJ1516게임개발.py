from collections import deque
N = int(input())
building = []
indegree = [0] * (N+1)
node = [[]for _ in range(N+1)]
for i in range(1,N+1):
    data = list(map(int,input().split()))[:-1]
    building.append(data)
    for j in data[1:]:
        node[j].append(i)
        indegree[i] += 1

dp = [0] * (N + 1)
q = deque()
for i in range(1,N+1):
    if indegree[i] == 0:
        q.append(i)
while q:
    x = q.popleft()
    dp[x] += building[x-1][0]
    for j in node[x]:
        indegree[j] -= 1
        dp[j] = max(dp[x],dp[j])
        if indegree[j] == 0:
            q.append(j)
for i in range(1,N+1):
    print(dp[i])

    

