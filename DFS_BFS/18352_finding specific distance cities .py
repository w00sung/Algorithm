from collections import deque
import sys
read = sys.stdin.readline

N_city, N_road, dist, strt = map(int,read().rstrip().split())
graph = [[] for _ in range(N_city + 1)]
for _ in range(N_road):
    frm, to = map(int,read().rstrip().split())
    graph[frm].append(to)

visited = [False] * (N_city + 1)
queue = deque()

ans = []


# BFS는 최단거리 찾는다!
def find_bfs(strt,dist):
    # 성공 여부 ( == 거리 같은 놈 있냐 없냐 )
    suc = False

    # 현재 거리
    now_dist = -1

    # 시작점에 출발지를 넣어준다.
    queue = deque([strt])
    visited[strt] = True

    while True:
        # 현재 거리를 할 수 있는 척도
        len_queue = len(queue)
        now_dist += 1

        # 현재거리가 목표거리보다 높으면 끝낸다.
        if now_dist > dist:
            break
        
        # 현재 레벨의 할당량 len_queue
        while len_queue > 0:
            now = queue.popleft()
            len_queue -= 1
            
            if now_dist == dist:
                ans.append(now)
                suc = True
                continue
            
            # 나와 붙어있는 녀석들 큐에 넣어주기
            for to in graph[now]:
                if visited[to] == False:
                    queue.append(to)
                    # 넣어주면서 방문처리,
                    # 앞전에 방문했으면 넣지 않는다.
                    visited[to] = True
    return suc

if find_bfs(strt,dist) :
    # 오름차순 !!!
    ans.sort()
    for i in range(len(ans)):
        print(ans[i])
else:
    print(-1)