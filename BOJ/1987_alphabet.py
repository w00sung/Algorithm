import sys
sys.setrecursionlimit(10**5)
read = sys.stdin.readline

# n 행
n, m = map(int, read().rstrip().split())
graph = []

# 2차원 리스트 초기화 후에 & 리스트 넣기
for i in range(n):
    graph.append(list(read().rstrip()))


# 다녀온 알파벳 조회
visited = []

# return을 언제 해주는 것이 best 인가?
def dfs(graph,x,y,visited,cnt):

    # 벗어났다.
    if x < 0 or y < 0 or x >= n or y >= m :
        return cnt
    
    # 내가 방문했던 녀석이면
    now = graph[x][y]
    if now in visited:
        return cnt
        
    # 왔던 알파벳이 아니면,
    elif now not in visited:
        visited.append(now)
        a = dfs(graph,x-1,y,visited,cnt+1)
        b = dfs(graph,x+1,y,visited,cnt+1)
        c = dfs(graph,x,y-1,visited,cnt+1)
        d = dfs(graph,x,y+1,visited,cnt+1)
        visited.pop()
        
        return(max(a,b,c,d))
    # 들어갔는데 갇혔으면

print(dfs(graph,0,0,visited,0))

