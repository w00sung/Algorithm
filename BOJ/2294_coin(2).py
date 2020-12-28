from collections import deque
import sys
read = sys.stdin.readline


N, goal = map(int, read().rstrip().split())
coin = []
for _ in range(N):
    coin.append(int(read()))

coin.sort(reverse = True)
visited = [False] * (N):
cnt = 0
tot = 0
min_cnt = float('inf')
res = False

for i in range(N):
    tot = 0
    cnt = 0
    queue = deque(coin[i:])
    
    while queue:

        now = queue[0]
        
        if tot + now > goal:
            queue.popleft()
            continue
        
        cnt += 1
        if cnt > min_cnt:
            break

        if tot + now == goal:
            res = True
            break
        
        if tot + now < goal:
            tot += now
            continue

    
    if cnt == 0:
        continue
    if res == True:
        min_cnt = min(cnt,min_cnt)

if res ==True: 
    print(min_cnt)
else:
    print(-1)