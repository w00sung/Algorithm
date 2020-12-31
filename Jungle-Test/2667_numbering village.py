import sys
read = sys.stdin.readline

N = int(read())
graph = []
for _ in range(N):
    graph.append(list(map(int,read().rstrip())))
visited = [[False] * N for _ in range(N)]




def dfs(x,y):
    global cnt
    suc = True
    # 상,하,좌,우
    for dx,dy in (-1,0),(1,0),(0,-1),(0,1):

        nx = x + dx
        ny = y + dy

        #벽을 만날경우
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            
            continue
        
        # 들어가면서 1개씩 업데이트
        if graph[nx][ny] == 1:
            if visited[nx][ny] == False:
                visited[nx][ny] = True
                cnt += 1
                dfs(nx,ny)
                # nx, ny 다음에도 와야돼!!

    return suc

        # return True
            
            # dfs는 True를 내뱉는다. -- True 개수로 단지수 셀거임

# town : 단지수
town = 0
# 집의 수
# piece = -1
ans = []

for row in range(N):
    for col in range(N):
        if graph[row][col] == 1 and visited[row][col] == False:
            cnt = 1
            house = -1
            ## DFS는 들어가기 전에 방문처리가 정말 정말 중요합니다 ****
            # 안그러면, 바로 옆에 녀석이 나한테 들어와요 ***
            # 들어가기 전에 방문처리 !!!!!!
            visited[row][col] = True
            if dfs(row,col):
                house = max(house,cnt)
                town += 1
                ans.append(house)

print(town)
ans.sort()
for i in range(len(ans)):
    print(ans[i])