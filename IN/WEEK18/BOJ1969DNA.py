import sys

input = sys.stdin.readline

n, m = map(int, input().split())

dnas = []
dna_to_num = {"T":4, "A":1, "G":3, "C":2 }
num_to_dna = {4:"T", 1:"A", 3:"G", 2:"C"}
for i in range(n):
    dnas.append(input().rstrip())
    
dnas.sort()
    
min_score = 0
min_str = ""

for i in range(m):
    res = [0] * 5     
    for j in range(n):
        res[dna_to_num[dnas[j][i]]] += 1
    score = max(res)
    min_score += n - score
    for j in range(1,5):
        if res[j] == score:
            min_str += num_to_dna[j]
            break

print(min_str)
print(min_score)