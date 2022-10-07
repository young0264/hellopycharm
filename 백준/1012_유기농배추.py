import sys
sys.setrecursionlimit(10**6)
def dfs(x,y): #x,y위:1. 2차원배열을 4사분면 그래프처럼
    # 표현하는경우 좌표로 (x,y) ==> 배열 [y][x]임을 꼭 기억할것

    if (x<=-1 or x>m or y>n or y<=-1 ):
        return False
    if arr[y][x]==1:
        arr[y][x]=0
        dfs(x-1,y) #좌
        dfs(x+1,y) #우
        dfs(x,y+1) #상
        dfs(x,y-1) #하
        return True
    return False

t = int(input())
for _ in range(t):
    m, n, k = map(int,input().split())
    arr = [[0]*(m+1) for _ in range(n+1)]
    box=[]
    num=0
    d=0
    for i in range(k):
        a,b = map(int,input().split())
        arr[b][a] = 1
   # if dfs(a,b)==True:
   #     d+=1 #덩어리 갯수 d
    for i in range(m):
        for j in range(n):
            if dfs(i,j)==True:
                d+=1

    print(d)


