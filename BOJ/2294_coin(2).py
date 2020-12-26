from collections import deque
import sys
read = sys.stdin.readline


N, K = map(int, read().rstrip().split())
coin = []
for _ in range(N):
    coin.append(int(read()))

# 정렬하고 맨 위부터 쭉 ?
coin.sort(reverse=True)
    
def bfs(coin,want):
    