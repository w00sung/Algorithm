import sys
read = sys.stdin.readline

num_coins, goal = map(int,read().rstrip().split())
coins = []
max_num = 100000
dp = [max_num] * (100001)
for _ in range(num_coins):
    coin = int(read())
    coins.append(coin)

    # base coin 들은 만드는데 1개 걸린다.
    dp[coin] = 1


for i in range(1, goal+1):
    for coin in coins:
        if i > coin:
            dp[i] = min(dp[i], dp[i-coin] + 1)
if dp[goal] != max_num:
    print(dp[goal])
else:
    print(-1)


def dfs(num):

    if dp[num] != max_num:
        return dp[num]

    
    