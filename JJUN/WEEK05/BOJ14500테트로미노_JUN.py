import sys
input = sys.stdin.readline

def find_max(arr, n, m):
    result = list()
    # ㅡ
    for i in range(n):
        for j in range(m-3):
            maximum = 0
            for k in range(4):
                maximum += arr[i][j+k]
            result.append(maximum)
    # ㅁ
    for i in range(n-1):
        for j in range(m-1):
            maximum = 0
            for k in range(2):
                maximum += arr[i+k][j+k]
            maximum += arr[i+1][j]
            maximum += arr[i][j+1]
            result.append(maximum)
    # L
    for i in range(n-2):
        for j in range(m-1):
            maximum = 0
            for k in range(3):
                maximum += arr[i+k][j]
            maximum += arr[i+2][j+1]
            result.append(maximum)
    # ㄱ
    for i in range(n-1):
        for j in range(m-2):
            maximum = 0
            for k in range(3):
                maximum += arr[i][j+k]
            maximum += arr[i+1][j+2]
            result.append(maximum)
    # _/-
    for i in range(n-2):
        for j in range(m-1):
            maximum = 0
            for k in range(2):
                maximum += arr[i+k][j]
            maximum += arr[i+1][j+1]
            maximum += arr[i+2][j+1]
            result.append(maximum)
    # Z
    for i in range(n-1):
        for j in range(m-2):
            maximum = 0
            for k in range(2):
                maximum += arr[i][j+k]
            maximum += arr[i+1][j+1]
            maximum += arr[i+1][j+2]
            result.append(maximum)
    # T
    for i in range(n-1):
        for j in range(m-2):
            maximum = 0
            for k in range(3):
                maximum += arr[i][j+k]
            maximum += arr[i+1][j+1]
            result.append(maximum)

    return max(result)


def rotate_90(arr, n, m):
    result = [[0 for j in range(n)] for i in range(m)]

    for i in range(m):
        for j in range(n):
            result[i][j] = arr[n-j-1][i]

    return result


def main():

    n, m = map(int, input().split())
    arr = list()
    for i in range(n):
        arr.append(list(map(int, input().split())))

    maximum = 0
    maximum = max(maximum, find_max(arr, n, m))
    arr = rotate_90(arr, n, m)
    maximum = max(maximum, find_max(arr, m, n))
    arr = rotate_90(arr, m, n)
    maximum = max(maximum, find_max(arr, n, m))
    arr = rotate_90(arr, n, m)
    maximum = max(maximum, find_max(arr, m, n))

    print(maximum)

    return

if __name__ == "__main__":
    main()