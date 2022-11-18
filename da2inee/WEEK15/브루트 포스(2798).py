N,M=map(int,input().split())
num=list(map(int,input().split()))
count=[]
count2=[]
for i in range(len(num)):
    for j in range(1,len(num)):
        for k in range(2,len(num)):
            if i<j<k:
                ans=M-(num[i]+num[j]+num[k])
                if ans>=0:
                    count.append(ans)
                    #print(count)
count.sort()
print(M-count[0])