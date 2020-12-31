from collections import deque


N = 9
visited = [False] * N
# node를 돌면서, 해당 노드에 연결된 것, 
# 모두 queue에 넣어줄것임
def bfs(graph,node,visited):

    # 네기 지나온 위치를 큐에 담는다.
    queue = deque([node])
    visited[node] = True

    # 나와 연결된 것들을 "큐"에 다 담는다.
    # 큐에 넣었던 것들을 빼면서, 
    # 내가 방문할 수 있는 것에 방문해감
    while queue:
        # 가장 좌측을 뺴주면서 주가 되는 node값 갱신
        v = queue.popleft()
        print(v, end = " ")

        for i in graph[v]:
            if visited[i] == False:
                # 일단 넣는다.
                # 방문처리를 동시에 진행한다
                queue.append(i)
                visited[i] = True    

graph = [ [], [2,3,8], [1,7],
[1,4,5],[3,5],[3,4],[7],[2,6,8],[1,7]]

bfs(graph,1,visited)