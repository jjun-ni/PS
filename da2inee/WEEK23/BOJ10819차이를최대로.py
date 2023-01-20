from itertools import permutations
N = int(input())
A = list(map(int,input().split()))
ans = 0 
for array in permutations(A,N):
    diff = 0
    for j in range(N-1):
        diff += abs(array[j+1] - array[j])
    ans = max(ans,diff)
print(ans)


