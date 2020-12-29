import sys
read = sys.stdin.readline


N, M  = map(int, read().rstrip().split())

li = [i for i in range(N+1)]

visited = [False] * (N+1)
ans = []
def combi(depth):

    # M단계가 끝나고 다음 단계로 오면 출력
    if depth == M+1:
        print(*ans)

    else:
        # 단계별 반복문을 사용하여 백트래킹
        for i in range(1,N+1):
            # 방문하지 않은 녀석들에 한해서
            if visited[i]:
                continue
            
            # 답을 넣어준다.
            ans.append(li[i])
            visited[i] = True

            # 단계가 완료될 때 가지 진행
            combi(depth+1)
            ans.pop()
            visited[i] = False

# 시작을 1단계로 가정하고 진행
combi(1)