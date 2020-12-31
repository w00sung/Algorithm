from collections import deque
import sys
read = sys.stdin.readline

graph = []
ROW , COL = map(int,read().rstrip().split())

for i in range(ROW):
    graph.append(list(map(int,read().rstrip().split())))
    # count_0 = graph.count(0)

virus_queue = deque()
pos_queue = deque()
# 바이러스 위치 찾기,

origin_graph = graph.copy()

for i in range(ROW):
    for j in range(COL):
        if graph[i][j] == 0:
            pos_queue.append((i,j))
        


# visited = [[False] * COL for _ in range(ROW)]
ans = 0
def make_wall(wall,ROW,COL):
    # 벽 3개 세워지면, 바이러스 퍼뜨리고 count한다.
    # 모든 위치에 대해서 해줘야함.

    # for x1,y1 in pos_queue:
    #     for x2,y2 in pos_queue:
    #         for x3,y3 in pos_queue:
    #             if (x1,y1) != (x2,y2) and (x1,y1) != (x3,y3) and (x2,y2) != (x3,y3):
    #                 # 0인 것들에 벽 세워주고
    #                 graph[x1][y1] = 1
    #                 graph[x2][y2] = 1
    #                 graph[x3][y3] = 1
                    # # 바이러스 퍼뜨린다.
                    # visited = [[False] * COL for _ in range(ROW)]

                    # pos_count = virus(visited,ROW,COL)

                    # ans = max(ans,pos_count)
                    # # 다시 원상복귀
                    # graph[x1][y1] = 0
                    # graph[x2][y2] = 0
                    # graph[x3][y3] = 0

 
    global ans
    # 3개 되면 센다

    # 멋진 skill 이다!!!!
    if wall == 3:
        visited = [[False] * COL for _ in range(ROW)]
        pos_count = virus(visited,ROW,COL)
        ans = max(ans, pos_count)
        # return을 해주어야한다 !
        return
        
    # 세 점 움직여서 벽 세우기
    for i in range(ROW):
        for j in range(COL):
            if graph[i][j] == 0:
                graph[i][j] = 1
                make_wall(wall+1,ROW,COL)
                graph[i][j] = 0

    return ans
                        
                        


# 0 제거 한 것 세주기
def virus(visited,ROW,COL):
    # 벽 세워졌음
    for i in range(ROW):
        for j in range(COL):
            if graph[i][j] == 2:
                virus_queue.append((i,j))
        
    pos_count = len(pos_queue) - 3
    while virus_queue:
        
        x,y = virus_queue.popleft()

        for dx, dy in (-1,0), (1,0) , (0,-1), (0,1):

            nx = x + dx
            ny = y + dy

            if nx < 0 or nx >= ROW or ny < 0 or ny >= COL:
                continue

            if graph[nx][ny] == 1:
                continue

            if graph[nx][ny] == 0 and visited[nx][ny] == False:
                graph[nx][ny] = 2
                visited[nx][ny] = True
                pos_count -= 1
                virus_queue.append((nx,ny))
                graph[nx][ny] = 0

    # graph.copy(origin_graph)
    return pos_count

ans = make_wall(0,ROW,COL)
print(ans)