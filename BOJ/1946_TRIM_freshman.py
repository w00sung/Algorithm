import sys
read = sys.stdin.readline

# 얘를 집합으로 설정한다.
N_test = int(read())

for i in range(N_test):
    N_new = int(read())
    new = [0] * (N_new+1)
    for _ in range(N_new):
        paper, interview = map(int,read().rstrip().split())

        # 인덱스를 걸어줘서 자동으로 정렬되어있음
        new[paper] = interview


    criteria = float('inf')
    cnt = 0
    for paper in range(1,N_new+1):
        if criteria > new[paper]:
            cnt += 1
            criteria = new[paper]

        elif criteria < new[paper]:
            continue

    print(cnt)