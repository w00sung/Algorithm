import sys
read = sys.stdin.readline

# n = int(read())
n,r,c = map(int,read().rstrip().split())
# 2^n 의 행렬 count 먹이기

def getCount(n,r,c):
    cnt = 0

    while n > 0:
        idx = 2**(n-1)
        if r >= idx and c>= idx:
            k = 3
            # 4로 나누는게 아니라, idx로 나눈다.
            r %= idx
            c %= idx
        elif r >= idx and c< idx:
            k = 2
            r %= idx
        elif r < idx and c>= idx:
            k = 1
            c %= idx
        else:
            k = 0
        
        cnt += idx*idx*k
        n -= 1    

    return cnt

print(getCount(n,r,c))
   
