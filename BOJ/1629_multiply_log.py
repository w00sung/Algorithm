import math
import sys
sys.setrecursionlimit(10**6)
read = sys.stdin.readline


tot = 0
# a를 b제곱
def mul(a,b):
    # 연속 제곱 회수
    global tot
    ans = a
    cnt = 1
    # 로그 계산이 오래걸린다.
    # logb = int(math.log(b,2))
    # 로그 번 만큼 제곱
    while True:
        # *** 초반에 더 곱해줘도 될 듯?
        cnt *= 2
        # 내 기준보다 많이 제곱되면 out
        if cnt > b:
            break
        ans *= ans

        tot += 1

    # 로그 계산 대체
    cnt /= 2
    
    # if logb == 0:


    # 제곱이 안남으면 -- 무조건 1남음 -- 본인호출
    if b == cnt:
        return ans
    else:
        return ans*mul(a,b-cnt)


# a,b,c = map(int,read().rstrip().split())

mul(2,1000)
print(tot)