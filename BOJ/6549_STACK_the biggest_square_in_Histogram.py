import sys
read= sys.stdin.readline

while True:
    hist = list(map(int,read().rstrip().split()))
    
    if hist[0] == 0:
        break
    # 마지막 순간, 
    # 스택을 모두 비우면 끝!
    stack = []
    max_area = 0
    # 1번째는 삽입 (좌측 꼭지점, 높이)
    stack.append((0,hist[1]))
    # 2번째부터 비교, 넣어주기
    
    # stack top의 높이, 위치
    for i in range(2,len(hist)):

        height = stack[-1][1]
        
        now_hist = hist[i]
        # 큰 놈이 들어오면?
        if height < now_hist:

            # 왼쪽 점과 높이 넣는다.
            stack.append((i-1,hist[i]))
        

        # 작은 놈이 들어오면?! 
        # --> 스택 내용물에 대해 다 비교 후 넓이 계산 할 것 들 다 계산
        elif height > now_hist: 
            # stack 안에 있는 녀석들 다 비교 필요.
            # 작은 놈은 살려둔다.
            # stack에 존재할 때 실행되어야 함
            while stack and stack[-1][1] > now_hist:
                # 넓이 계산 후 최고만 넣는다.
                height = stack[-1][1]
                idx = stack[-1][0]
                now_area =  ((i-1) - idx) * height
                max_area = max(max_area,now_area)
                pop_hist = stack.pop()
                # 최소 위치, 본인 높이 넣는다.
            
            # 최소 위치는 마지막 pop 된 녀석이 갖고 있던 위치
            stack.append((pop_hist[0],now_hist))
    
    right = len(hist)-1
    # 마무리 작업
    while stack:
        pop_hist = stack.pop()
        pop_height =pop_hist[1]
        pop_idx = pop_hist[0]
        now_area = (right - pop_idx) * pop_height
        max_area = max(max_area, now_area)
        # 같은 놈이 들어오면 안 넣어준다.

    print(max_area)



