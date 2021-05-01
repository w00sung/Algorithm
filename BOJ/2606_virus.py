from collections import deque
import sys
read = sys.stdin.readline

N_computer = int(read())
N_connection = int(read())
connection = [[] for _ in range(N_computer+1)]
virus_flag = [True]* (N_computer + 1 )
virus_cnt = 0

for _ in range(N_connection):
    strt, end = map(int,read().rstrip().split())
    # 상호 연결임을 인지!
    connection[strt].append(end)
    connection[end].append(strt)

virus_que = deque(connection[1])
virus_flag[1] = False

while virus_que:
    com = virus_que.popleft()
    
    # False 라는 것은 이미 큐에 들어가 있음.
    if virus_flag[com]:
        virus_cnt += 1
        virus_flag[com] = False
        virus_que.extend(connection[com])


print(virus_cnt)
