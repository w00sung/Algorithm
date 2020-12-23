import sys
read = sys.stdin.readline

x,y = 7,2
L = 4
n_gun ,n_ani, L = map(int,read().rstrip().split())

gun = list(map(int,read().rstrip().split()))
animal = []

for _ in range(n_ani):
    
    animal.append(list(map(int,read().rstrip().split())))

gun.sort()
cnt = 0
for ani in animal:
    x = ani[0]
    y = ani[1]

    able_dist = L-y

    # 더이상 움직일 수 없으면 넘기자 -- 속도 감소 50ms
    if able_dist < 0:
        continue


    # gun 의 좌, 우측 끝 좌표
    left = 0
    right = len(gun)-1

    # x +- L-y 반경에 사대가 있냐?
    # x - (L-h) <= gun <= x + (L-h)

    # 사대의 위치를 이분탐색
    while left <= right:

        mid = (left+right) // 2

        # 상한보다 멀리있냐?
        if gun[mid] > x + able_dist:

            right = mid - 1

        # 상한안에 들어오면,
        elif gun[mid] <= x+able_dist:
            
            # 범위 안에있으면
            if x-able_dist <= gun[mid]:
                cnt += 1
                break

            # 상한안에는 들어오는데, 작으면
            else:
                left = mid + 1

    
print(cnt)