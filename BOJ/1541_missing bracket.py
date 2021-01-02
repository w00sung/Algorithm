import sys
read = sys.stdin.readline

# math : 수식
math = read().rstrip()

# - 가 나오기 이전과 이후로 숫자를 분류한다.

# For 문 사용 index 찾기
minus_idx = 0
for i in range(len(math)):
    if math[i] == "-":
        minus_idx = i
        break

## method 활용
# minus_idx = math.index("-")

# 마이너스 있으면
if minus_idx != 0:
    math_plus = math[:minus_idx]
    math_minus = math[minus_idx+1:]

# 없으면
else:
    math_plus = math
    math_minus = ""   

plus_num = []
minus_num = []
plus = 0
minus = 0
# 수식 계산
for i in range(len(math_plus)+1):
    # +를 만나거나, 끝에 도달 했으면,
    # 좌측 부터 조건부 실행됨

    if i == len(math_plus) or math_plus[i] == "+":
        # 들어가 있던 숫자들 붙여서, 숫자로 만들어준다.
        # 만들어진 숫자를 plus 에 더한다.
        plus += int("".join(plus_num))
        # 지워줌
        plus_num.clear()
        continue

    plus_num.append(math_plus[i])

# =마이너스 없을 수도 있다.
if len(math_minus) > 0:
    for i in range(len(math_minus)+1):
        # +를 만나거나, 끝에 도달 했으면,
        # 좌측 부터 조건부 실행됨

        if i == len(math_minus) or math_minus[i] in ("+","-"):
            # 들어가 있던 숫자들 붙여서, 숫자로 만들어준다.
            # 만들어진 숫자를 plus 에 더한다.
            minus += int("".join(minus_num))
            # 지워줌
            minus_num.clear()
            continue
        
        minus_num.append(math_minus[i])




print(plus-minus)