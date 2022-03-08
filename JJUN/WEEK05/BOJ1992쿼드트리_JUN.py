import sys
input = sys.stdin.readline
N = int(input())
video = []
for i in range(N):
    video.append(list(map(int, input().rstrip())))

def compress(x, y, len):
    if len == 1:
        return "1" if video[x][y] == 1 else "0"
    equal = True
    for i in range(x, x+len):
        for j in range(y,y+len):
            if video[i][j] != video[x][y]:
                equal = False
                break
    if equal:
        return str(video[x][y])
    else:
        res = "("
        x_list = [x, x, x + len // 2, x + len // 2]
        y_list = [y, y + len // 2, y, y + len // 2]

        for i in range(4):
            res += compress(x_list[i], y_list[i], len // 2)
        res += ")"
    return res
print(compress(0, 0, N))