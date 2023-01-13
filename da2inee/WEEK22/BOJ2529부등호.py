from itertools import permutations
k = int(input())
array = list(input().split())
result = []
for data in permutations([0,1,2,3,4,5,6,7,8,9], k+1):
    ans = False
    for i in range(len(array)):
        if array[i] == "<":
            if data[i] < data[i+1]:
                ans = True
                continue
            else:
                ans = False
                break
        elif array[i] == ">":
            if data[i] > data[i+1]:
                ans = True
                continue
            else:
                ans = False
                break
    if ans == True:
        result.append(data)
print(''.join(map(str,list(max(result)))))
print(''.join(map(str,list(min(result)))))

        