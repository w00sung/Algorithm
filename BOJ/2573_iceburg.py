from collections import deque
import sys
sys.setrecursionlimit(10**6)
read= sys.stdin.readline


N, M = map(int,read().rstrip().split())
iceburg = []
xyqueue = deque()
for _ in range(N):
    iceburg.append(list(map(int,read().rstrip().split())))

visited = [[False] * M for _ in range(N)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]



# 빙산 조각들 세기
for i in range(1,N):
    for j in range(1,M):
        if iceburg[i][j] != 0:
            xyqueue.append((i,j))

# 숫자 줄이기
def after_year(x,y):
    

    cnt_0 = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue

        if iceburg[nx][ny] == 0:
            cnt_0 += 1
            


    # 빙산 높이 줄이기 
    # -- 같은 시간의 바로 옆 빙산도 널 0으로 본다.
    iceburg[x][y] -= cnt_0

    # 0 되면 끝내기
    if iceburg[x][y] <= 0:
        iceburg[x][y] = "G"

        return

    # 살아있으면 다시 넣어주기
    elif iceburg[x][y] >= 1:
        xyqueue.append((x,y))
        return



# 빙산 조각 세기 
# -- 다 돌면, 조각 수 += 1
def count_iceburg(x,y):

    # 방문지였으면, 나오기
    if visited[x][y]:
        return False
    # 방문지 아니었으면, 
    else:
        visited[x][y] = True

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            
            # 빙산이 있고, 방문안했으면, 들어가기
            if iceburg[nx][ny] != "G" and iceburg[nx][ny] >= 1 and visited[nx][ny] == False:
                count_iceburg(nx,ny)

        #조각 다 세고 돌아오면 True
        return True
    return False
# 조건 바꿔야됨
year = 0
piece = 0

while True:

    # 다 조각 2개되기 전에 0 되면,
    if not xyqueue:
        year = 0
        break

    visited = [[False] * M for _ in range(N)]
    # 살아있는 녀석들에 한해서 조각세기 시작
    piece = 0
    # 하루 조각세기
    for x,y in xyqueue:
        if count_iceburg(x,y):
            piece += 1
    
    if piece > 2:
        break
    
    cnt = 0
    len_xy = len(xyqueue)

    # 하루 녹는값 update
    while cnt < len_xy :

        x,y = xyqueue.popleft()
        after_year(x,y)
        cnt += 1

    # 숫자 update 후에 조각 세주기
    
    year += 1
    
print(year)