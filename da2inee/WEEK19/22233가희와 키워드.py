import sys
input = sys.stdin.readline
N,M = map(int,input().split())
'''
keyword = []
for i in range(N):
    keyword.append(input().rstrip())
memo = []

for i in range(M):
    memo.append(input().rstrip().split(","))
print(memo)
for i in memo:
    for j in range(len(i)):
        if i[j] in keyword:
            keyword.remove(i[j])
    print(len(keyword))
'''
keyword = dict()
for i in range(N):
    keyword[input().rstrip()] = 1
ans = N
for i in range(M):
    memo = input().rstrip().split(",")
    for word in memo:
        if word in keyword.keys():
            if keyword[word] == 1:
                keyword[word] -= 1
                ans-=1
    print(ans)

    

            
