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

for i in range(len(letters)-1, -1,-1):

    stack.append(letters[i])

    if len(stack) >= len(bomb) and letters[i] == bomb[0]:
        # print("check!", stack[-bomb_len:], bomb[::-1])
        if stack[-bomb_len:] == bomb[::-1]:
            # print(stack)
            for i in range(bomb_len):
                stack.pop()
if stack:
    print("".join(stack[::-1]))
else:
    print("FRULA")
