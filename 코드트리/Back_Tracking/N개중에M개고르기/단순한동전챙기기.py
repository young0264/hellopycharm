#무조건 세개구나
import sys
sys.setrecursionlimit(10**6)
n = int(input())
m = 3
f = [list(map(str,input())) for _ in range(n)]  #f
graph = [[0]*n for _ in range(n)]
coin_num = 9
INT_MAX = sys.maxsize
coin_pos = []   #숫자가 있는 위치
combination_num = []   #combinations
start = (-1,-1)
end = (-1,-1)
answer = INT_MAX #?

def dist(a,b):  #a와 b지점간의 거리
    (ax,ay) , (bx,by) = a , b
    return abs(ax-bx) + abs(ay-by)

def calc(): #총이동거리 return
    start_move = dist(start,combination_num[0])
    for i in range(m-1):
        start_move += dist(combination_num[i],combination_num[i+1])
    start_move += dist(end,combination_num[-1])
    return start_move

#내가해야될건 selected에 1~3의 숫자의 조합을 저장하기.
ans = INT_MAX
def dfs(curr_idx,flag):
    global ans
    if flag == m :  #3개의 동전을 택한것
        ans = min(ans,calc())
        return
    if curr_idx == len(coin_pos):
        return

    dfs(curr_idx+1,flag)
    combination_num.append(coin_pos[curr_idx])
    dfs(curr_idx+1,flag+1)
    combination_num.pop()

#숫자위치를 coin_pos에 넣기
for num in range(1,10): #동전의 1의 위치부터 넣기위함
    for i in range(n):
        for j in range(n):
            if f[i][j] == '.':
                graph[i][j] = 0
            elif f[i][j] == 'S':
                start = i,j
            elif f[i][j] == 'E':
                end = i,j
            else:
                if num == int(f[i][j]):
                    coin_pos.append((i, j)) #동전을 오름차순으로 넣어줌
dfs(0,0)

if ans == INT_MAX:
    ans = -1

print(ans)

#graph = [[0]*n for _ in range(n)]
#visited = [[0]*n for _ in range(n)]
#dx,dy = [1,-1,0,0],[0,0,1,-1]
#def in_range(x,y):
#    return 0<=x<n and 0<=y<n
#def find(x):
#    for i in range(n):
#        for j in range(n):
#            if f[i][j] == x:
#                return (i,j)
#s1,s2 = find('S')
#e1,e2 = find('E')
#f[s1][s2] = '.'
#f[e1][e2] = '.'
#for i in range(n):
#    for j in range(n):
#        if f[i][j] == '.':
#            graph[i][j] = 0
#        else: graph[i][j] = int(f[i][j])
#
#def dfs(x,y,flag,depth):
#    global e1,e2
#    if flag == 3 and x == e1 and y == e2 :   #최소3개래
#        print(depth)
#        exit(0)
#    for i in range(4):
#        nx , ny = x+dx[i], y+dy[i]
#        if in_range(nx,ny) and visited[nx][ny]==0:
#            if graph[nx][ny]:
#                flag += 1
#                graph[nx][ny] = 0
#            visited[nx][ny] = 1
#            dfs(nx,ny,flag,depth+1)
#dfs(s1,s2,0,0)

