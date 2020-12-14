
def bubble_sort(a):
    ''' 버블 정렬 '''
    n = len(a)
    # 끝에서 부터 작은 놈을 앞으로 한칸 민다
    # 한번의 패스가 지나면 남은 놈들부터 진행
    for i in range(n):
        for j in range(n,i,-1):
            if a[j] > a[j-1]:
                a[j-1] , a[j] = a[j], a[j-1]

def bubble_sort_up1(a):
    ''' 버블 정렬 시, 중간에 정렬이 완료된 경우 '''
    '''              = 중간에 패스 횟수 0 인 경우 '''
    n = len(a)
    # 끝에서 부터 작은 놈을 앞으로 한칸 민다
    # 한번의 패스가 지나면 남은 놈들부터 진행
    for i in range(n):
        pass = 0
        for j in range(n,i,-1):
            if a[j] > a[j-1]:
                a[j-1] , a[j] = a[j], a[j-1]
                pass += 1
        if pass == 0 :
            break

def bubble_sort_up2(a): # ---- for문으로 불가
    n = len(a)
    # 끝에서 부터 작은 놈을 앞으로 한칸 민다
    # 한번의 패스가 지나면 남은 놈들부터 진행
    for i in range(n):
        for j in range(n,i,-1):
            if a[j] > a[j-1]:
                a[j-1] , a[j] = a[j], a[j-1]
                last = j
            i = j
            # i = j 먹지 않는다 ! ---- while 문으로 변환

def bubble_sort_up2_while(a):
    n = len(a)
    i = 0
    # i == n-1 -- n-1 이 last가(인덱스 끝) 되면 정렬 완료 !
    while i < n-1:
        last = i
        for j in range(n,last):
            if a[j] > a[j-1]:
                # pass 가 일어나면 last 변경
                a[j-1], a[j] = a[j], a[j-1]
                last = j
        i = last


def shaker_sort(a):
    ''' 버블 정렬 쌍방으로 달리기 '''
    # left : 좌측 출발, right : 우측 출발
    left = 0
    right = len(a) - 1
    # 출발 지점이 엇갈리는 순간 끝!
    last = left
    while left > right:
        # right 출발
        for i in range(right, left, -1):
            if a[i-1] < a[i]:
                a[i-1],a[i] = a[i],a[i-1]
                last = i
        # last 부터 제일 큰 것 오른쪽으로 밀어라!
        left = last
            
        for j in range(left, right, 1):
            if a[j] > a[j+1]:
                a[j-1], a[j] = a[j], a[j-1]
                last = j
        # last 부터 제일 작은 것 왼쪽으로 밀어라 !
        right = last



        # left 출발




