import sys
read = sys.stdin.readline


# 범위를 줄여서도 다 가봐야함?
def count_number(arr,find,strt,end):
    cnt = 0

    a = first(arr,find,strt,end)

    b = last(arr,find,strt,end)
    
    # 못찾으면
    if a is None and b is None:
        cnt = -1
    # 찾으면 ( 한쪽 만 찾는 경우는 없음 )
    else:
        cnt = b-a + 1

    return cnt


def first(arr,find,strt,end):
    # 못찾음
    if strt > end :
        return None

    else:
        mid = (strt+end) // 2
        # 내가 찾은 놈이 find  &&& ***왼쪽 놈이 나보다 작거나 없어야함***
        if (arr[mid] == find) and (arr[mid-1] < find or mid ==0):
            return mid

        # 큰 놈이면
        elif arr[mid] < find:
            # 이 함수 불러와 !! 여기로 들어가~
            return first(arr, find, mid+1, end)

        # 작은놈이거나, ***찾은놈이 find 인데, 왼쪽에 똑같은게 더있으면***
        else:
            return first(arr,find,strt,mid-1)

def last(arr,find,strt,end):
    # 못찾음
    if strt > end:
        return None
    
    else:
        mid = (strt + end) // 2

        # 내가 찾은 놈이 find &&& *** 우측 놈이 나보다 크거나, 내가 우측 끝에 있을
        if (arr[mid] == find) and (arr[mid+1] > find or mid == n-1):
            return mid

        elif arr[mid] > find:
            return last(arr, find, strt, mid-1)

        ## 찾고있는놈이 더 크거나, find를 찾았는데 우측에 더 있거나 내가 우측 끝에 없을 경우
        else:
            return last(arr,find, mid+1, end)

n, find = map(int,read().rstrip().split())
arr = list(map(int,read().rstrip().split()))

print(count_number(arr,find,0,n-1))