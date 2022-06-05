
N=int(input())
num=[]
Y=[1]*N

for i in range(N):
    x,y=map(int,input().split())
    num.append([x,y])
numm=num.copy()
numm.sort()
numm.reverse()

for i in range(len(numm)):
    for j in range(len(numm)):
        if i>j:
            if numm[j][0]!=numm[i][0]:
                if numm[i][1]<numm[j][1]:
                    Y[i]+=1
#print(num)
#print(numm)
#print(Y)
ans=[]
for i in range(N):
    a=numm.index(num[i])
 #   print(a)
    ans.append(Y[a])

print(*ans)


