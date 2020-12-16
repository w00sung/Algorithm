import sys
sys.setrecursionlimit(10**8)
read = sys.stdin.readline

n = int(read())
cost_arr = []
for _ in range(n):
    cost_arr.append(list(map(int,read().rstrip().split())))

# list는 global 선언 불필요
visited = [0] * n


# 인자로 넣으면 ---- 메모리
# global -- 시간
# strt : ,
# now  : 지금 내가 있는 섬 (자주 바뀌는 것)
# tot : 자주 변경 된다.  (다음 함수에 던져줄 수 있는, 변할 수 있는)
minCost = float('inf')

def dfs(strt, now, tot, depth):
    # global visitied
    global minCost
    # 종료 조건
    if depth == n:
        if cost_arr[now][strt] != 0 :
            minCost = min(minCost, tot+cost_arr[now][strt])

        return



    # i가 내가 방문할 섬
    for i in range(n):
        # 내가 갈 곳 !0, 방문 x
        if cost_arr[now][i] != 0 and visited[i] == 0:
            visited[i] = 1
            # tot의 변화, depth는 늘려주고 끝나면 다시 돌아옴(== 인자로 써야함)
            dfs(strt, i, tot+cost_arr[now][i], depth + 1)
            # 빠져 나오는 시점에서 0으로 안왔다는
            visited[i] = 0

visited[0] = 1
# 0,0 에서 출발해서 1,0 2,0 3,0 ---

# 0에서 시작하나, 
# 1에서 시작하나, 
# 2에서 시작하나 모두 똑같다!!!!!!!!!
dfs(0,0,0,1)
# visited[i] = 0

print(minCost)