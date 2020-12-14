
n = 4
num = [ i for i in range(1,n+1)]
use = [True] * len(num)
res = ""

def nm
    for i in range(n):
        cnt = 0
        for n in num:
            if use[i] == True:
                res += num[i]
                cnt += 1
            
            if cnt == 3:
                print(res)