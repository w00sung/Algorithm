import heapq
import sys
read = sys.stdin.readline

n = int(read())

heap = []
def heap_command(n):

    if n == 0:
        if len(heap) == 0:
            print(0)

        else:
            k = heapq.heappop(heap)[1]
            print(k)

    else:
        # -n을 넣어줌으로써 최대 힙 처리
        heapq.heappush(heap,(-n,n))



for _ in range(n):
    heap_command(int(read().rstrip()))