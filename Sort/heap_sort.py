import heapq
import sys
read = sys.stdin.readline

heap = []
n = int(read())
for _ in range(n):
    heapq.heappush(heap,int(read()))

for _ in range(n):
    print(heapq.heappop(heap))