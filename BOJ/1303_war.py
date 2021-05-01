import sys
read = sys.stdin.readline

N, M = map(int,read().rstrip().split())
field = []
for _ in range(M):
    field.append(list(read().rstrip()))

def dfs(x,y,flag,color,depth):

    # 최대 깊이 알아내는 방법 고안!
    # depth를 return 하면 ?! 최종 녀석의 depth가 return 값이 될 것이다.

    for dx, dy in (-1,0),(1,0),(0,-1),(0,1):   
        move_x = x+dx
        move_y = y+dy
        if move_x < 0 or move_x >= M or move_y < 0 or move_y >= N:
            continue
        
        if flag[move_x][move_y] and field[move_x][move_y] == color:
            flag[move_x][move_y] = False
            color_dict[color] += 1
            depth = dfs(move_x,move_y,flag,color, depth+1)
    
    return depth


flag = [[True]*N for _ in range(M)]
color_dict= {"W":0,"B":0}
ans=[0,0]

for i in range(M):
    for j in range(N):
        if flag[i][j]:
            color = field[i][j]
            color_dict[color] = 1
            flag[i][j] = False
            # print("FINISH DFS",dfs(i,j,flag,color,1))
            depth = dfs(i,j,flag,color,1)
            if color == "W":
                ans[0] += depth**2
            else:
                ans[1] += depth**2

print(*ans)
