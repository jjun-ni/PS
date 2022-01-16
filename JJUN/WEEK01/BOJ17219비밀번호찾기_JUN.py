import sys
input = sys.stdin.readline
N, M = map(int, input().split())
hash_table={}
for i in range(N):
    address, password = map(str, input().split())
    hash_table[address]=password
for i in range(M):
    site = input().rstrip()
    print(hash_table[site])