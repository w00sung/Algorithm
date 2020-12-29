import sys
read = sys.stdin.readline

# while True:
#     li = list(map(int,read().rstrip().split()))
    
#     if li[0] == 0:
#         break

#     visited = [True] * (li[0])

    
def recur(i, N):

    if i == N:
        visited[i] = True
        print(li[i])

    visited[i] = True
    print(li[i])
    recur(i+1)
    visited[i] = False