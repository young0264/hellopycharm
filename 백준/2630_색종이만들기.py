#쿼드(4)로 쪼개지는 구조이다. 시작점을 4가지로 나누어 경우를 생각하고(dfs들어감)
#재귀로 들어가는 것들의 범위(시작,끝,변의값) 설정에 유의한다.


import sys
sys.setrecursionlimit(10**6)
n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]


wcnt = 0
bcnt = 0
def dfs(x,y,n):
    global wcnt,bcnt
    check = graph[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if check != graph[i][j]:
                dfs(x,y,n//2)   #2
                dfs(x,y+n//2,n//2)  #1
                dfs(x+n//2,y,n//2)  #3
                dfs(x+n//2,y+n//2,n//2) #4
                return
            #저기 안들어간거면
    if check == 0 :
        wcnt += 1
        return
    elif check == 1:
        bcnt += 1
        return
dfs(0,0,n)
print(wcnt)
print(bcnt)



#for x in range(n):
#    for y in range(n):
#        if dfs(x,y)==True:
#            answer += 1
#print(answer)