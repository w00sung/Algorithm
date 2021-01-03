import sys
read = sys.stdin.readline

N_number, Len, Limit = map(int,read().rstrip().split())

nums = list(map(int, read().rstrip().split()))

nums.sort()

# 가장 큰 2개만 사용한다.
first = nums.pop()
second = nums.pop()

cnt = 1
ans = 0
while cnt <= Len:

    if cnt % (Limit + 1) == 0:
        ans += second
    
    else:
        ans += first
    
    cnt += 1
    
print(ans)