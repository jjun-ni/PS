n = int(input())
tree = [[] for _ in range(n)]
value = [[] for _ in range(n)]
for i in range(n-1):
    a,b,c = map(int,input().split())
    tree[a].append(b)
    value[a].append(c)
print(tree)
