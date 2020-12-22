from collections import deque
import sys
read = sys.stdin.readline

snake = deque()
apple_li = []
dir_li = deque()
x,y = 1,1
nx_li = [0,1,0,-1]
ny_li = [1,0,-1,0]


n = int(read())
n_apple = int(read())
for _ in range(n_apple):
    # 사과 좌표 리스트 - 튜플로 받기
    apple_li.append(tuple(map(int,read().rstrip().split())))

# 방향 전환
n_dir = int(read())
for _ in range(n_dir):
    # 문자열도 있으니, int 화 하지 않는다.
    dir_li.append(list(read().rstrip().split()))

time = 0
# i : 방향 idx
i = 0
snake.append((x,y))
while True:

    # 진행 방향 설정 // 
    # dir_li 가 없어도 무리없이 진행되어야함 -- 조건에 dir_li 넣어준다.
    if dir_li and time == int(dir_li[0][0]):
        dirc = dir_li.popleft()
        if dirc[1] == "D":
            i += 1

        elif dirc[1] == "L":
            i -= 1
    
    # 다음 좌표
    nx = x + nx_li[i%4]
    ny = y + ny_li[i%4]
    time += 1
    

    # 다음에 뱀을 만나거나 // 벽을 만나면 중단
    # append 시키고 검증하면 당연히 break 하지
    if (nx,ny) in snake or (nx > n or nx < 1 or ny > n or ny < 1):
        break

    snake.append((nx,ny))
    x = nx
    y = ny
    # 현재 내가 사과 있는 곳에 있으면 다음으로
    # apple 먹으면 없애줘야함 !!!
    if (nx,ny) in apple_li:
        apple_li.remove((nx,ny))
        continue

    # 내 위치에 사과 없으면 꼬리좌표 빼주기
    else:
        snake.popleft()
    

print(time)