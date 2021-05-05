import sys
read = sys.stdin.readline

num = int(read())
calc = list(map(int,read().rstrip()))

# print(calc)
print(sum(calc))