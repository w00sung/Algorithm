import sys
read = sys.stdin.readline

N, calc_cnt = map(int,read().rstrip().split())
parent = [0] * (N+1)
level = [1] * (N+1)

# 초기화
for i in range(N+1):
    parent[i] = i

def find(n):
    # 내가 루트냐?
    if n == parent[n]:
        return n

    # 루트를 찾으러가면서, 루트와 직속으로 이어줌
    parent[n] = find(parent[n])
    return parent[n]

def merge(a,b):
    # 루트 구해와!
    a = find(a)
    b = find(b)

    if a == b:
        return

    # 뒤에 녀석이 더 깊숙이 있는 녀석으로 고정 
    # >>> 루트의 level은 트리의 깊이를 의미한다.
    if (level[a] > level[b]):
        a, b = b, a

    parent[a] = b

    if level[a] == level[b]:
        level[b] += 1

for i in range(calc_cnt):
    func, a, b = map(int,read().rstrip().split())
    if func == 0:
        merge(a,b)
    else:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")
