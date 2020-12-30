from collections import deque
import sys
read = sys.stdin.readline

N = int(read())
shark_queue = deque()
fish_queue = deque()
fish_exist = [[False] * N for _ in range(N)]
graph = []

for i in range(N):
    graph.append(list(map(int,read().rstrip().split())))

# 처음 shark 위치와 생선 위치 찾기
for i in range(N):
    for j in range(N):
        if graph[i][j] > 0:

            if graph[i][j] == 9:
                shark_queue.append((i,j))
                continue
            # 물고기 크기 & 위치 정보 삽입
            fish_queue.append((graph[i][j],i,j))
            fish_exist[i][j] = True


 # 먹을 수 있는 물고기 찾기

 # 크기 , x, y 순으로 정렬하면됨
 # fish_queue = sorted(fish_queue, key = lambda x: x[0],x[1],x[2])
 
 # 크기 커질 때마다 찾아야 함! -- 없으면 종료
# def find_eatable_fish(size):
#     eatable_fish = []
#     for i in range(len(fish_queue)):
#         if fish_queue[i][0] < size and fish_exist[fish_queue[i][1]][fish_queue[i][2]]:
#             # 작은 녀석이면 뽑는다.
#             eatable_fish.append(fish_queue[i])

#     return eatable_fish

# 먹을 수 있는 것들 모두까지 거리 (BFS)
# 여러개 있으면, 최소 모음집 + 상단 좌측 부터

def move_until_fish(size,x,y):
    shark = deque([(x,y)])
    fish = []
    # visited 초기화
    visited = [[False] * N for _ in range(N)]
    visited[x][y] = True
    # 위, 좌측 순으로 정렬된 생선들

    dist = 0
    while True:
        
        # 같은 거리에 있는 물고기 내뱉기
        if len(fish) > 0:
            # 1) 상단 2) 좌측
            fish = sorted(fish, key = lambda x : (x[0],x[1]))
            return fish[0], dist
    
        len_shark = len(shark)

        while len_shark > 0:
            shark_x, shark_y = shark.popleft()
            # 내가 왔다 !
            graph[shark_x][shark_y] = 0
            len_shark -= 1
            
            for dx, dy in (1,0), (-1,0), (0,-1), (0,1):
                nx = shark_x + dx
                ny = shark_y + dy

                if nx < 0 or nx >= N or ny < 0 or ny >= N:
                    continue

                if graph[nx][ny] > size or visited[nx][ny]:
                    continue
                
                # size 같으면 움직일 수 있음
                # 나 자신도 움직일 수 있다 ..!!!! 9 도 추가해주어야함 + 
                # !!!! size 작은데, 이미 먹은 곳도 내가 방문할 수 있따!!
                if (graph[nx][ny] == size or graph[nx][ny] == 0):
                    shark.append((nx,ny))
                    visited[nx][ny] = True
                    continue

                # 물고기 먹을 수 있다.
                # -- 지금 작은거 먹으러 가는거임

                # 물고기 먹을 수 있는 것
                if graph[nx][ny] < size and fish_exist[nx][ny]:
                    fish.append((nx,ny))
                    # 같은 물고기 안잡아먹게
                    visited[nx][ny] = True 
                    continue
        dist += 1

# 여행 시작
size = 2
tot_dist = 0

x, y = shark_queue.popleft()

while True:
    
    size_eatable_fish = 0
    # 내 사이즈 기준 먹을 수 있는 물고기
    for fish in fish_queue:
        if fish[0] < size and fish_exist[fish[1]][fish[2]]:
            size_eatable_fish += 1
    # 내 크기에서 더이상 먹을 것이 없으면 멈추기
    # if size_eatable_fish == 0:
    #     break
    

    # 먹다가 중간에 다시 나올 수도 있다.
    for _ in range(size):

        # 내 사이즈에서 먹을 것 더이상 없으면, out!
        if size_eatable_fish == 0:
            print(tot_dist)
            exit()
        
        fish, dist = move_until_fish(size,x,y)
        # 하나 먹었다.
        size_eatable_fish -= 1
        
        # 생선 지우기
        # 먹고 나온 좌표가 이제 다시 들어갈 좌표다.
        x , y = fish[0], fish[1]
        # fish_exist[x][y] = False
        # shark_queue.append((x,y))
        tot_dist += dist

    # 내 사이즈 만큼 먹고 나오면, 사이즈 커짐
    size += 1