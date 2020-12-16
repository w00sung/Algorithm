import sys
read = sys.stdin.readline

n = int(read())
R = n
new_n = -1
cnt = 0
while True:
    if new_n == R:
        break
    
    
    # 앞자리수
    front = n // 10
    # 뒷자리수
    back = n % 10
    # 합
    add = front + back

    new_n = back*10 + (add%10)
    cnt += 1
    n = new_n

print(cnt)