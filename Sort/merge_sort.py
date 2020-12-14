import sys
sys.setrecursionlimit(10**8)
read =sys.stdin.readline


def merge_sorted_list(a,b,c):
    na,nb,nc = len(a),len(b),len(c)

    # 끌고 갈 인덱스
    pa,pb,pc = 0,0,0

    # 둘 중 작은 값을 먼저 넣기
    while pa < na and pb < nb:
        if a[pa] <= b[pb]:
            c[pc] = a[pa]
            pa += 1
        else:
            c[pc] = b[pb]
            pb += 1
        pc += 1
    # pa가 남았을 경우 (pb가 먼저 nb에 도달)
    while pa < na:
        c[pc] = a[pa]
        pa += 1
        pc += 1
    # pb가 남았을 경우 (pa가 먼저 na에 도달)
    while pb < nb:
        c[pc] = b[pb]
        pb += 1
        pc += 1

    return c

# a = [1,3,4,6,9]
b = [1,5,6,7,10,11]
# c = [None] * (len(a)+len(b))
# print(merge_sorted_list(a,b,c))
    
# return 없고, 변경 시켜주는 함수



# def merge(a):




def merge_sort(a,left, right):
    # 진행 되는 조건
    tmp = [None] * len(a)
    if left < right:
        center = (left + right) // 2

        # right 값을 len으로 넣을 것이기 때문에 등호를 제거해준다!
        merge_sort(a, left = center, right = right)
        merge_sort(a, left = left, right = center)

        pl = left
        pr = center


        while  pl < center - left and pr < right:
            if a[pl] <= a[pr]:
                tmp[pn] = a[pl]
                pl += 1
            else:
                tmp[pn] = a[pr]
                pr += 1

            pn += 1

        while pl < center - left:
            tmp[pn] = a[pl]

            pl += 1
            pn += 1

        while pr < right:
            tmp[pn] = a[pr]
            pr += 1
            pn += 1
        
    return tmp

b = [1,5,6,7,10,11]
n = len(b)
c = [None] * len(b)
merge_sort(b,0,n-1)

import sys
sys.setrecursionlimit(10**8)
read =sys.stdin.readline


def merge_sort(a, left, right):
    tmp = [None] * len(a)

    if left < right:

        # 정가운데 or -1
        center = (left+ right) //2
        print("left : {} , right : {} ".format(left,right))
        merge_sort(a,left = left, right = center)
        merge_sort(a,left = center+1, right = right)
        # i : idx of lower / k : idx of higher
        # j : idx of tmp 
        i, j = left, left
        p = right
        k = center + 1
        print("i : {} , j : {} , k : {}".format(i,j,k))

        while i <= center and k <= right:
            print( " i : {} center : {} k : {} right : {} ".format(i,center,k,right))
            if a[i] <= a[k]:
                tmp[j] = a[i]
                i += 1

            else:

                tmp[j] = a[k]
                k += 1
            j += 1
            print("j 상승 1st", j)
            print("현재 tmp , i, j, k",tmp,i,j,k)

        while i <= center:
            print( " i : {} center : {} k : {} right : {} ".format(i,center,k,right))

            tmp[j] = a[i]
            j += 1
            i += 1
            print("j 상승 2nd", j)

        while k <= right:
            print( " i : {} center : {} k : {} right : {} ".format(i,center,k,right))

            print(j,k)
            tmp[j] = a[k]
            j += 1
            k += 1
            print("j 상승 3rd", tmp,j)
        
    return tmp


a = [1,6,3,8,2]

merge_sort(a,0,len(a)-1)
            


            

