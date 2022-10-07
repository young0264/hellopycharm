
import sys
sys.setrecursionlimit(60000)
def dfs(x,y):
    if x<=-1 or x>=a or y<=-1 or y>=b:
        return False
    if graph[y][x] == 1:
        graph[y][x] = 0      #땅을바다로 #방문처리
        dfs(x + 1, y)
        dfs(x - 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)
        dfs(x + 1, y - 1)
        dfs(x + 1, y + 1)
        dfs(x - 1, y - 1)
        dfs(x - 1, y + 1)
        return True

        #dx = [1,-1,0,0,1,-1,1,-1]
        #dy = [0,0,1,-1,1,-1,-1,1]
        #for i in range(8) :
        #    dfs(dx[i],dy[i])
        #   return True
    return False

while True:
    result = 0
    graph = []

    a,b = map(int,input().split())
    if (a,b) == (0,0) :
        break
    for i in range(b):
        graph.append(list(map(int,input().split())))
    #print(graph)
    for i in range(b):  #y좌표
        for j in range(a):  #x좌표
            if dfs(j,i) == True:
                result += 1
    #print(graph)
    print(result)





















#import sys
#sys.setrecursionlimit(60000)
#
#def dfs(x,y):
#    #if -1>=x or x>=a or -1>=y or y>=b :
#    if not (0 <= x < a and 0 <= y < b):
#        return False
#    if matrix[x][y] == 1 :
#        matrix[x][y] = 0
#        dfs(x + 1, y)
#        dfs(x - 1, y)
#        dfs(x, y + 1)
#        dfs(x, y - 1)
#        dfs(x + 1, y - 1)
#        dfs(x + 1, y + 1)
#        dfs(x - 1, y - 1)
#        dfs(x - 1, y + 1)
#
#        return True
##result=0 #여기에 있으면 testcase마다 초기화가 이루어지지 않습니다.
#
#while True:
#    b,a =map(int,input().split()) #col,row순으로 input이 들어옴
#    result = 0
#    if a==0 and b==0 : break
#    matrix = [list(map(int, input().split())) for i in range(a)]
#
#    for i in range(a):
#        for j in range(b):
#            #if dfs(j,i) == True:
#            if not matrix[i][j]: continue #matrix가 False라면
#            dfs(i,j)
#            result+=1
#    print(result)