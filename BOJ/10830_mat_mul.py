import sys
read= sys.stdin.readline
# i : 행, j : 열

matrix = []
n, k = map(int,(read().rstrip().split()))
# 행렬 입력
for _ in range(n):
    matrix.append(list(map(int,read().rstrip().split()))) 


# row = 0
# col = 0
# # i를 움직여 줄거다.
# col_cnt = 0

# 제곱하는 카운팅
def get_square(n, matrixL,matrixR):
    res = [[0] * n for i in range(n)]
    row = 0
    col = 0
    col_cnt = 0
    ele = 0
    
    while True:
        ele = 0
        # 열이 n번 움직이면 행을 +1 해준다.

        # row 행, col 열
        for j in range(n):
            ele += matrixL[row][j] * matrixR[j][col]
            col_cnt += 1

        res[row][col] = ele % 1000

        # 행, 열 다 넣어줬으면 out
        if row == n-1 and col == n-1:
            break

        # 열 되돌리기, 행 늘려주기
        # 행 늘려주기
        if col_cnt % (n*n) == 0:
            col = 0
            row += 1
        else:
            col += 1

    return res

# 제곱
# mul = get_square(n, matrix, matrix)

# # 4제곱
# mul = get_square(n,mul,mul)


# ## 곱셈 구현
# ans = mul
# ans = get_square(n,ans,ans)

# 결과는 1000으로 나눈것이다.

# 재귀는 계속 본인을 불러오고, 던져준다 !!!
def get_mul(n,matrix,k):
    
    # 제곱이면 본인
    if k == 1:
        
        # 본인은 1000으로 나눠서 보내준다.
        # 요소로 1000 갖고 있을 수 있음!!!
        for i in range(n):
            for j in range(n):
                matrix[i][j] = matrix[i][j] % 1000
        
        return matrix
        
    # 2의 배수 제곱이면
    if k % 2 ==0:
        ans = get_mul(n,matrix,k//2)
        res = get_square(n,ans,ans)
        return res

    # 홀수 처리 !!!
    else:
        ans = get_mul(n,matrix,k//2)
        # res 는 제일 받아온 놈 제곱해서
        res = get_square(n,ans,ans)
        # 1이랑 곱해줌
        res = get_square(n,matrix,res)
        return res

mul = get_mul(n,matrix,k)


for i in range(n):
    print(*mul[i])