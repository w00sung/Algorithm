import sys
read = sys.stdin.readline

N = int(read())
towers = list(map(int,read().rstrip().split()))
stack = []
order_list = []
answer = [0] * N

def clean_up(stack, h):
    while stack and h >= stack[-1] :
        stack.pop()
        order_list.pop()

for i in range(len(towers)):

    clean_up(stack,towers[i])

    if stack :
        answer[i] = order_list[-1]
    else:
        answer[i] = 0

    stack.append(towers[i])
    order_list.append(i+1)

for i in range(N):
    print(answer[i], end = " ")