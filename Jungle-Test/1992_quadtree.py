import sys
read = sys.stdin.readline

n = int(read())
arr = []
for _ in range(n):
    # 문자열로 받는다.
    arr.append(list((read().rstrip())))

ans = ''
def dfs(arr,x,y,n):
    global ans
    brk = False
    # ans += '('
    check = arr[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            # 압축불가 등장
            if arr[i][j] != check:
                
                n = n // 2
                ans += '('
                
                dfs(arr,x,y,n)
                dfs(arr,x,y+n,n)
                dfs(arr,x+n,y,n)
                dfs(arr,x+n,y+n,n)

                ans += ')'
                brk = True
                break


        if brk == True:
            break
            
    # 통과 됐음
    if brk == False:
        ans += check
    
    
dfs(arr,0,0,n)
print(ans)