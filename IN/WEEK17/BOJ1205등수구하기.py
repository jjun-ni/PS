import sys

input = sys.stdin.readline

n, score, p = map(int, input().split())
if n > 0:
    scores = list(map(int, input().split()))
    out_of_rank = True 
    if n < p:
        for i in range(n):
            if scores[i] <= score:
                print(i+1)
                out_of_rank = False
                break
        if out_of_rank:
            print(n+1)
    else:
        if score == scores[-1]:
            print(-1)
            out_of_rank = False
        else:
            for i in range(p):
                if scores[i] <= score:
                    print(i+1)
                    out_of_rank = False
                    break
        if out_of_rank:
            print(-1)
else:
    print(1)