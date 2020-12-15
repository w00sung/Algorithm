import sys
read = sys.stdin.readline

n = int(read())
# pos [i] : i열에 배치한 행!


# cf) 아래 코드에서는 1행이 시작이다.  not 0
# 현재 col에서 i행 유망한가 ? == 들어갈만한가?
def promising (i,col):
    # k는 1행부터 살펴 볼거야 초기화 == 첫 행의 값은 1부터 끝까지 다 넣어 줄거야.
    k = 1
    # return 할 값
    flag = True
    # i == 0,1 일때는 그냥 True 임, 들어가!! == 첫 행의 값은 1부터 끝까지 다 넣어 줄거야.
    # 계속 돌면서
    while (k < i and flag):
        # 1행부터 i행 까지 놓은 것 중에 -- 같은 열 있냐?! or 대각선에 있는 거 있냐?!  
        if (col[i] == col[k]) or (abs(col[i]-col[k]) == i-k):
            flag = False
       
        k += 1


    return flag

cnt = 0
# i : depth, col : i번째 depth / 현재까지 col
# col : 각 행마다 배치된 열!
def n_queens(i, col):

    global cnt
    # *** promising? 
    # 지금 행 값을 넣었는데, 유망한가?!(조건에 만족하냐?) -- 들어갈래 말래
    # i가 두번째 부터는 바꾸고 검증이다.
    if (promising(i,col)):
        
        # 유망한데,
        # depth 만큼 갔으면! 출력해
        if (i == n):
            # 이동 경로 출력해
            # 초기 행 1이었다.
            # print(col[1: n+1])
            ## 여기까지 와야 카운트 됨, 아니면 그냥 끝남 !!
            cnt += 1
        
        # 유망한데,
        # 아직 안갔으면, 트리 계속 옆으로 한칸 이동해놓고 들어가봐!
        else:
            # 다시 돌아오면, 값 다시 넣어줄거야.
            for j in range(1,n+1):
                col[i+1] = j
                # 더 깊숙이 있는 친구 +1 하면서 돌려주고, 찍어주기!
                n_queens(i+1, col)


col = [0] * (n+1)
n_queens(0,col)
print(cnt)
# print(promising(1,col))
