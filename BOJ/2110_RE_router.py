import sys
read = sys.stdin.readline

n, c = map(int,read().rstrip().split())
house = []

for _ in range(n):
    house.append(int(read()))

house.sort()

# 탐색 최대값
max_d = house[-1] - house[0]
# 탐색 최소값
min_d = 1
now = house[0]
res = -1
# 이분 탐색의 while
while True:

    # 이분탐색 종료 조건
    if min_d > max_d:
        break

    dist = (max_d + min_d) // 2
    
    # 거리 설정되었으면 검증한다.
    now = house[0]
    # 공유기 개수 cnt
    # 초기화는 1로 -- 나는 설치하고 시작됨
    cnt = 1
    for i in range(1,n):

        # 거리보다 멀거나 같게 떨어진 친구 발견시 !
        # 공유기 설치 & 다음 설치로 넘어감
        if house[i] >= now + dist:
            cnt += 1
            now = house[i]

        # 내 거리보다 적게 떨어진 친구는 설치 못한다.
        # 건너뛴다.

    # 검증
    # 많거나 같게 세었으면, 탐색 거리 늘려준다.
    # -- 거리가 작거나, 딱 맞았으면 --> max로 작은 것 처리
    if cnt >= c:
        res = max(res,dist)
        min_d = dist + 1

    else:
        max_d = dist - 1

print(res)
