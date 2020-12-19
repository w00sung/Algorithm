from collections import deque
import sys
read = sys.stdin.readline

n, m = map(int,read().rstrip().split())
queue = list(range(1,n+1))
res = []
front = 0
while queue:
    # 그 인덱스에 다음 숫자온다. 
    # -- 여기가 시작점 : front를 계속 변경 시켜줘야함  !!!!!!!
    idx = (front + (m-1)) % len(queue)
    res.append(queue.pop(idx))
    
    front = idx


print("<"+", ".join([str(i) for i in res])+">")