import sys

input = sys.stdin.readline

a, b = map(int, input().split())

prime = [1] * (b+1)
prime[0] = 0
prime[1] = 0
prime_list = []

for i in range(2, b+1):
    if prime[i]:
        prime_list.append(i)
        mul = 2
        num = i * mul
        while num <= b:
            prime[num] = 0
            mul += 1
            num = i * mul

under_prime = [0] * (b+1)
under_prime[2] = 1

def count_prime(num):
    res = 0
    if num == 1:
        return 0
    if under_prime[num] != 0:
        return under_prime[num]
    for i in prime_list:
        if num % i == 0:
            res = count_prime(num // i) + 1
            under_prime[num] = res
            return res
            
cnt = 0
for i in range(a, b+1):
    num_prime = count_prime(i)
    if prime[num_prime]:
        cnt += 1
print(cnt)
