
def binary_search(arr,strt,end):

    while strt <= end:

        mid = (strt + end) // 2

        if arr[mid] == mid:

            return mid

        # 숫자가 idx보다 크면, 우측은 절대 잡을 수 없다.
        elif arr[mid] > mid:

            end = mid -1
        
        # 숫자가 idx보다 작으면, 좌측은 절대 잡을 수 없다.
        else:

            strt = mid +1

    return -1

n = int(input())
arr = list(map(int,input().split()))

print(binary_search(arr,0,n-1))