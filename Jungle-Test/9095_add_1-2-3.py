import sys
read = sys.stdin.readline

k = int(read())
cnt = 0
# i : 시작 노드
def dfs(tot):
    global cnt

    # 전단계 돌아와서 다음 1,2,3 살펴보고 크면 return
    # 줄일 수 있을 것 같은데.....ㅠㅠ --> 전전단계로 가기
    if tot > n:
        return

    if (tot == n):
        cnt += 1
        return

    
    else:
        # 1,2,3 반복해야됨
        for j in range(1,4):
            dfs(j+tot)
        return

for _ in range(k):
    n = int(read())
    dfs(0)
    print(cnt)
    cnt = 0