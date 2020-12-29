import sys
read = sys.stdin.readline

N, M = map(int,read().rstrip().split())
li = [i for i in range(N+1)]
visited = [False] * (N+1)
ans = []
# 사용된 idx
use = []

# 
def dfs(depth,frm):

    if depth == M+1:
        print(*ans)


    else:


        for i in range(frm,N+1):
            if visited[i]:
                continue


            visited[i] = True
            ans.append(li[i])

            # 현재의 나보다 큰 값을 넘겨준다 !!!!!!!!
            # 2로 dfs를 들어가면, range는 2부터 받는다.

            
            # frm이 아니라 i 다.
            # 지금의 나보다 큰값으로 range를 돌린다.
            dfs(depth + 1 ,  i + 1)
            visited[i] = False
            ans.pop()

            # 올라갈때는 false로 바뀌어야 하고,
            # 옆으로 갈때는 true가 유지되여야 한다.
            # for 문이 다돌면, 사용된 것들 true 로 바꿔주자.

            # if depth != 1:
            #     visited[i] = False

dfs(1,1)