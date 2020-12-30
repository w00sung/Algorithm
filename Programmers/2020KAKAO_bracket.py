from collections import deque


# 2단계, 분리 & u가 올바른가 올바르지 않은가

def split_bracket(p):
    if p == "":
        return

    is_right = True
    u = []
    v = deque(p)
    cnt = 0
    for i in range(len(p)):
        if p[i] == "(":
            cnt += 1

        elif p[i] == ")":
            cnt -= 1
        
        u.append(v.popleft())

        # 세는 도중 ")" 가 더 많이 나온 상황이 있다면
        if cnt < 0:
            is_right = False
        
        if cnt == 0:
            u = ''.join([str(i) for i in u])
            v = ''.join([str(i) for i in v])
            return u, v ,is_right



# split = split_bracket(p)

# u, v = split[0], split[1]
# u_right = split[2]

# u가 올바르지 않다면
def not_right(u,v):
    ans = "("
    # solution(v) 가 있다.
    ans =  ans + solution(v) + ")"
    for i in range(len(u)):
        if i == 0 or i == len(u)-1:
            continue
        else:
            if u[i] == "(":
                ans += ")"
            elif u[i] == ")":
                ans += "("

    return ans

def right(u,v):

    # u가 완전해짐
    if v == "":
        return u

    ans = u
    ans += solution(v)
    return ans

def solution(p):
    if p == "":
        return p

    u, v, u_right = split_bracket(p)

    if u_right == True:
        answer = right(u,v)

    elif u_right == False:
        answer = not_right(u,v)

    return answer
p = "(())"		

print(solution(p))