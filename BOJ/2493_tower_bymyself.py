import sys
read = sys.stdin.readline

n = int(read())
# 타워 높이
tower = list(map(int,read().rstrip().split()))
# 유의미한 것 -- 현존 가장 높은 것
stack = []

# 0으로 초기화, 맞는 놈 있으면 갱신
res = [0] * n

# 타워 하나씩 돌면서 대조할거다.
for i in range(n):

    now = tower[i]

    # 스택 없으면 pass 해야함
    while stack and tower[stack[-1]] < now:
        # 나보다 작은 놈 다 뽑아 !
        # 나보다 큰놈만 남거나, 다 뽑힘
        stack.pop()

    # stack에 남아 있으면, 그 놈한테 쏜다.
    # 안남아 있으면, 본인이 가장 큰거임 -- 0 유지
    if stack:
        res[i] = stack[-1] + 1

    # 마지막에 본인 넣어주기 
    # -- stack 마지막에는 
    # stack은 큰 순서 대로 들어가있음
    # 바로 작은 놈이면 res 바뀌고 바로 append 됨
    stack.append(i)

print(*res)