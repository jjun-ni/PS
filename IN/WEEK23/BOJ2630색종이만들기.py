import sys

input = sys.stdin.readline

def perfect_square(square):
    global blue, white
    l = len(square)
    if len(square) == 1:
        if square[0][0] == 1:
            blue += 1
            return True
        else:
            white += 1
            return True
    check_white = 0
    check_blue = 0
    for i in range(l):
        for j in range(l):
            if square[i][j] == 1:
                check_blue += 1
            else:
                check_white += 1

    if check_white == l * l:
        white += 1
    elif check_blue == l * l:
        blue += 1
    else:
        middle = len(square) // 2
        quarter1 = []
        quarter2 = []
        quarter3 = []
        quarter4 = []
        for z in range(len(square) // 2):
            quarter1.append(square[z][:middle])
            quarter2.append(square[z][middle:])
            quarter3.append(square[z + middle][:middle])
            quarter4.append(square[z + middle][middle:])
        perfect_square(quarter1)
        perfect_square(quarter2)
        perfect_square(quarter3)
        perfect_square(quarter4)

N = int(input())
board = []
blue = 0
white = 0
for _ in range(N):
    board.append(list(map(int, input().split())))
perfect_square(board)
print(white)
print(blue)

