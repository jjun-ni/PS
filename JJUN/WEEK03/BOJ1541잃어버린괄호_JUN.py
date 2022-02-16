N = input()
L = len(N)
num = []
number = ''
opr = []
for i in range(L):
    if N[i] != '+' and N[i] != '-':
        number += str(N[i])
        if i == L-1:
            num.append(int(number))
    else:
        num.append(int(number))
        number = ''
        opr.append(N[i])
count = 0
point = True
for i in range(len(opr)):
    if opr[i] == '-':
        breakpoint = i
        point = False
        break
if point:
    for i in range(len(num)):
        count += num[i]
else:
    for i in range(len(num)):
        if i <= breakpoint:
            count += num[i]
        else:
            count -= num[i]
print(count)