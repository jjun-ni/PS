import sys

input = sys.stdin.readline

n = int(input())
res = ["" for _ in range(n)]

def print_star(x,y,size, blank):
    if size == 1:
        if blank:
            res[y] += " "
        else:
            res[y] += "*"
        return
    next_size = size // 3
    print_star(x,y,next_size,blank)
    print_star(x+next_size,y,next_size,blank)
    print_star(x+2*next_size,y,next_size,blank)
    print_star(x,y+next_size,next_size,blank)
    print_star(x+next_size,y+next_size,next_size,1)
    print_star(x+2*next_size,y+next_size,next_size,blank) 
    print_star(x,y+2*next_size,next_size,blank)
    print_star(x+next_size,y+2*next_size,next_size,blank)
    print_star(x+2*next_size,y+2*next_size,next_size,blank)

print_star(0,0,n,0)
for i in range(n):
    print(res[i])