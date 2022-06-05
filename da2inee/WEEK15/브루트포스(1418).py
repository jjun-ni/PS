N=int(input())
K=int(input())
count=0
num=[]
for i in range(2,N+1):
    for j in range(2,N):
        if j<i:
            if i%j==0:
                num.append(i//j)
    num.sort()
    num.reverse()  
    if len(num)==0:
        count+=1
        i+=1
        
      
    else:
        for k in range(len(num)):
            for m in range(2,num[k]+1):
                if num[k]%m==0:
                    num.pop(k)




    print(num)
    num=[]
    
print(count)



