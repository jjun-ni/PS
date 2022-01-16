import sys
input = sys.stdin.readline
N = int(input())
for i in range(N):
    hash_table = {}
    kind_cloth_type = set([])
    num_cloth_type = 0
    li = [0 for i in range(30)]
    M = int(input())
    if M == 0:
        print(0)
    else:
        for j in range(M):
            cloth_name, cloth_type = map(str, input().split())
            if cloth_type in kind_cloth_type:
                k = hash_table[cloth_type]
                li[k-1] += 1
            else:
                kind_cloth_type.add(cloth_type)
                num_cloth_type += 1
                hash_table[cloth_type] = num_cloth_type
                li[num_cloth_type-1] += 1
        num = 1
        for l in range(num_cloth_type):
            num *= li[l]+1
        print(num-1)