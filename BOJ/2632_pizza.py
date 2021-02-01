import sys
read = sys.stdin.readline

size = int(read().rstrip())
A_sum_li = [0] * (size+1)
B_sum_li = [0] * (size+1)
A_li = []
B_li = []
A, B = map(int,read().rstrip().split())

for i in range(A):
    A_li.append(int(read()))

for i in range(B):
    B_li.append(int(read()))

s = 0
for i in range(len(A_li)):
    idx = i
    s = 0
    while True:
        s += A_li[idx]
        if s > size:
            break
        A_sum_li[s] += 1
        idx += 1
        if idx == len(A_li):
            idx = 0
        # circular - 한번만
        if idx == i:
            if i > 0:
                A_sum_li[s] -= 1
            break

for i in range(len(B_li)):
    idx = i
    s = 0
    while True:
        s += B_li[idx]
        if s > size:
            break
        B_sum_li[s] += 1
        idx += 1
        if idx == len(B_li):
            idx = 0
        
        # circular - 한번만
        if idx == i:
            if i > 0:
                B_sum_li[s] -= 1
            break

cnt = 0
cnt += (A_sum_li[size]+B_sum_li[size])
for i in range(1,size):
    if A_sum_li[i] and B_sum_li[size-i]:
        cnt += (A_sum_li[i] * B_sum_li[size-i])

print(cnt)

# print(A_sum_li)
# print(B_sum_li)
