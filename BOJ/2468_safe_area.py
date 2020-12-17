import sys
sys.setrecursionlimit(10**8)
read = sys.stdin.readline

n = int(read())
area = []
# 방문

# min_area = 1
max_height = 0

for i in range(n):
    area.append(list(map(int,read().split())))
    # 최대 높이
    max_height = max(max_height, max(area[i]))

# print(area)
# print(max_height)
# # 위, 아래, 좌, 우에 강우량 이하가 있냐?
# # 계속 변화할 것들을 매개 인자로 받자.
# # 내 현재 위치를 x,y
# n : 강수 높이

def dfs(h,x,y):
    global n

    # 종료조건 // 양 끝이 막혀있거나, 평균 이하를 만나면 stop
    if x < 0 or x >= n or y < 0 or y >= n:
        # cnt += 1
        return False
    
    height = area[x][y]

    # 평균 이하를 만나면 or 왔었으면 return
    if height <= h or visited[x][y] == 1:

        return False

    # 현재 강수 높이보다 높을 경우 진행
    else:
        # 다시 지나가지 못하게
        visited[x][y] = 1
        # 아래로 보내보기
        dfs(h,x+1,y)
        # 우측으로 보내보기
        dfs(h,x,y+1)
        # 위로 보내보기
        dfs(h,x-1,y)
        # 좌로 보내보기
        dfs(h,x,y-1)


        return True

cnt = 0
# i_cnt = 1
# 조각수 2되면 stop ---  1, max-1 일 때, 조각수 1 
for i in range(0,max_height+1):
    # 수면 올릴 때마다 초기화
    i_cnt = 0
    visited = [[0] * n for i in range(n)]
    # 이미 간 것은 안가게 할 수도 있다.
    for j in range(n):
        for k in range(n):
            if(dfs(i,j,k)):
                i_cnt += 1

    cnt = max(cnt, i_cnt)

print(cnt)