import sys
from collections import deque
# import heapq

read = sys.stdin.readline


# 바이러스 정보, 힙에 담을 것이다.
# 힙에 넣어주면 append 된 것이 1일 경우 그놈을 바로 빼낸다.
virus_queue = deque()
virus_map = []
N, K = map(int, read().rstrip().split())

for _ in range(N):
    virus_map.append(list(map(int, read().rstrip().split())))

seconds, find_x, find_y = map(int, read().rstrip().split())


# 힙에 넣어준다.
for i in range(N):
    for j in range(N):
        if virus_map[i][j] > 0:
            # heapq.heappush(virus_heap,(virus_map[i][j],i,j))
            virus_queue.append((virus_map[i][j], i, j))


def infection(x, y):

    for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
        nx = x + dx
        ny = y + dy

        # 벽 만나면 다음!
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue

        # 전염 시킨 녀석 다시 넣을 필요없다.
        # 전염 시켰으면, 저장해준다.
        if virus_map[nx][ny] == 0:
            virus_map[nx][ny] = virus_map[x][y]
            # heapq.heappush(virus_heap,(virus_map[nx][ny],nx,ny))
            virus_queue.append((virus_map[nx][ny], nx, ny))


sec = 0
while True:
    if sec == seconds:
        break

    len_queue = len(virus_queue)
    virus_queue = deque(sorted(virus_queue))

    # 1초 지남
    while len_queue > 0:

        # coor = heapq.heappop(virus_heap)
        coor = virus_queue.popleft()
        x, y = coor[1], coor[2]
        len_queue -= 1
        infection(x, y)

    # 오늘의 할당량
    # 오늘의 할당량 끝났으면 1초 없그레이드
    sec += 1

print(virus_map[find_x-1][find_y-1])
