



cnt = 0
# i : 현재 행, col : 내가 지나간 col
def n_queen(i, col):
    global cnt

    
        # 모든 행에 다 넣었으면,
        if ( i == n ):
            cnt += 1

        else:
            # 다음 행에 같은 행위
            n_queen(i+1,col)