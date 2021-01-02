import sys
read = sys.stdin.readline

# math : 수식
# 마이너스 구분자로 다 나눠준다.
math = read().rstrip().split("-")

# split은 요소가 없어도 된다 
# ['55', '50+40']
# print(math)

plus = 0
# plus 요소
for plus_num in math[0].split("+"):
    plus += int(plus_num)


minus = 0

# minus 요소들
# 슬라이싱 질문!!
for minus_math in math[1:]:
    for minus_num in minus_math.split("+"):
        minus += int(minus_num)

print(plus-minus)

