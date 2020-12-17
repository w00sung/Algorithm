def ddeok_sum(ddeok,mid):
    sum = 0
    for i in ddeok:
        if i - mid >0:
            sum += (i-mid)

    return sum


def binary_cut(ddeok, want, strt, end):

    # 커트 접근 -> 얻을 수 있는 총 길이 구하고 
    # 길면 커트 높이고, 짧으면 커트 늘리고
     
    while strt <= end:
        
        mid = (strt + end) // 2
        if ddeok_sum(ddeok,mid) == want:
            return mid

        if (ddeok_sum(ddeok,mid) > want):
            strt = mid + 1

        else :
            end = mid -1

    return None
n, want = map(int, input().split())
ddeok = list(map(int, input().split()))
print(binary_cut(ddeok,want,0,max(ddeok)))