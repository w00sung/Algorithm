############## dx, dy 리스트 (성공) ####################

import sys
read = sys.stdin.readline

# 사각형 각 꼭지점을 a,b,c,d
# a : 가로 상한, b : 세로 상한
a, b = map(int,read().rstrip().split())
n = int(read())

# 0을 넣은 이유는 dx가 첫 점이 될 수도 있다!
# 꼭지점을 넣어준것임!!!!!

x_list = [0, a]
y_list = [0, b]
# 기준 : 변의 중앙
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

print(x_list)
print(y_list)

dx_list = []
dy_list = []
for i in range(1,len(x_list)):
  dy_list.append(x_list[i]-x_list[i-1])
for j in range(1,len(y_list)):
    dx_list.append(y_list[j]-y_list[j-1])

print(dx_list, dy_list)
print(max(dy_list)* max(dx_list))
