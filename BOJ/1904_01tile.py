import sys
read = sys.stdin.readline
# sys.setrecursionlimit(10**9)

N = int(read())


# A(n) = A(n-2) + A(n-1)

##### Bottom  - Up ######
tile = [0] * (1000001)

tile[1] = 1
tile[2] = 2

if N >= 3:
    for i in range(3,N+1):
        tile[i] = (tile[i-2] + tile[i-1]) % 15746

print(tile[N])


##### Top - Down #######
### ERROR #####

# def get_tile(num):

#     if num == 1:
#         return 1
    
#     if num == 2:
#         return 2

#     # 이미 저장되어 있으면 불러와라 !!
#     if tile[num] != 0:
#         return tile[num]

#     tile[num] = ((get_tile(num-2)) % 15746) + ((get_tile(num-1)) % 15746)
#     return tile[num]

# print(get_tile(N))