import sys
read = sys.stdin.readline

# 행렬 개수
N = int(read())

matrix = []

# N+1 x N+1 테이블 생성
# table[i][j] = 행렬(i) 에서 행렬(j)까지 곱할 때 최적값
table = [[0] * (N) for _ in range(N)]

for _ in range(N):
    row, col = map(int,read().rstrip().split())
    matrix.append((row,col))

def put_table():
    # for i in range(N):
    #     table[i][i] = 0
    #     # 대각 행렬 계산해주기

    # 대각선으로 다루기 !
    for diagonal in range(1,N):
        # 행은 1,2,3,4 -> 1,2,3 -> 1,2 -> 1
        # diagonal top으로 갈 때 마다 줄여준다.
        for row in range(N - diagonal):
            # 열은 하나씩 밀린다.
            col = row + diagonal
            table[row][col] = get_value(row,col)


def get_value(row,col):
    value = float('inf')
    # table[1][3] = table[1][1] + table[2][3] + matrix[1][0] * matrix[2][0] * matrix[3][1]
    for k in range(row,col):
        value = min(value, table[row][k] + table[k+1][col] + matrix[row][0] * matrix[k+1][0] * matrix[col][1])
        
    return value

put_table()
print(table[0][N-1])