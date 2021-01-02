import sys
read = sys.stdin.readline

N = int(read())
dp = [0] * (N+1)

for i in range(2,N+1):
    # 모든 숫자 적용가능
    # 1차이 나는 값에서 올라왔다고 가정
    dp[i] = dp[i-1] + 1


    if i % 2 == 0:
        dp[i] = min(dp[i],dp[i//2] + 1)


    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)

print(dp[N])