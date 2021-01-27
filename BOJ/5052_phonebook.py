import sys
read = sys.stdin.readline


def insert(num, dic):
    cur = dic
    for n in num:

        # 안들어있으면 들어간다.
        if n not in cur:
            cur[n] = {}
        # 있으면 들어가기 or 들어가서 넣었으면 또 들어가기
        cur = cur[n]
        # 지금 내가 누군가의 마지막에 있다면?
        if '#' in cur:
            return False

    # 나는 마지막인데, 뒤에 더 있으면? (내가 접두사)
    if len(cur):
        return False

    # 마지막 NULL 삽입
    cur['#'] = {}
    return True


N = int(read())
for i in range(N):
    flag = True
    dic = {}
    cnt = int(read())
    for i in range(cnt):
        # 이미 false 였으면 버린다.
        if not flag:
            read()
            continue

        num = list(read().rstrip())

        flag = insert(num, dic)

        # flag가 false가 되어도 꾹 참고 다 입력받아야한다.
        # if not insert(num, dic):

        #     flag.append(False)

    # if len(flag):
    #     print("NO")
    # else:
    #     print("YES")
    if flag:
        print("YES")
    else:
        print("NO")

# print(dic)
