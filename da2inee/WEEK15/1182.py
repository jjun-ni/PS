#combinations  써도 되는가
import itertools
from typing import Counter
N,S=map(int,input().split())

num=list(map(int,input().split()))

print(num)
count=0
for i in range(1,N+1):
    BF=list(itertools.combinations(num,i))
    print(BF)
    for j in BF:
        if sum(j)==S:
            count+=1
        
    
print(count)