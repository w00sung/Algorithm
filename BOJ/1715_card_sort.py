import heapq
import sys
read = sys.stdin.readline


heap = []

def count(card_heap):
    tot = 0
    n = len(card_heap)

    if n == 1:
        return 0

    # n번째에서는 나밖에 안남음
    for _ in range(n-1):
        # 지금 단계에서 가장 작은 2개를 골라야 한다.
        a = heapq.heappop(card_heap)
        b = heapq.heappop(card_heap)
        

        tot += (a+b)
        # 다시 넣어줘서 비교할 수 있게 해준다.
        heapq.heappush(card_heap,a+b)


    return tot

k = int(read())

for _ in range(k):
    heapq.heappush(heap, int(read().rstrip()))

print(count(heap))