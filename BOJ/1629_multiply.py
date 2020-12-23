import sys
read = sys.stdin.readline

cnt = 0

def mul(x,y):
    global c
    # print("{}의 {}승 소환!".format(x,y))
    
    # 숫자가 계속 커지니까 
    # c 로 나눠주면서 진행해야함
    
    if y == 1:
        # 마지막엔 결국 본인이 호출됨
        return x % c

    if y % 2 == 0:
        res = mul(x,y//2) ** 2
        return res % c 

    else:
        res = mul(x,y//2) ** 2
        return (x * res) % c

a,b,c = map(int,read().rstrip().split())
print(mul(a,b))
# print(cnt)