from collections import deque
import sys
read = sys.stdin.readline

# 에라토스테네스의 체
N = 10000

flag = [True] * (N+1)
for i in range(2, N):

    if flag[i]:
        for j in range(2*i, N, i):
            flag[j] = False


def is_prime(num):
    if flag[num]:
        return True
    else:
        return False

def get_possible(num):
    for i in range(0,4):
        for j in range(0,10):
            tmp = list(str(num))
            if i == 0 and j == 0 :
                continue
            if tmp[i] != str(j):
                tmp[i] = str(j)
                check_num = int("".join(tmp))
                if is_prime(check_num) and visited[check_num] == False:
                    visited[check_num] = True
                    # print(check_num)
                    que.append(check_num)

# 소수이면 계속 깊게 들어가는 dfs를 작성한다.
cnt = 0
M = int(read())
for _ in range(M):
    strt, target = map(int,read().rstrip().split())
    que = deque([strt])
    cnt = 0
    check = True
    visited = [False] * (N+1)
    while que:
        len_que = len(que)
        # len_que 안쓰려면 값을 cnt와 같이 append 하는 방법이 있다.
        while len_que: 
            num = que.popleft()
            if num == target :
                print(cnt)
                check = False
                break
            len_que -= 1
            get_possible(num)

        if check == False:
            break
        cnt += 1
    if check:
        print("impossible")
    

