N=int(input())
a=[]
for i in range(N):
    num=list(str(i))
    #print(num)
    ans=i
    for k in range(len(num)):
        
        ans+=int(num[k])
    if N==ans:
        a.append(i)
    else:
        False
if len(a)==0:
    print("0")
else:
    print(min(a))

    