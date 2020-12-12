import sys
read = sys.stdin.readline

n = int(read())
li = []
for _ in range(n):
    r = int(read())
    li.append(r)

li.sort()

print("\n".join([strs(num) for num in li]))
# 