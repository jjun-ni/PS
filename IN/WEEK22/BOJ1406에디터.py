import sys

input = sys.stdin.readline

target = input().rstrip()

m = int(input())

front = []
front_size = 0
back = []
back_size = 0

for i in range(len(target)):
    front.append(target[i])
    front_size += 1

for _ in range(m):
    command = input().rstrip()
    if len(command) > 1:
        command, insert = command.split()
        front.append(insert)
        front_size += 1
    else:
        if command == "L":
            if front_size > 0:
                move = front.pop()
                back.append(move)
                front_size -= 1
                back_size += 1
        elif command == "D":
            if back_size > 0:
                move = back.pop()
                front.append(move)
                back_size -= 1
                front_size += 1
        elif command == "B":
            if front_size > 0:
                front.pop()
                front_size -= 1

for i in front:
    print(i, end="")
for i in reversed(back):
    print(i, end="")