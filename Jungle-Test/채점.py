"#정답
import sys
read = sys.stdin.readline

size = int(read())
board = []
# 남북동서
da = [1, -1, 0, 0]
db = [0, 0, 1, -1]

for i in range(size):
    a = read().rstrip()
    a = list(a)
    board.append(list(map(int, a)))


stack = []
for r in range(size):
    for c in range(size):
        if board[r][c] == 1:
            stack.append([r, c])


countlist = []


def DFS(a, b):
    if board[a][b] == 0:
        return
    count = 0
    DFSStack = [[a, b]]
    while DFSStack:
        a, b = DFSStack.pop()
        if board[a][b] == 0:
            continue
        board[a][b] = 0
        count += 1
        for t in range(4):
            na = a + da[t]
            nb = b + db[t]
            if -1 < na < size and -1 < nb < size and board[na][nb] == 1:
                DFSStack.append([na, nb])

    countlist.append(count)


for i in stack:
    DFS(i[0], i[1])

countlist.sort()
print(len(countlist))
for i in countlist:
    print(i)
"