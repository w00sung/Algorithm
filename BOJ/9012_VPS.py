import sys
read = sys.stdin.readline


cnt = 0
# 스택의 포인터 개념으로 접근
def is_vps(ps):
    cnt = 0

    for s in ps:

        if s == "(":
            cnt += 1

        else:
            cnt -= 1

        # 중간에 ")" 가 더 많이 나오면 끊어서 NO다
        if cnt < 0:
            return "NO"

    if cnt == 0:
        return "YES"

    # "(" 가 더 많으면 
    else:
        return "NO"

n = int(read())
for _ in range(n):

    print(is_vps(read().rstrip()))