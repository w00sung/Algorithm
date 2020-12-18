
def get_posi_strt(arr,strt,end):

    while strt <= end:

        mid = (strt + end) // 2

        if arr[mid] > 0 and arr[mid-1] < 0:

            return mid

        # 내가 찾은게 0보다 작으면 -- 우측에 있음
        elif arr[mid] < 0 :

            strt = mid + 1

        # 0보다 큰데, 좌측이 0보다 크면 -- 왼쪽에 있음
        else: 
            end = mid - 1
    
    # 양수가 없으면
    # return end+1 -- out of index로 빼버릴까?
    return end+1


def is_nearest(arr,idx):
    if(abs((abs(arr[mid])-find)) <= abs(abs(arr[mid+1])-find)):
        if abs((abs(arr[mid-1])-find)) >= abs(abs(arr[mid])-find)

def binary_search(arr,find,strt,end):

    while strt <= end:

        mid = (strt + end) // 2

        # **** 여기 잘못됐음 **** 항상 큰 값만 가까운게 아니다
        # 가장 가까운 값!!!!!!!!!!!!!!! 아오

        # 절대값 커진다 -- 가장 비슷한값
        # 인덱스 벗어날 것 고려                     # 등호 : 첫번째 녀석 고려해보니 붙여야겠음
        if abs((abs(arr[mid])-find)) <= abs(abs(arr[mid+1])-find) or abs(arr[mid]) == find:
            return arr[mid]

        else:
            strt = mid + 1


    # 없을 수가 없다고 생각..
    return None





def get_0(arr,strt,end):
    li = []
    res_sum = float('inf')
    # 양수 시작 위치
    posi_strt = get_posi_strt(arr,strt,end)

    # 모두 양수
    if posi_strt ==  strt:
        return arr[strt], arr[strt+1]

    # 모두 음수
    elif posi_strt == end+1:
        return arr[end-1], arr[end]

    else:

        # 양수부분에서 하나씩 뽑는다.
        for find in arr[posi_strt:]:
            
            # 음수 부분에서 가장 가까운 값 찾기
            neg_find = binary_search(arr,find,0,posi_strt-1)
            now_sum = neg_find + find
            
            # 0에 가장 가까운 값을 나타내는 now_sum 구성원 뽑기
            if res_sum > now_sum:
                res_sum = now_sum
                li =[neg_find, find]    


        return li

arr = [-2,4,-99,-1,98]
arr.sort()

print(get_0(arr,0,len(arr)-1))


