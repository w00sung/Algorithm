import sys
read = sys.stdin.readline

def get_two(arr, strt, end):
    ans_li = []
    ans = float('inf')
    # 같아지면 안됨, 동일 숫자 허용 x
    while strt < end:

        front = arr[strt]
        back = arr[end]

        tmp = front + back

        # 전에 대답과 비교해야함
        if tmp == 0:
            return front, back
        
        else:
            # 양의 값 : 큰값을 줄인다.
            if tmp > 0:
                end -= 1
            # 음의 값 : 작은 값을 크게한다.
            else:
                strt += 1

        # 작업 진행 중에 작아졌는지 체크하면서 저장
        if abs(tmp) < abs(ans):
            ans = tmp
            ans_li = [front, back]

    return ans_li[0], ans_li[1]

n = int(read())
arr = list(map(int,read().rstrip().split()))
arr.sort()
ans_a, ans_b = get_two(arr,0,len(arr)-1)
print(ans_a, ans_b)