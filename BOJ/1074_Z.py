import sys
read = sys.stdin.readline

# n = int(read())
n,r,c = map(int,read().rstrip().split())
# 2^n 의 행렬 count 먹이기

def count(n,r,c):
    if n == 0:
        return 0
    idx = 2**(n-1)
    k = idx ** 2
    # A,B,C,D 0을 할지, 1을 할지 열로 검증
    res = k if c >= idx else 0
    # 2를 더할지, 더하지 않을지 행으로 **바로** 검증
    res += 2*k if r >= idx else 0
    
    # idx 로 나눠줘도, 앞에 행, 열은 영향받지 않는다.
    return res + count(n-1,r%idx,c%idx)
print(count(n,r,c))

   
