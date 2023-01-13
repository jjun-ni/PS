world = list(input())
M = int(input())
stack = []
for _ in range(M):
    note = list(input().split())
    if note[0] == 'P':
        world.append(note[1])
    if note[0] == 'L':
        if len(world) > 0:
            word = world[-1]
            stack.append(word)
            world.pop()
    if note[0] == 'B':
        if len(world) > 0 :
            world.pop()    
    if note[0] == 'D':
        if len(stack) > 0:
            word2 = stack[-1]
            world.append(word2)
            stack.pop()
       

for i in range(len(stack)):
    ans = stack[-1]
    world.append(ans)
    stack.pop()
print(''.join(world))
    

# insert랑 remove사용하면 시간초과 나옴
# append랑 pop 사용해야함 (stack 두개 사용하기)
