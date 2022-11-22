N,M = map(int,input().split())
array = list(map(int,input().split()))
cnt = 0 
start = 0
end = 1
ans = 0
if N==1:
    if array[0] >M:
        print(0)
        exit(0)
    else:
        print(array[0])
        exit(0)
if array[start] <= M:
        ans = array[start]
while start <= end and end < N:
    if ans + array[end] <= M:
        ans += array[end]
        end +=1
    elif ans + array[end] > M:
        if array[end]>M:
            start = end+1
            end +=1
            ans = 0
        else:
            ans -= array[start]
            start+=1
    cnt = max(cnt,ans)
print(cnt)