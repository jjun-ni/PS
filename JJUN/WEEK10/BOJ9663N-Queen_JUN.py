n = int(input())
cnt = 0

def N_Queen(selected, order):
    global n, cnt
    if order == n:
        cnt += 1
        return
    for i in range(n):
        new_pos = (order, i)
        flag = False
        for y,x in selected:
            if order == y or i == x or abs(order-y) == abs(i-x):
                flag = True
                break
        if flag is False:
            N_Queen(selected + [(order, i)], order+1)

for i in range(n):
    N_Queen([(0, i)], 1)
print(cnt)
