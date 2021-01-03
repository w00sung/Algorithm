import sys
read = sys.stdin.readline


num = list(map(int,read().rstrip()))

# ans를 더하고 곱하고 
ans = num[0]
for i in range(1,len(num)):
    
    # 전에 것이랑 더한 것과 곱한 것 중 큰것 선택 !!!
    ans = ans + num[i] if ans + num[i] > ans * num[i] else ans * num[i]


print(ans)
