############### 꼭지점 초기화 할 때, 상한만 넣어줌 ##################

import sys
read = sys.stdin.readline

# 사각형 각 꼭지점을 a,b,c,d

a, b = map(int,read().rstrip().split())
n = int(read())

## Fail Block ##
x_list = [a]
y_list = [b]
for _ in range(n):
  # info : 정보, loc : 위치
  info, loc = map(int,read().rstrip().split())
  # 기준 정보

  # 가로 자르기
  if info == 0:
    y_list.append(loc)
  else:
    x_list.append(loc)

y_list.sort()
x_list.sort()

dx_list = []
dy_list = []
for i in range(1,len(x_list)):
  dy_list.append(x_list[i]-x_list[i-1])
  for j in range(1,len(y_list)):
    dx_list.append(y_list[j]-y_list[j-1])

print(max(dy_list)* max(dx_list))