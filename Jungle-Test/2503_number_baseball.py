import sys
read = sys.stdin.readline

n = int(read())
game = []

# 입력하면서 조건에 맞는 숫자들 True 만들기

for _ in range(n):
    game = list((map(int,read().rstrip().split())))

    # 00 01 02 03 10 11 12 20 21 30 

    # 같은 숫자 & 같은 위치 -- True

    # 더 열심히 해야겠다....
    if game[1] >= 1:


      if game[2] >= 1:

