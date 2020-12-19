import sys
read = sys.stdin.readline

n = int(read())
tower = list(map(int,read().rstrip().split()))
# 나보다 큰 놈을 마지막으로 두는 stack
# 작은 놈은 pop 시킨다.
stack = []
# 결과 위치
res = [0] * n


# 앞에서부터 쭉 돌거야.
for i in range(n):
    now = tower[i]

    # 스택에 쌓여있고, 마지막 녀석이 나보다 작으면
    while stack and tower[stack[-1]] < now:
        stack.pop()
        # 결국 나보다 큰놈이 남거나, 다 뽑힌다.

    # 큰 놈이 남았으면
    if stack:
        # 지금 녀석의 안테나를 수신 받는 놈은 그 큰놈이다.
        # (+1: 문제에서 1번째부터 시작하기 때문에)
        res[i] = stack[-1]+1

    # 내 다음 녀석의 기준이 되야 하는 "지금"의 인덱스를 넣어준다.
    stack.append(i)

print(*res)

# 이게 스택인가....