from itertools import combinations as combi
import sys
read = sys.stdin.readline

N, limit = map(int, read().rstrip().split())
cards = list(map(int,read().rstrip().split()))

cards_sum = set(map(sum,list(combi(cards,3))))

diff = float('inf')
res = 0
for s in cards_sum:
    tmp = limit - s
    if tmp >= 0 and tmp < diff:
        diff = tmp 
        res = s

    if res == limit :
        break

print(res)