import sys
read = sys.stdin.readline

# n = int(read())
n,r,c = map(int,read().rstrip().split())
# 2^n 의 행렬 count 먹이기

def count(n,r,c):
    if n == 0:
        return 0
    idx = 2**(n-1)
    if r >= idx and c>= idx:
        k = 3
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
    
    return idx*idx*k + count(n-1,r,c)
print(count(n,r,c))

   
