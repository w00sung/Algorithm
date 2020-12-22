from collections import deque
import sys
read = sys.stdin.readline


n , k = map(int,read().rstrip().split())

num = list((read().rstrip()))
stack = deque()
stack_right = deque()
res = deque()
# k개를 남겨두고
for i in range(n):
    now = int(num[i])
    if i <= (n-k):

        # 이번 녀석이 가장 크다고 했던 녀석보다 크면
        while stack and stack[-1] < now:
            
            stack.pop()

        # 가장 큰 녀석의 num을 담는다.
        stack.append(now)

    else:
        stack_right.append(now)

res.append(stack.popleft())
# 이제 k-1 개 찾으면됨
k -= 1
n_left = stack[0]
n_right = stack_right[0]

while k > 0:
    if n_left >= n_right:
        res.append(stack.popleft())
        n_left = stack[0]
    
    # 우측 덱으로 넘어옴
    else:
        # 구해야 될 것 k개 남았으면 == stack_right 개수랑 똑같으면 그대로 붙여넣기
        if len(stack_right) == k:
            while stack_right:
                res.append(stack_right.popleft())
        
        break
        
        # 우측 덱에 더 많은 숫자가 들어있어. 비교가 필요해 
        # 9 3 7 5 6 중 순서대로 3개 뽑기
        else:
            while True:
                res.append(stack_right.popleft())
            res.append(stack_right.popleft())
            stack = stack_right
            stack.popleft()

    k -= 1

print(res)