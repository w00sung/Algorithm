
def binary_search_repeat(data, find, strt, end):

    # 반복문으로 진행 시에는,
    # strt, end만 mid를 이용하여 변경해준다.
    while strt <= end:
        
        mid = (strt + end) // 2

        if data[mid] == find:
            return mid

        elif data[mid] < find:
            strt = mid+1

        else:
            end = mid-1

    # strt > end 가 되면
    return None