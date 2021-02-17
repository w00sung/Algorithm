import sys
read = sys.stdin.readline

sticks = list(read().rstrip())
valid = 0 # 유효한 막대기
res = 0 # 결과값

for i in range(len(sticks)):
    if i < len(sticks)-1:
        # 레이저 등장!
        if sticks[i] == "(" and sticks[i+1] == ")":
            res += valid
        # 막대기 등장! -- (유효한 막대기 + 1 && 결과값 +1)
        elif sticks[i] == "(":
            valid += 1
            res += 1
        # 막대기 끝! -- (레이저 끝과 구분 필요)
        elif sticks[i] == ")" and sticks[i-1] != "(":
            valid -= 1

print(res)
