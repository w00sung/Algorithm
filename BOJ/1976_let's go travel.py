import sys
read = sys.stdin.readline

N = int(read())
T = int(read())

parent = [0] * (N+1)
level = [1] * (N+1)

for i in range(N+1):
    parent[i] = i

def find(n):
    if n == parent[n]:
        return n

    parent[n] = find(parent[n])
    return parent[n]

def merge(a, b):
    a = find(a)
    b = find(b)

    if a == b:
        return

    if (level[a] > level[b]):
        a,b = b,a

    parent[a] = b

    if level[a] == level[b]:
        level[b] += 1

for i in range(N):
    li = list(map(int,read().rstrip().split()))
    if i != N-1:
        for j in range(i+1,N):
            if li[j] == 1:
                merge(i+1,j+1)

travel_li = list(map(int,read().rstrip().split()))
tmp = find(travel_li[0])
for city in travel_li:
    if find(city) != tmp:
        print("NO")
        exit()

print("YES")
    