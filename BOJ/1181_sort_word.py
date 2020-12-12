import sys
read = sys.stdin.readline

n = int(read())
li = []
for _ in range(n):
    word = read().rstrip()
    li.append(word)

# sort는 단순 앞글자로 비교한다.
li.sort()
print(li)

