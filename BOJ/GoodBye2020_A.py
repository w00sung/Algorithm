import sys
read = sys.stdin.readline

N = int(read())

palindroms = list((read().rstrip().split()))

for i in range(1,N):

    # 뒷 글자의 맨 앞자리 vs 앞글자의 맨 뒷자리
    if palindroms[i-1][-1] != palindroms[i][0]:
        print(0)
        exit()

print(1)