from collections import deque
import sys
read = sys.stdin.readline


n_city, n_road, dist, strt = map(int,read().rstrip().split())

# 도시이름, idx 맞춰주기
city = [[] * (n_city+1) for _ in range(n_city+1)]
# visitied = [False] * (n_city+1)
for _ in range(n_road):
    frm, to = map(int,read().rstrip().split())
    city[frm].append(to)

visited = [-1] * (n_city+1)

# bfs 로 2가 퍼진 것들 return 하자
# 2가 최소거리인 도시
def bfs(city,strt,visited):
    brk = True
    queue = deque([strt])
    visited[strt] += 1

    while queue:

        
        strt = queue.popleft()
        # 연결된 것들 본인보다 +1씩 해주기
        for i in city[strt]:
            # 갈 수 있는 도시 막아놨음
            if visited[i] == -1:
                # 큐에 넣어주고,
                queue.append(i)
                # 방문값 올려주기
                visited[i] = visited[strt] + 1

    # 어차피 O(N) 형태임
    for i in range(1,n_city+1):
        if visited[i] == dist:
            print(i)
            brk = False
    if brk:
        print(-1)

    # 뭔 차이지...?
    #         if visited[i] == dist:
    #             print(i)
    #             brk = True

    #     if brk == True:               
    #         return
    # if brk == False:
    #     print(-1)
    #     return

bfs(city,strt,visited)





# 2로 갈 수 있는 도시
# def dfs(city,strt,visited,cnt):

#     if cnt ==2:
#         print(strt)
#         return
#     # 방문처리
#     visited[strt] = True
    
#     # 연결된 녀석들 다 돌아본다.
#     for nxt in city[strt]:
#         if visited[nxt] == False:
#             cnt += 1
#             dfs(city,nxt,visited,cnt)
#             cnt -= 1

# dfs(city,strt,visited,0)