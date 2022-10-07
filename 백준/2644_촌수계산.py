#실버2 쉬운dfs 1시간넘게걸림
#visited 0 이 방문안한거. True가 방문한거면 재귀의 깊이를 visited에다가 저장해줌
import sys
sys.setrecursionlimit(10**6)
num = int(input())
a , b = map(int,input().split())
n = int(input())
family = [[] for _ in range(num+1)]
for i in range(n):
    x , y = map(int,input().split())
    family[x].append(y)
    family[y].append(x)
#print(family)
visited = [0]*(num+1)
def dfs(x,y): #x 자리에 a>> 그리고 y(b)를찾을꺼야
    for i in family[x]:  #family[7]=2
        if visited[i]==0:          #family[2]
            visited[i] = visited[x]+1
            if i == y:
                print(visited[x]+1)
                exit(0)
            dfs(i,y)
       #위아래위치
    return False
if not dfs(a,b):
    print(-1)
