num = list(input())
numnum = num + num
anum = 0
for i in num:
    if i == "a":
        anum+=1
cnt = 1000
for i in range(len(num)):
    ans = 0
    for j in range(i, i + anum):
        if numnum[j] == 'b':
            ans +=1
    cnt = min(cnt, ans)
print(cnt)