from collections import deque
import sys
read = sys.stdin.readline

n, m = map(int,read().rstrip().split())

queue = deque(range(1,n+1))
josephus = []

while queue:
    if m > 1:
        for _ in range(m-1):
            # n-1개는 밑으로 보낸다.
            queue.append(queue.popleft())
        
    josephus.append(queue.popleft())

print("<",end="")
for i in range(n):
    if i == n-1:
        print("{}>".format(josephus[i]),end ="")
    else:
        print("{}, ".format(josephus[i]), end ="")
