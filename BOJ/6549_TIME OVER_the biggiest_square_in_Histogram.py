import sys
read = sys.stdin.readline
sys.setrecursionlimit(10**8)
# 나와 같은 or 나보다 높은 앞,뒤 히스토그램 찾기

# !!!!!!!!! 시간 초과 !!!!!!!!1
cnt = 0
def count_hist_right(hist,now,nxt):

    if nxt >= len(hist):
        return

    now_hist = hist[now]
    nxt_hist = hist[nxt]

    # 나보다 큰 놈 나올 때까지 찾기
    if now_hist <= nxt_hist:
        global cnt
        cnt += 1
        count_hist_right(hist,now,nxt+1)
    else:
        return

def count_hist_left(hist,now,nxt):

    # 첫 값은 개수다
    if nxt <= 0:
        return

    now_hist = hist[now]
    nxt_hist = hist[nxt]

    # 나보다 큰놈 나올 때까지 찾기
    if now_hist <= nxt_hist:
        global cnt
        cnt += 1
        count_hist_left(hist,now,nxt-1)

    else:
        return

while True:
    hist = list(map(int,read().rstrip().split()))
    
    if hist[0] == 0:
        break
    res = -1

    for i in range(1, len(hist)):
        cnt = 1
        count_hist_left(hist,i,i-1)
        count_hist_right(hist,i,i+1)
        
        area = cnt * hist[i]
        res = max(res,area)

    print(res)