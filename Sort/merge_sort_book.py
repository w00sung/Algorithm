import sys
sys.setrecursionlimit(10**8)
read =sys.stdin.readline

def _merge_sort(a):
    def merge_sort(a, left, right):

        if left < right :
            center = (left + right) //2

            merge_sort(a, left, right)
            merge_sort(a, center+1, right)


            p = j = 0
            i = k = left

            # 절반까지 buff 에 복사
            # a에는 절반 이상이 설정
            while i <= center:
                buff[p] = a[i]
                p += 1
                i += 1

            # a의 k(left)를 채운다.
            while i <= right and j < p:
                if buff[j] <= a[i]:
                    a[k] = buff[j]
                    j += 1
                
                else:
                    a[k] = a[i]
                    i += 1
                k += 1

            while j < p:
                a[k] = buff[j]
                
                k+=1
                j+=1

    n = len(a)
    buff = [None] * n
    merge_sort(a,0,n-1)
    del buff

a = [1,3,5,7,2]
_merge_sort(a)