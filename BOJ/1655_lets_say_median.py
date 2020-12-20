import heapq
import sys
read = sys.stdin.readline

heap_left = []
heap_right = []


# 가운데에 중앙값이 유지되어야 시간복잡도가 해결됨
def heap_command(num):

    # 아무것도 없으면    
    if not heap_left:
        heapq.heappush(heap_left,((-1)*num,num))
        print(num)
        return


    medi = heap_left[0][1]

    if num > medi:
        heapq.heappush(heap_right,num)

    # median 대체 // pop시킬 때 마지막 값 나오게 하기 위해서 최대 힙으로 저장
    elif num <= medi:
        heapq.heappush(heap_left,((-1)*num,num))

    # +1 : 4 2 일 때만 오른 쪽으로 값 빼기 // 3 2 일 때는 그대로 유지 
    if len(heap_left) > len(heap_right) + 1:
        move = heapq.heappop(heap_left)[1]
        heapq.heappush(heap_right,move)

    # +1 없음 : -- 2 4 일때 + 2 3 일 때 도
    elif len(heap_left) < len(heap_right):
        move = heapq.heappop(heap_right)
        heapq.heappush(heap_left,((-1)*move,move))
    
    # 최댜 합임
    print(heap_left[0][1])

n = int(read())

for _ in range(n):
    heap_command(int(read().rstrip()))