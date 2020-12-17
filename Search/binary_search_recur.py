
def binary_search_recur(data, find, strt, end):

    if strt > end:

        return None
    mid = (strt + end) // 2

    if data[mid] == find:
        
        # 위치 반환
        return mid

    elif data[mid] < find:
        
        # 찾고자 하는게 더 크다 -- 범위를 우측으로
        binary_search_recur(data,find,mid+1,end)

    else:

        # 찾고자 하는게 더 작다 -- 범위를 좌측으로
        binary_search_recur(data,find,strt, mid-1)