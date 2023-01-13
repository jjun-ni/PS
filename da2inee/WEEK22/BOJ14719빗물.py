H, W = map(int,input().split())
block = list(map(int,input().split()))
ans = 0
for i in range(1,W-1):
    left_max = max(block[:i])
    right_max = max(block[i+1:])
    rain = min(left_max,right_max)

    if rain > block[i]:
        ans += (rain - block[i])
print(ans)

#알고리즘 생각해내는 게 너무 어려웠음
