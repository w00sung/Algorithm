import sys
read = sys.stdin.readline


n = int(read().rstrip())
stick = []

for _ in range(n):
    stick.append(int(read().rstrip()))

# 내가 보이니까 기본값 1
cnt = 1
crtria = stick.pop()

# 2번째까지만 진행하면됨 
# 1번째는 pop 할게없다
for _ in range(n-1):
    nxt = stick.pop()
    if nxt > crtria:
        cnt += 1
        # 기준 바꿔준다.
        crtria = nxt

    else:
        continue

print(cnt)