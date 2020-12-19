import sys
read = sys.stdin.readline

n = int(read())
tower = list(map(int,read().rstrip().split()))
res = []
def get_received(tower)
    ptr = len(tower)
    crtria = tower.pop()
    # 첫번째는 자동 0
    for _ in range(n-1):
        nxt = tower.pop()
        # 내가 맞출 놈의 위치
        ptr -= 1

        # 다음이 나보다 작으면
        # -- 작은 놈은 내가 맞추는 놈하고 똑같다
        if nxt >= crtria:
            # pop된 함수 call 한다.

            get_received(tower)
            # 큰 놈도 작은 놈 찾으면 돌아온다.
    
    # pop해서 발견하면 index추가
    res.append(ptr)
    # 돌아가야되는데...?

