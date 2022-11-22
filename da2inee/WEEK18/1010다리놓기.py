T = int(input())
def factorial(x):
    f = 1
    for i in range(1,x+1):
        f *= i
    return f

for i in range(T):
    a, b = map(int,input().split())
    ans = factorial(b)//(factorial(b-a)*factorial(a))
    print(ans)
    
    