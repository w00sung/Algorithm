
# n : node 개수
N = 9
visited = [False] * 9
# 재귀함수로 구현한다.
# visited로 왔는지 확인한다.
def dfs(graph,node,visited):

    # 방문처리
    visited[node] = True
    # 방문 동시에 출력
    print(node, end = " ")

    # graph[node] : node에 연결된 리스트
    # 내가 연결된 node에 다 들어가볼거야.
    for n in graph[node]:
        # 그 중에서도 내가 안들어 가본 녀석들에 한해서
        if visited[n] == False:
            dfs(graph,n,visited)

graph = [ [], [2,3,8], [1,7],
[1,4,5],[3,5],[3,4],[7],[2,6,8],[1,7]]


dfs(graph,1,visited)