import sys
read = sys.stdin.readline


# i가 A에 있냐?
def isIn(i,A):
            # i번째 도시는 비트에서 제일 마지막 비트 --> i-2 의 이유
            # 1을 그 도시에 위치하게 밀어준다
    if (A & (1 << (i-2)) != 0):
        return True
    else:
        return False

# 차집합 : A - j
def diff(A,j):
    # 해당 도시를 비트 처리해주고
    t = 1 << (j-2)

    # ~t 와 &연산자를 하면,
    # t가 없는 것만 쏙 빼고 A 요소들이 나온다.
    return (A & (~t))

# 부분집합 A의 원소 개수 세기
def count(A,n):
    count = 0

    # A 의 0 길이 만큼 반복하여
    # 1을 밀어보낸 후 1이 있는지 확인한다.
    for i in range(n):
        if ((A & (1 << i)) != 0):
            count += 1
    return count

def travel(W):
    n = len(W) - 1
    # 집합의 최대 bit
    size = 2**(n-1) # 총 n-1 개
    D = [[0] * size for _ in range(n+1)]
    
    # 0은 취급하지 않고, 1은 시작점이다.
    # "부분집합 0개"일 때, 먼저 대입해준다.
    for i in range(2,n+1):

        # 종착지로 가는 거리가 없으면?
        if W[i][1] == 0:
            D[i][0] = float('inf')
        
        # 맨 마지막 종착지는 i에서 1로 가는 거리
        else:
            D[i][0] = W[i][1]

    # 부분집합 개수 별로 진행 (순서대로) -- 밑에서 부터
    for k in range(1,n-1):
    
        # 각 집합 별로 (가능한 A 모두 도입)
        for A in range(1, size):
    
            # A의 부분집합 개수가 k개 이면? 
            # 1개부터 n-1 개 까지!
            if (count(A,n) == k):
                # 2에서 n까지 진행해준다.
                for i in range(2,n+1):
                    # i가 A에 들어가 있지 않은 경우에만
                    if (not isIn(i,A)):
                        #D[i][A] : i도시에서 A의 도시들을 거쳐서 
                        #           1에 도달할 수 있는 최적값
                        D[i][A] = minimum(W,D,i,A)

    # 우리의 모든 subset별 계산을 마치고 
    # 최종 목적지를 작성해준다.
    A = size - 1
    D[1][A] = minimum(W, D, 1, A)
    return D

# 갈 수 없는 도시 처리

# W : 도시간 거리 
# D : 부분집합별 비교
# 그 때마다의 i
def minimum(W,D,i,A):
    minValue = float('Inf')
    n = len(W) - 1
    # 각 도시별로,
    for j in range(2,n+1):
        # 해당 도시가 A에 속해 있는 경우에만
        if (isIn(j,A)):

            # i와 j는 같을 수 없다.
            if W[i][j] == 0:
                m = float('inf')

            else:
                # i에서 j까지 간 거리 + j에서 나머지 활용해서 간 거리의 최적값
                m = W[i][j] + D[j][diff(A,j)]

            # minValue : i도시에서 A까지 도달할 때, 
            #                           가장 최소 값
            if (minValue > m):
                minValue = m

    return minValue

N = int(read().rstrip().strip())
W = [[-1] * (N+1) for _ in range(N+1)]
for i in range(1,N+1):
    W[i][1:] = map(int,read().rstrip().split())

# for i in range(1,N+1):
#     for j in range(1,N+1):
#         if i != j and W[i][j] == 0:
#             W[i][j] = float('inf')

D = travel(W)
print(D[1][2**(N-1)-1])
# print(D)
# print(W)