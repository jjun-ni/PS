import sys

input = sys.stdin.readline

first_B = ["BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB"]
first_W = ["WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW","WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW"]

N, M = map(int, input().split())
board = []

for i in range(N):
    one_line = input().rstrip()
    board.append(one_line)

change = 64

for i in range(N - 7):
    for j in range(M - 7):
        B_tmp_change = 0
        W_tmp_change = 0
        for y in range(8):
            for x in range(8):
                if first_B[y][x] != board[y + i][x + j]:
                    B_tmp_change += 1
                if first_W[y][x] != board[y + i][x + j]:
                    W_tmp_change += 1
        change = min(change, B_tmp_change, W_tmp_change)

print(change)