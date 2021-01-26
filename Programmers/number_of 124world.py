import sys
read = sys.stdin.readline

n = 10
num = ['4', '1', '2']
stack = []
answer = ''
while n > 0:

    # stack.append(num[n % 3])
    answer = num[n%3] + answer
    if n % 3 == 0:
        n = (n//3) - 1
    else:
        n = n//3

    # 뒤에 붙이기!
# for i in range(len(stack)-1, -1, -1):
#     answer.append(stack[i])

# answer = ''.join(answer)
print(answer)
