import sys
import heapq
from collections import deque

read = sys.stdin.readline

N_hole, tot_cnt = map(int,read().rstrip().split())

# 물건 별, 순서 
stuffs = [[] for _ in range(tot_cnt+1)]

# 순서
order = deque(list(map(int,read().rstrip().split())))


# 거꾸로 넣기 !
for i in range(tot_cnt-1,-1,-1):
    # 각기 stuff에 따른 순서를 append
    stuffs[order[i]].append(i+1)


# 1이면 꽂아 있는 거임
# multitab = [0] * (stuffs+1)
multitab = []
multitab_flag = [False] * (tot_cnt+1)
## 멀티탭에 뭐가 있는 지 명시

## 개수가 작고, 나중에 오는 것 먼저 뺀다.
## 개수 제일 작은 것 명시, 제일 늦게 오는 것 명시


cnt = 0
while order:


    stuff = order.popleft()
    stuffs[stuff].pop()
    ### 곧 올 순서
    # 다시 올 일 없으면

    if len(stuffs[stuff]) == 0:
        soon = 101
    else:
        # 다음 녀석으로 뽑혀야 됨
        soon = stuffs[stuff][-1]


    
    # 들어 왔던 것이 들어오면 
    # 물건 있으면 뺄 필요 없다. - 다음 순서는 업데이트 해줘야됨
    # 또 오는 거는 제일 빨리 오는 거임
    if multitab_flag[stuff]:

        multitab.pop()
        heapq.heappush(multitab,(-soon,stuff))

        continue

    # 다음에 오는 번호 순으로 heap을 만들까?
    # 늦게오는게 + 안오는거 빠져야됨
    if len(multitab) >= N_hole:
        
        # 빠질 때도 뭐가 빠졌는지 알아야됨
        left_stuff = heapq.heappop(multitab)[1]
        multitab_flag[left_stuff] = False
        cnt += 1
        heapq.heappush(multitab,(-soon,stuff))
        
    else:
        heapq.heappush(multitab,(-soon,stuff))

    multitab_flag[stuff] = True

print(cnt)