## 다시 하자!

import sys
read = sys.stdin.readline

# 끝에서부터 팝하면 좋은 점은 ?!
# 문자열의 길이가 줄어드는 것이 반영된다!
# 그 때는 아니었는데, 줄어들고 나면 다시 체크할 수 있게 된다!

letters = read().rstrip()
stack = []
bomb = list(read().rstrip())
bomb_len = len(bomb)

# del list[2:] -> idx 2 이후 모두 pop

for ltr in letters:
    # 일단 순서대로 삽입
    stack.append(ltr)

    # 폭발물 가능성
    if len(stack) >= len(bomb) and ltr == bomb[-1] :
        # print("stack : ",stack[-bomb_len:])
        # print("bomb : ",bomb[:])
        if stack[-bomb_len:] == bomb :
            del stack[-bomb_len:]

if stack :    
    print("".join(stack))
else:
    print("FRULA")
