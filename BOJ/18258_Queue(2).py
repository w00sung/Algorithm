from collections import deque
import sys
read = sys.stdin.readline

queue = deque()

def queue_command(command):

    command = command.split()
    
    if command[0] == "push":
        queue.append(int(command[1]))

    elif command[0] == "pop":
        if queue:
            p = queue.popleft()
            print(p)
        else:
            print(-1)

    elif command[0] == "size":
        print(len(queue))

    elif command[0] == "empty":
        if queue:
            print(0)
        else:
            print(1)

    elif command[0] == "front":
        if queue:
            print(queue[0])
        else:
            print(-1)

    elif command[0] == "back":
        if queue:
            print(queue[len(queue)-1])
        else:
            print(-1)

n = int(read())

for _ in range(n):
    queue_command(read().rstrip())