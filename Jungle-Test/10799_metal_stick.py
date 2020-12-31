import sys
read= sys.stdin.readline
stack = []

metal = list(read().rstrip())
# n logn 필요하다.

cnt = 0
ray = 0
# for 문 n
for m in metal:

    # 레이저 들어왔음
    if stack and ( m == ")" and stack[-1] == "(" ):
        stack.pop()
        if len(stack) != 0 :
            stack.append(1)
            ray += 1
            cnt += (len(stack) -ray)
        else:
            cnt +=1

    elif stack and ( m== ")" and stack[-1] == 1):
        
        # 레이저 뽑기
        while stack and stack[-1] == 1:
            ray -= 1
            stack.pop()

        stack.pop()
        cnt += 1

        # stack 남아있으면 그건 막대기

    # 막대기 끝남
    elif m == ")":
        stack.pop()
        cnt += 1

    elif m == "(":
        stack.append(m)

print(cnt)
    
    