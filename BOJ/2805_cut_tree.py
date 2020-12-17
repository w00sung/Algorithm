import sys
read = sys.stdin.readline

n, want_sum = map(int,read().rstrip().split())
trees = list(map(int,read().rstrip().split()))

# 지금 자른 나무_합
def sum_cut(trees,cutter):
    sum_tree = 0
    for tree in trees:
        if tree > cutter:
            sum_tree += tree - cutter
    
    return sum_tree

# 적어도 m 미터 !!
# trees: 나무들, want_sum: 원하는 cutting 길이, strt,end : 0부터 최대치까지
def binary_search(trees, want_sum, strt,end):

    # 최대한 좁힌 후 그 놈을 뽑는다.
    while strt <= end:
    
        cutter = (strt+end) // 2
        now_sum = sum_cut(trees,cutter)
        # 잘린 나무길이의 총합 == cut 그만
        if now_sum == want_sum:
            return cutter

        # 자른 값이 크면, 커터 높여야 됨
        elif now_sum > want_sum:
            
            strt = cutter + 1
            
        # 자른 값이 작으면, 커터 낮춰야 됨
        else:
            end = cutter - 1
    
    # "적어도" -- 
    # 합이 커진 상태로 나오면 그놈 그대로
    if now_sum >= want_sum:
        return cutter
    # 합이 작아진 상태로 나오면 커터 1개 낮추기
    else:

        return cutter-1


print(binary_search(trees,want_sum,0,max(trees)))

