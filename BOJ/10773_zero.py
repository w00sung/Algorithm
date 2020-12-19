import sys
read = sys.stdin.readline


acnt = []
tot = 0
def write(x):
    global tot

    if x == 0:
        err = acnt.pop()
        tot -= err

    else:
        acnt.append(x)
        tot += x


k = int(read())
for _ in range(k):
    write(int(read().rstrip()))

print(tot)
