import re
import sys
read = sys.stdin.readline


stack = [None] * 10000
ptr = 0
# for 문으로 돌릴 것임
def stack_command(command):
    global ptr

    # read().split() 하여서, command[0]으로 읽을 수도 있음
    if re.search('push',command):
        x = command[5:]
        # stack에 인덱스로 접근해서 넣어줄 수는 없나..? 
        # -- None 으로 미리 배열한 후!!!
        stack[ptr] = int(x)
        ptr += 1

    elif command == "pop":
        if ptr == 0:
            print(-1)
        else:
            ptr -= 1
            k = stack[ptr]
            print(k)
            # 후에 이 자리에 덮어 씌어짐

    elif command == "size":
        print(ptr)

    elif command == "empty":
        if ptr > 0:
            print(0)
        
        else:
            print(1)

    elif command == "top":
        if ptr == 0:
            print(-1)
        else:
            top = stack[ptr-1]
            print(top)

n = int(read())
for _ in range(n):
    stack_command(read().rstrip())