from collections import deque
import sys
read = sys.stdin.readline

n = int(read())
queue = deque(range(1,n+1))

while True :
    if len(queue) == 1:
        break
    queue.popleft()
    queue.append(queue.popleft())

print(queue[0])