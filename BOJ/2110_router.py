import sys
read = sys.stdin.readline


## 설치 거리를 --- 촤소 설치 거리 !! 를 기준으로
# 다음 녀석이 나로부터 그만큼 거리가 떨어져 있냐?
# 거리를 이분 탐색

## --- 거리가 꼭 존재하는 거리가 아니어도 된다.

# count_router : 주어진 거리로 설치 대수 구하기 
def count_router(house,dist):
    strt = house[0]
    tot = 1
    for i in range(n):
        # 시작 + 거리 >= 다음 집 위치 --- 설치 (최소 거리 이상이니까!)
        if strt + dist <= house[i]:
            tot += 1
            # 기준 바꿔서 다음 설치 진행
            strt = house[i]

    return tot

house = []
n, cnt = map(int,read().rstrip().split())
for _ in range(n):
    house.append(int(read()))

house.sort()

# 최대, 최소 거리
mini = 1
maxi = house[n-1] - house[0]

res = 1

while mini <= maxi:

    # 거리
    dist = (mini + maxi) // 2
    
    # 설치 개수
    tot = count_router(house,dist)

    # 주어진 개수랑 일치하면 -- 일치하는데 더 큰 숫자 있을 수 있음!
                                ## 1 10 20 40  --- 그런 mid 중 최고 !
    
    # 개수가 더 적으면? -- 거리 좁혀야됨
    if tot < cnt :
        maxi = dist - 1


    # 개수가 더 많으면? -- 거리 넓혀야됨
    else:
        # ***초기 잘못된 생각 *** 같을 때는 거리 늘려주되, 정답 가능성있으니
                                                        #  res에 넣어줌
        # if tot == cnt:
        
        # ***** 같을 때만 넣어주면 안된다, 클 때도 정답일 때 있음 ****
        # ex ) 1 3 6 8 11 12  --- 정답 2임 
        # => 생각해보면 클 때 dist <= 똑같을 때
        res = max(res,dist)
        mini = dist + 1 


print(res)
