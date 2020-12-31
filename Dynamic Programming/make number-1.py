import sys
read = sys.stdin.readline

num = int(read())

cnt = 0
dp = [0] * (num+1)
# 연산의 최소값

for i in range(2,num+1):

    # 2부터 시작이다.
    dp[i] = dp[i-1] + 1

    if i % 2 == 0:
        # 2로 나눠서 얻은 숫자의 결과 값에 1더한것  -- 하나 내려온거임
        # ex) 8 은 4가 만들어진 시간에 1개 더한것 vs 7에서 1더해서 만든 것
        dp[i] = min(dp[i], dp[i//2] + 1)

    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)
    
    if i % 5 == 0:
        dp[i] = min(dp[i], dp[i//5] + 1)

print(dp[num])

# dx = [0] * (num+1)

## 재귀로도 사용해보고 싶다.