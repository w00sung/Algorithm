import sys
read = sys.stdin.readline

n = int(read())
arr = []
cnt = [0 0]
for _ in range(n):
    arr.append(list(map(int,read().rstrip().split())))

# arr 을 len(arr) // 2 를 하여 인덱스
def cut(arr,n):


    i = len(cut)
    # 다 잘렸으면
    if n == 0 :
        if arr[0][0]:
            cnt[0] += 1
        else:
            cnt[1] += 1

    else:

        k = n // 2
        cut(arr[0:k][0:k],k)

        cut(arr[k:n][k:n],k)

        cut(arr[])