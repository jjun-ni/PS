N, M = map(int,input().split())
array = []
for i in range(N):
    array.append(input())
def hamming_distance(i):
    a = 0
    b = 0
    c = 0
    d = 0
    for j in range(N):
        if array[j][i] == "T":
            a += 1
        elif array[j][i] == "A":
            b += 1
        elif array[j][i] == "G":
            c += 1
        elif array[j][i] == "C":
            d += 1
    if max(a,b,c,d) == b:
        dna.append("A") 
    elif max(a,b,c,d) == d:
        dna.append("C")
    elif max(a,b,c,d) == c:
        dna.append("G")
    elif max(a,b,c,d) == a:
        dna.append("T") 
    return N - max(a,b,c,d)
cnt = 0
dna = []
for i in range(M):
    ans = hamming_distance(i) 
    cnt += ans
DNA = dna[0].strip('')
for i in range(1,len(dna)):
    DNA += dna[i].strip('')
print(DNA)
print(cnt)
        
