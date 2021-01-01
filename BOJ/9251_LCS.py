import sys
read = sys.stdin.readline

strA = list(read().rstrip())
strB = list(read().rstrip())

# 첫 행, 첫 열은 0으로 채워놓는다.
table = [[0] * (1+len(strB)) for _ in range(1+len(strA))]

# LCS - DP 테이블 생성
# 세로에 A(열)가 위치하고, 가로에 B(행)가 위치해있다.
for table_idx_A, i in enumerate(range(len(strA)),1):
    for table_idx_B, j in enumerate(range(len(strB)),1):
        # i번째 문자 vs j번째 문자
        if strA[i] == strB[j]:
            table[table_idx_A][table_idx_B] = table[table_idx_A-1][table_idx_B-1] + 1

        else:
            table[table_idx_A][table_idx_B] = max(table[table_idx_A-1][table_idx_B], table[table_idx_A][table_idx_B-1])

ans_len = table[len(strA)][len(strB)]
print(ans_len)

# 개수 변환 지점 check -- 문자열 추출

ans = []
# 문자열 출력
# 행 단위로, 열 돌리기(--진행시키기)
# 밑에서 부터 올라가야한다!!
row = len(strA)
col = len(strB)

# 글자 다 채울 때까지 실행
while len(ans) < ans_len:
    # 값이 좌측에서 온 것이면,
    if table[row][col] == (table[row][col-1]):
        col -= 1
        continue
    
    # 위에서 온것이면,
    if table[row][col] == table[row-1][col]:
        row -= 1
        continue
    
    # 대각선 방향에서 왔으면 그 글자다!
    if table[row][col] == table[row-1][col-1] + 1:
        # 현재 행은 인덱스에 1이 추가되어있음
        row -= 1
        col -= 1
        ans.append(strA[row])
        # 다음행으로
        continue


# 역순 출력
print("".join([ans[i] for i in range(len(ans)-1,-1,-1)]))