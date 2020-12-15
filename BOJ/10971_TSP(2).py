import sys
read = sys.stdin.readline

n = int(read())
cost = []
for _ in range(n):
    cost.append(list(map(int,read().rstrip().split())))

path = [-1] * (n+1)
path_li = []
def promising(i,path):
    k = 1
    flag = True
    # 어디까지 살펴볼꺼야?
    # flag false 되면 나올거다.

    # 1에는 모든 값 다 넣을 수 있음
    # i 2부터 while문 들어갈 수 있음!
    while k < i and flag:
        # 왔다간 적 있니?
        print ("path[k] : {} vs path[i] : {} ".format(path[k],path[i]))
        if (path[k] == path[i]) or cost[path[i-1]][path[i]] == 0:
            flag = False

        k += 1 

    return flag


# i는 i번째 도시 #path[i] : i번째 접근 도시
def TSP_cost(i,path):

    # 더 갈 수 있나?
    if(promising(i,path)):
        
        # 들어왔고
        # depth 만큼 들어왔으면
        if i == n:
            print("순회!")
            # 끝에 본인의 위치 넣어야함

            # path list 들에 넣어주기
            path_li.append(path)

            path = [-1] * (n+1)

            # path_li.append(path)
            # # 여기서 가격 계산
            # for i in range(1,n+2):
            #     sum += cost[path[i]][path[i+1]]
            # print("가격 총합 : sum")
            
        else:
            # j 행을 바꿔준다.
            for j in range(n):
                # cost[i][j] != 0 : 경로가 연결되어 있어야 넘어감
                print("현재 j : ",j)
                print(cost[j][i])
                path[i+1] = j
                print(path)
                # 다음 행으로 넘긴다., 돌아오면 다시 path에 덧쓴다.
                TSP_cost(i+1,path)



TSP_cost(0,path)




# 도시 간 순서
# 1부터 넣을 거임
idx = [False] * (n+1)