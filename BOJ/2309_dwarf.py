import sys
read = sys.stdin.readline


dw_height = []
for _ in range(9):
    dw_height.append(int(read()))

dw_sum = sum(dw_height)
y = True
i= 0
while y:
    for j in range(i+1,len(dw_height)):
        if dw_height[i] + dw_height[j] == dw_sum - 100:
            fst = dw_height[i]
            snd = dw_height[j]
            y = False
    i += 1
dw_height.remove(fst)
dw_height.remove(snd)
dw_height.sort()
for i in dw_height:
    print(i)
        