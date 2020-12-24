import sys
read= sys.stdin.readline
stack = []
opener = []
metal = list(read().rstrip())
# n logn 필요하다.

cnt = 0
ray = 0
# for 문 n
for m in metal:

    # 따로 받아보자.
    # 스택에는 괄호 열었던 개행 괄호만 담는다.
    # 앞에 ( 인데 뒤에 ))만나면 하나 팝 & 스택개수만큼 더하기
     
    # 레이저 들어왔음
    if stack and ( m == ")" and stack[-1] == "(" ):
        stack.pop()
        ray += 1
        cnt += (len(stack) - ray)

    # 닫는거 들어왔음
    elif stack and m== ")" :
        cnt += 1
        # 레이저 뽑기

        # stack 남아있으면 그건 막대기
    stack.append(m)

print(cnt)    