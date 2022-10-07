n = int(input())
graph = [list(map(int,input())) for _ in range(n)]
res=[]
def dfs(x,y,n):
    now = graph[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if graph[i][j] != now:
                res.append('(')
                dfs(x,y,n//2)   #2사분면
                dfs(x,y+n//2,n//2)  #1사분면
                dfs(x+n//2,y,n//2)  #3사분면
                dfs(x+n//2,y+n//2,n//2) #4사분면
                res.append(')')
                return
    if now == 1 :
        res.append('1')
    else:
        #res.append(0)
        res.append('0')


dfs(0,0,n)
print(''.join(res))









#def f(x):
#    for i in range(x):
#        for j in range(x):
#
#            if 0<= i <= (x//2)-1 and 0<= j <=(x//2)-1:
#                if graph[i][j]==0:
#
#                elif graph[i][j]==1:
#            else:
#                return f(x // 2)
#
#
#            if 0 <= i <= (x // 2) - 1 and x//2 <= j <= x - 1:
#                if graph[i][j] == 0:
#                elif graph[i][j] == 1:
#            else:
#                return f(x // 2)
#
#
#            if x//2 <= i <= x-1 and 0 <= j <=(x//2)-1:
#                if graph[i][j]==0:
#                elif graph[i][j]==1:
#            else:
#                return f(x // 2)
#
#
#            if x//2 <= i <= x-1 and x//2 <= j <= x-1:
#                if graph[i][j]==0:
#                elif graph[i][j]==1:
#            else:
#                return f(x // 2)
#
#print(f(n))