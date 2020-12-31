from collections import deque


# 1이라고 되어있는 값을 전의 값 + 1

# (nx,ny) : 순서대로 우측, 아래측 
    
def bfs(graph,x,y,visitied):
    
    # 상,하,좌,우 ---> 우,하 막혀있으면 어떻게든 가야함
    dx = [-1,1,0,0]
    dy = [0,0,-1,1] 

    # 초기 좌표 넣어준다.
    # 좌표를 넣고, 빼줄거야.

    queue = deque((x,y))
    # 좌표(큐)가 다 빠질때까지(BFS) 진행
    while queue:
        # 현재 위치는 덱에서 빼온다.
        x,y = queue.popleft()
        # 내가 갈 수 있는 곳은 모두 큐에 담는다.
        # 담으면서, 그래프에 값 1 씩 더해감
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 해당지점을 갈 수 있는지 검정
            # 범위 넘으면 안간다.
            if nx < 0 or nx >= n or ny < 0 or ny >=n:
                continue
            
            # 벽은 안간다. 안해준다.
            if graph[nx][ny] == 0:
                continue


            # 내가 갈 곳이 처음 가는 곳(값 : 1)에만 적용
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((x,y))

    return graph[n-1][m-1]

