import sys
read = sys.stdin.readline


n = int(read())
# n+1개 만들자 -- 0번째 비어있고, 1번째는 무조건 빈 것 유지

graph =[[] for _ in range(n+1)]
tree = [[] for _ in range(n+1)]
visited = [False] * (n+1)

# 연결관계 만들어 놓고, 1부터 깊숙히 들어가자
for _ in range(n-1):
    a, b = map(int,read().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)    
    

# 깊숙하게 들어가면서, 부모관계 정리
def dfs(graph,node):

    visited[node] = True

    for point in graph[node]:
        if visited[point] == False:
            # 부모관계 삽입
            tree[point].append(node)
            # 이제 너도 들어가라~
            dfs(graph,point)


dfs(graph,1)
for i in range(2,n+1):
    print(*tree[i])