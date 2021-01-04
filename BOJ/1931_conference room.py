import sys
read = sys.stdin.readline

N = int(read())
conferences =[]

for _ in range(N):
    strt, end = map(int,read().rstrip().split())
    conferences.append((strt,end))

conferences = sorted(conferences, key = lambda x : x[0])

## 일찍 시작하는 것이 만능은 아니다.
# 영역 안에 많은 개수가 들어오는게 더 좋다.
# (2,5) 보다 (3,3)(3,4)(4,5) 가 좋다.

# 첫 친구의 끝 시간 
criteria = float('inf')
cnt = 1
for strt,end in conferences:

    # 기준보다 빨리 시작하고, 빨리 끝나는 친구 있으면,
    if strt < criteria and end < criteria:

        #기준을 바꿔준다.
        criteria = end

    # 시작 끝 같은 놈도 있음!
    # 앞 영역 시간 끝 ! 뒷 영역 시간 시작!
    elif strt >= criteria:
        cnt += 1
        criteria = end

print(cnt)