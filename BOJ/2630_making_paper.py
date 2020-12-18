import sys
read = sys.stdin.readline

n = int(read())
arr = []
cnt = [0,0]
for _ in range(n):
    arr.append(list(map(int,read().rstrip().split())))

# arr 을 len(arr) // 2 를 하여 인덱스

## 길이에 맞춰서 for문 돌리기?
# arr : 배열, x,y : 시작점 행,열
def cut(arr,x,y,n):
    global cnt
    brk = False
    theme = 0
    theme = arr[x][y]

    # 종료조건에 반드시 return !!!!!!!!!
    if n==1:
        cnt[theme] += 1
        return



    for i in range(x,x+n):
        for j in range(y,y+n):
            if arr[i][j] != theme:
                # 초기값과 다른 값 등장시 짤!
                brk = True
                break
        if brk:
            break
    
    if brk:
        k = n // 2
        # y true 면 잘릴 일 없다.
        # arr[0:k][0:k] 불가능함
        ## 분할 --- 범위를 조절
        # 1사분면
        cut(arr,x,y,k)
        # 2사분면
        cut(arr,x,y+k,k)
        # 3사분면
        cut(arr,x+k,y,k)
        # 4사분면
        cut(arr,x+k,y+k,k)
    else:
        cnt[theme] += 1

cut(arr,0,0,n)
print(cnt[0])
print(cnt[1])