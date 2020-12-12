################# 상한, 하한 ####################

import sys
read = sys.stdin.readline

# 사각형 각 꼭지점을 a,b,c,d
# a : 가로 상한, b : 세로 상한
a, b = map(int,read().rstrip().split())
# c : 가로 하한, d: 세로 하한
c, d = 0, 0
n = int(read())

# 기준 : 변의 중앙
mx, my = 0, 0
for _ in range(n):
  # info : 정보, loc : 위치
  info, loc = map(int,read().rstrip().split())
  # 기준 정보 mx : 가로, my : 세로
  mx = (a+c)/2
  my = (b+d)/2

  # 가로
  if info == 0:
    if loc >= my:
      b = min(b,loc)

    else:
      d = max(d,loc)

  # 가로 정보
  else:
    # 상한
    if loc >= mx:
      a = min(a,loc)

    else:
      c = max(c,loc)
  print

print((a-c)*(b-d))
