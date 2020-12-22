import sys
read = sys.stdin.readline

stack = []
bracket = list(read().rstrip())
tot = 0
# 검증
cnt = 0
y = True
# 그동안 더해놓은거 pop x now
try :
    for br in bracket:
        calc = 0

        # 시작 괄포들은 그냥 넣는다.
        if br == "(":
            stack.append(br)

        elif br == "[":
            stack.append(br)


        # 닫는 괄호들 등장

        elif br == ")":
            if stack[-1] == "(":
                stack.pop()
                stack.append(2)
            
            else:
                while True:
                    num = stack.pop()
                    if num == "(":
                        break
                    calc += num
                stack.append(2*calc)
        
        elif br == "]":
            if stack[-1] == "[":
                stack.pop()
                stack.append(3)
            else:
                while True:
                    # "[" 나올 때까지 숫자 더해준다.
                    num = stack.pop()
                    if num == "[":
                        break
                    calc += num
                # "[" 등장하면,
                # 그자리에 3을 곱한 숫자로 합으로 대체
                stack.append(3*calc)


    while stack:
        num = stack.pop()
        tot += num

    print(tot)
except:
    print(0)

