import sys
read = sys.stdin.readline

N = int(read())

# size : 부분집합 가능 개수
size = 2**(N-1)
W = []
for _ in range(N):
    W.append(list(map(int,read().rstrip().split())))

DP = [[0] * size for _ in range(N)]

def set_count(Set):
    count = 0
    binary = format(Set,'b')
    # Set의 길이까지만 push 한다.
    for push in range(len(binary)+1):
        if (Set & (1 << push) != 0):
            count += 1

    return count

def is_subset(Set,sub):
    # sub -1 이 2진수에서 위치임
    # 000'1' 은 0번 push 했을 때, 확인할 수 있음
    if (Set & (1 << (sub-1)) != 0 ):
        return True
    else:
        return False


def travel():
    # 0번 도시가 우리의 출발지
    
    # 부분집합 0개일 때,
    # 바로 0번 도시로 가는경우 
    for i in range(1,N):
        # 0번 도시로 가는길 막혔으면 inf
        # 우리는 최소값만 취할 것이기 때문에 inf 처리
        if W[i][0] == 0:
            DP[i][0] = float('inf')

        else:
            DP[i][0] = W[i][0]

    # 부분집합 개수 : 1<=  <= N-2 까지 구한후,
                            # N-1 은 따로 구함

    # 우리의 목표는 부분집합 1개부터 N-2개
    for set_num in range(1,N-1):

        # 부분집합 00000...1 부터 2**(N-1)-1 까지
        for Set in range(1,size):
            
            # 부분집합 개수가 작은 수부터
            if set_count(Set) == set_num:
                # 0번 도시 제외 Set에 들었나 안들었나 확인용
                for strt in range(1,N):
                    # 부분집합이 아니면?
                    # 시작점은 부분집합이 아니어야 함
                    if (not is_subset(Set,strt)):
                        # 0번 도시 제외 각각 돌아오는 값 구함
                        DP[strt][Set] = minimum(strt,Set)
    
    final_Set = size - 1
    # 0에서 출발해서 마지막 세트를 이용하여 구할 수 있는 최소값 -- 다른 도시는 구할 필요 없다.
    DP[0][final_Set] = minimum(0,final_Set)
    ans = DP[0][final_Set]

    return ans

def minimum(strt,Set):
    minValue = float('inf')

    for city_num in range(1,N):
        
        # 부분집합 일 때만!
        if is_subset(Set,city_num):

            if W[strt][city_num] == 0:
                m = float('inf')

            else:
                
                reverse_binary_city = ~(1 << (city_num -1))                    
                # Set&(~A) : 차집합
                diff_set = Set & reverse_binary_city
                m = W[strt][city_num] + DP[city_num][diff_set]

            if minValue > m:
                minValue = m
                
    # strt에서 Set을 거쳐 도착하는데, 가장 짧은 값
    return minValue

print(travel())