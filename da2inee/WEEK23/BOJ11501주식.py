T = int(input())
def stock(account):
    coin = 0
    m = max(account)
    ans = []
    if account[0] == m:
        coin = 0
        return 0
    else:
        for i in range(N):
            if account[i] != m:
                coin -= account[i]
                ans.append(i)
            else:
                coin += len(ans) * account[i]
                ans = []
                if i+1 == N:
                    return coin
                else:
                    m = max(account[i+1:])
        return ans 

for i in range(T):
    N = int(input())
    account = list(map(int,input().split()))
    print(stock(account))

# 앞에서부터 반복문 돌려서 맞기는 했는데 비효율적으로 푼것 같다.
# 뒤에서 부터 반복문 돌리면서 max 값 변경해주면 훨씬 더 효율적으로 풀 수 있다.