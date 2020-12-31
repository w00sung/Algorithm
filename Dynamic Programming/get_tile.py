

# tile -- 점화식

num = 3
d = [0] * (num+1)
# 가로가 1 or 2 일 때,
d[1] = 1
d[2] = 3

# S(n) = S(n-1) + 2 * S(n-2)

# 점화식 표현
for i in range(3,num+1):
    d[i] = d[i-1] + 2*d[i-2]

print(d[num]) 