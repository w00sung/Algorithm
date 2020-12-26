import sys
read = sys.stdin.readline


n = int(read())
# n+1개 만들자 -- 0번째 비어있고, 1번째는 무조건 빈 것 유지

tree =[[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int,read().rstrip().split())
    
    
    # 1은 항상 a에만 있다.
    if b == 1:
        a, b = b, a
    
    # 1을 받았는데, 이미 차있다면?
    # 그 전에 부모관계를 몰라서 넣어놓은 것
    if a == 1 and tree[b] :

        # print("나 모르고 넣었습니다.",tree[b])
        # 바꿔주기
        tree[tree[b].pop()].append(b)    
        # b에는 1을 넣어준다.
        tree[b].append(a)
   
    # 1받는 것 작업!
    # a에 부모가 존재하면,
    elif a == 1 or tree[a] :
        # b에 부모 a를 넣는다.
        tree[b].append(a)
    
    # b에 부모가 존재하면,
    elif tree[b] :
        # a에 부모 b를 넣는다.
        tree[a].append(b)
    
    # 부모가 누군지 모르는 경우
    # 일단 b에 넣는다.
    else:
        tree[b].append(a)


for i in range(2,n+1):
    print(*tree[i])