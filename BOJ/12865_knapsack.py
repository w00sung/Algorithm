import sys
read = sys.stdin.readline


N, limit_weight = map(int,read().rstrip().split())

knapsack = []
for _ in range(N):

    weight, value = map(int,read().rstrip().split())
    knapsack.append((weight,value))

# 무게 순 정렬
# knapsack.sort()

# 열 : 가방 무게 , 행 : limit 까지의 무게 // # 열을 무게 만큼 만들기 위해 + 1 해주었음
table = [ [0] * (limit_weight+1) for _ in range(N) ]

# 나를 이용한 것이 크냐? 아니면 나를 이용하지 않은 것이 크냐?
for row in range(N):
    knapsack_weight = knapsack[row][0]
    knapsack_value = knapsack[row][1]
    for tot_weight in range(1,limit_weight+1):
        # 총 무게가 나의 무게와 같거나 크다면?
        # max(나를 이용해서 만든 것, 나를 이용하지 않고 만든 것)

        if tot_weight >= knapsack_weight:
            # 첫 줄은 가방 한개로 만들고 있다 -> 본인 값
            if row == 0:
                table[row][tot_weight] = knapsack_value
            else:
                # "value + 나를 빼고, (총 무게 - 배낭무게)를 만든 값" VS 나 빼고 지금 무게 만든 값         
                table[row][tot_weight] = max(knapsack_value + table[row-1][tot_weight - knapsack_weight],table[row-1][tot_weight])
        
        # 나로 만들 수 없는 상황이면, 앞전에 만든 가치
        elif tot_weight < knapsack_weight:
            if row > 0 :
                table[row][tot_weight] = table[row-1][tot_weight]
        

# print(table)
print(table[N-1][limit_weight])