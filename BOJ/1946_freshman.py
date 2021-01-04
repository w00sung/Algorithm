import sys
read = sys.stdin.readline

# 얘를 집합으로 설정한다.
N_test = int(read())
new = [[] for _ in range(N_test)]

rank_paper1_interview = 0
rank_interview1_paper = 0

for i in range(N_test):
    N_new = int(read())
    ans = []
    for _ in range(N_new):
        paper, interview = map(int,read().rstrip().split())
        new[i].append((paper,interview))

        # 각 1등의 interview와 paper 순위를 받는다.
        if paper == 1:
            rank_paper1_interview = interview

        if interview == 1:
            rank_interview1_paper = paper


    # 둘중에 더 작은 놈 선정
    # 서류 1등의 면접 등수가 더 낮으면
    if rank_paper1_interview < rank_interview1_paper:
        # interview 순으로 정렬
        # 범위 좁힐 거임
        ans = sorted(new[i], key = lambda x : x[1])
        limit = rank_paper1_interview
        cnt = 0
        criteria = float('inf')
        for i in range(limit):
            if criteria > ans[i][0]:
                cnt += 1
                criteria = ans[i][0]

            elif criteria < ans[i][0]:
                continue
                
    # 면접 1등의 서류 등수가 더 낮으면
    elif rank_paper1_interview >= rank_interview1_paper:
        # 면접 순으로 정렬
        ans = sorted(new[i], key = lambda x : x[0])
        limit = rank_interview1_paper
        cnt = 0
        criteria = float('inf')
        for i in range(limit):
            if criteria > ans[i][1]:
                cnt += 1
                criteria = ans[i][1]

            elif criteria < ans[i][1]:
                continue


    print(cnt)