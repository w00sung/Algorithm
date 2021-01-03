import sys
read = sys.stdin.readline

ans = [0] * 2
num = list(map(int,read().rstrip()))


def count_block(num):
    # 다른 숫자 나올 때 마다 끊어줄 거임
    check = num[0]
    for i in range(len(num)):
            
        # 다를 때만 작동시켜주면 됨
        if num[i] != check:

            # "앞전에" 셌던 녀석 + 1 해주기
            ans[check] += 1
            check = num[i]
        
        if i == len(num) - 1:
            ans[check] += 1

        # 마지막에는 블럭 처리!!

count_block(num)
# print(ans)
print(min(ans))