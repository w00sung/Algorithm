import sys
read = sys.stdin.readline

k = int(read())

# 움직여, 그거면 돼?

# n 개의 원판을 마지막 것 제외 옆으로 옮기기 
# 현재기둥, 빈 기둥, 목표 기둥 지정 필요

# cur : 현재, loc : 목표
l = []
# n개 원반 목표 기둥으로 옮기기
def hanoi(n, cur , loc):
    # print("n 단계 : 최종 목표는 {}에서 {} 로 가는 것입니다!".format(cur,loc))
    # n-1 개 기둥 매개 기둥으로 옮기기
    if n > 1:
        # print("n-1 : 1차 매개로 옮기기")
        hanoi (n-1, cur = cur, loc = 6- (loc + cur))
    
    # 큰 기둥 이동
    # print("{} 에서 {} 로 기둥 이동".format(cur,loc))
    # li.append[cur,loc]
    print(cur,loc)

    # n-1 개 기둥 매개 기둥에서 목표 기둥으로 옮기기

    if n > 1:
        # print("n-1 단계 : 2차 목표로 옮기기")
        hanoi(n-1, cur = 6-(loc + cur), loc = loc)

## *** 알고 있는 값을 입력하는 것이 시간 절약, 메모리 절약에 효율적 ****
print(2**k-1)

if k <= 20:
    hanoi(k,1,3)

