## 왜 작동되는지 증명하지 못했다.
## 그냥 된다. 뭐지? 
## --> 앞전에 이미 만들어 놓은 것이 있기 때문에 가능하다고 가정

import sys
read = sys.stdin.readline
coins = list(map(int,read().rstrip().split()))
coins.sort()

target = 1
for c in coins:
    
    # 더할 때 c의 생각 : 나는 target - 1 까지 구할 수 있어 !
    # 이미 존재하는 숫자들에 본인만 얹으면 됨

    if target >= c:
        target += c

    # tatget은 나를 얹어서 만들 수 있는 숫자보다 큰 숫자다
    else:
        break

print(target)