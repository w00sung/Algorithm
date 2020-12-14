import sys
sys.setrecursionlimit(10**8)
read =sys.stdin.readline

def get_medi(a,id1,id2,id3):
    if a[id2] < a[id1] : a[id2], a[id1] = a[id1],a[id2]
    if a[id3] < a[id2] : a[id3], a[id2] = a[id2],a[id3]
    if a[id2] < a[id1] : a[id2], a[id1] = a[id1],a[id2]
    return id2



# 피벗 (idx -> pl, pr)이 중요한 퀵 소트 #
def quick_sort(a, left : int, right : int):
    pl = left
    pr = right
    # x = a[(left+right)//2]


    # 피벗 선택하기 ##
    m = get_medi(a,pl,(pl+pr)//2,pr)
    x= a[m] # 가운데에 위치한 피벗

    a[m],a[pr-1] = a[pr-1],a[m]

    pl += 1
    pr -= 2
    #
    # pl이 pr에게 잡아먹히기 전까지 교환 계속!#
    

    while pl <= pr:
        # 피벗 보다 큰 놈 발견할 "때 까지", pl  +=1 #
        while a[pl] < x : pl += 1
        
        # 피벗 보다 작은 놈 발견할 때 까지, pr -= 1 #
        while a[pr] > x : pr -= 1

        # 같은 놈 만나도 멈춘다.
        

        # 피벗 값에서 멈춰 일치하는 경우 포함, 
        if pl <= pr:
            a[pl], a[pr] = a[pr], a[pl]
            # 선택된 자 다음부터 시작!
            pl += 1
            pr -= 1
    
    if left < pr : quick_sort(a,left = left, right = pr)
    if right > pl : quick_sort(a,left = pl, right = right)

n = int(read())
li = []
for _ in range(n):
    li.append(int(read()))
    
quick_sort(li,0,len(li)-1)

print("\n".join([str(k) for k in li]))

