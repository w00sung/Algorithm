import sys
read = sys.stdin.readline

N_coin, goal = map(int,read().rstrip().split())
coins = []
for _ in range(N_coin):
    coin = int(read())
    if coin <= goal:
        coins.append(coin)

cnt = 0
while True:

    if goal == 0:
        break
    # 큰 것부터 꺼내온다.
    coin = coins.pop()

    # 개수는 coin으로 만들 수 있는 goal * N    
    cnt += (goal // coin)
    # 나머지만 맞추면 된다.
    goal %= coin 
    
print(cnt)
