from collections import deque
import sys
read = sys.stdin.readline


n , k = map(int,read().rstrip().split())

# k개 뽑는게 아니라, n-k개 뽑으면 된다.
k = n-k

# 아래는 n개 중 k개 뽑는 코드
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

# 좌측 popleft 시키면서 우측 append 해준다. 
# 이 때, 동일기준 적용
while True:

    res.append(stack.popleft())
    k -= 1
    if k == 0:
        break
    now = stack_right[0]
    while stack and stack[-1] < now:
        stack.pop()

    stack.append(stack_right.popleft())

print("".join([str(i) for i in res]))


# res.append(stack.popleft())
# # 이제 k-1 개 찾으면됨
# k -= 1
# n_left = stack[0]
# n_right = stack_right[0]

# while k > 0:
#     if n_left >= n_right:
#         res.append(stack.popleft())
#         n_left = stack[0]
    
#     # 우측 덱으로 넘어옴
#     else:
#         # 구해야 될 것 k개 남았으면 == stack_right 개수랑 똑같으면 그대로 붙여넣기
#         if len(stack_right) == k:
#             while stack_right:
#                 res.append(stack_right.popleft())
        
#         break
        
#         # 우측 덱에 더 많은 숫자가 들어있어. 비교가 필요해 
#         # 9 3 7 5 6 중 순서대로 3개 뽑기
#         else:
#             while True:
#                 res.append(stack_right.popleft())
#             res.append(stack_right.popleft())
#             stack = stack_right
#             stack.popleft()

#     k -= 1

# print(res)