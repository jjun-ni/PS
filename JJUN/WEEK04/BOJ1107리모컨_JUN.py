import sys
input = sys.stdin.readline
n = input().rstrip() # 목표 채널의 str값
d = int(input()) # 고장난 버튼의 개수
def mini(num1, n): # 남아있는 버튼으로 누를 수 있는 n보다 작은 채널 중 가장 큰 채널의 str값
    nt = True # 채널값이 이미 n보다 작아졌는지 확인하기 위한 값
    nodab = True # False가 되면 n보다 자리수가 작아져야만 n보다 작은 채널을 누를 수 있음을 의미
    mn = '' # 채널값
    for i in range(len(n) - 1):
       if nodab:
            if nt:
                if u <= int(n[i + 1]):
                    if int(n[i]) in num1:
                        mn += n[i]
                    else:
                        c = 0
                        for j in num1:
                            if j < int(n[i]):
                                mn += str(j)
                                nt = False
                                break
                            c += 1
                        if c == N:
                            nt = False
                            nodab = False
                else:
                    if u < int(n[i]):
                        for l in num1:
                            if l < int(n[i]):
                                mn += str(l)
                                nt = False
                                break
                    else:
                        nt = False
                        nodab = False
            else:
                mn += str(v)
       else:
            mn = str(v) * (len(n)-2)
            break

    if nt:
        for i in num1:
            if i <= int(n[len(n) - 1]):
                mn += str(i)
                break
    else:
        mn += str(v)
    if len(mn) >= 2 and mn[0] == '0':
        mn = mn[1:]
    if mn == '':
        mn = '9999999'
    return mn

def maxi(num2, n): #남아있는 버튼으로 누를 수 있는 n보다 큰 채널 중 가장 작은 채널의 str값
    mt = True # 채널값이 이미 n보다 커졌는지 확인하기 위한 값
    mx = '' # 채널값
    nodab = True
    if v < int(n[0]):
        mt = False
        if u != 0:
            mx += str(u)
        else:
            if len(num2) >= 2:
                mx += str(num2[1])
            else:
                mx += str(u)
    for i in range(len(n) - 1):
        if nodab:
            if mt:
                if v >= int(n[i + 1]):
                    if int(n[i]) in num2:
                        mx += n[i]
                    else:
                        c = 0
                        for j in num2:
                            if j > int(n[i]):
                                mx += str(j)
                                mt = False
                                break
                            c += 1
                        if c == N:
                            nt = False
                            nodab = False
                else:
                    if v > int(n[i]):
                        for l in num2:
                            if l > int(n[i]):
                                mx += str(l)
                                mt = False
                                break
                    else:
                        nodab = False
                        mt = False
            else:
                mx += str(u)
        else:
            mx = str(u) * len(n)
    if mt:
        for i in num2:
            if i >= int(n[len(n) - 1]):
                mx += str(i)
                break
    else:
        mx += str(u)
    if int(mx) == 0:
        mx = '9999999'
    return mx
if d != 0: # 고장난 버튼이 1개 이상일 때
    delete = list(map(int, input().split()))
    num1 = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    num2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in delete:
        num1.remove(i)
        num2.remove(i)
    N = len(num1)
    if d != 10: # 고장난 버튼이 1개 이상 10개 미만일 때
        u = min(num1)
        v = max(num1)
        print(min(abs(int(n) - int(mini(num1, n))) + len(mini(num1, n)),
                  abs(int(maxi(num2, n)) - int(n)) + len(maxi(num2, n)), abs(int(n) - 100)))
    else: # 고장난 버튼이 10개일 때
        print(abs(int(n)-100))
else: # 고장난 버튼이 0개일 때
    print(min(abs(int(n)-100), len(n)))