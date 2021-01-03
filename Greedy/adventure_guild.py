import sys
read = sys.stdin.readline

N = int(read())
adv = list(map(int, read().rstrip().split()))

adv.sort()

ans = 0
cnt = 0
for i in range(N):

    cnt += 1

    if adv[i] < cnt:
        cnt = 1
        ans += 1
    
    elif adv[i] >= cnt:
        # 끝에서도 연속되면 덩어리로 끊어준다.
        if i == N-1:
            ans += 1
        continue
    
print(ans)