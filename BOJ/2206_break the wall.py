from collections import deque
import sys

read = sys.stdin.readline
ROW, COL = map(int,read().rstrip().split())

graph = []

for _ in range(ROW):
    graph.append(list(map(int,read().rstrip())))

visited = [[False] * COL for _ in range(ROW)]
visited_break = [[False] * COL for _ in range(ROW)]

# Q > 벽을 뚫고 같은자리에 도착한 녀석이 더 늦게 도착할 수 있나?

# x,y : 0,0 && brk : 0
def move(x,y):
    xyqueue = deque([(x,y,0,1)])
    visited[x][y] = True
    ans = float('inf')
    suc = False
    while xyqueue:
        x,y,brk,cnt = xyqueue.popleft()
        # BFS 는 같은 레벨 단위로 움직인다.
        # 늦게 들어온 녀석은 늦게 도착한 녀석임

        if (x,y) == (ROW-1, COL-1):
            ans = min(ans,cnt)
            suc = True
            continue

        for dx, dy in (-1,0), (1,0), (0,1), (0,-1):
            nx = x + dx
            ny = y + dy
            

            if nx < 0 or nx >= ROW or ny < 0 or ny >=COL:
                continue
            
            if visited[nx][ny]:
                continue
            
            # 벽뚫기
            if graph[nx][ny] == 1:

                # 이전에 이 벽을 누가 먼저 뚫어봤으면, 안들어감
                if brk == 0 and visited_break[nx][ny] == False:
                    xyqueue.append((nx,ny,brk+1,cnt+1))
                    # 넣을 때, 방문 처리 해줘야 
                    # 다음에 넣는애가 안넣음

                    # 벽을 뚫고 온거면, 다음녀석이 와도 됨.
                    visited_break[nx][ny] = True


                # 벽을 부셔봤으면 pass
                # 이때, if를 병렬적으로 두자!
                if brk == 1:
                    continue
            
            # 이동하기
            if graph[nx][ny] == 0:
                # cnt += 1
                # 값을 변경해주면 다음 nx,ny에도 영향을 끼친다.

                # 한번도 안온 놈이 왔을 때에만, True
                if brk ==0 :
                    visited[nx][ny] = True
                    xyqueue.append((nx,ny,brk,cnt+1))
                
                # 벽을 뚫었던 녀석인데, 같은 곳을 오게 할 순 없다.
                elif brk ==1 and visited_break[nx][ny] == False:
                    visited_break[nx][ny] = True
                    xyqueue.append((nx,ny,brk,cnt+1))

    if suc:
        return ans
    else:
        return -1

print(move(0,0))  