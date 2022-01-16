T = int(input())
Q = [0] * 101
def P(N):
    if N <= 3:
        return 1
    elif N >= 4 and N <= 5:
        return 2
    if Q[N] != 0:
        return Q[N]
    Q[N] = P(N-1) + P(N-5)
    return Q[N]
for i in range(T):
    N = int(input())
    print(P(N))