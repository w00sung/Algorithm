import sys

read = sys.stdin.readline
num = int(read())

fibo = [-1] * (num+1)

# fibo[0] = 0
# fibo[1] = 1


###### Bottom - Up ########
# for i in range(2,num+1):
#     fibo[i] = fibo[i-2] + fibo[i-1]

# print(fibo[num])
###########################

####### Top - Down ########

def fibo_dp(num):
    if num == 0:
        return 0

    if num == 1:
        return 1

    # 왔었냐 ?
    if fibo[num] != -1:
        return fibo[num]

    # 안왔으면 앞에 녀석들로 구해봐!
    fibo[num] = fibo_dp(num-2) + fibo_dp(num-1)
    return fibo[num]
##############################

fibo_dp(num)
print(fibo[num])