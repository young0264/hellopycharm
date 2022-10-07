n , m = map(int,input().split())
graph=[list(map(int,input().split())) for _ in range(n)]
happy = 0
for i in range(n):  #가로탐색
    cnt = 1
    for j in range(1,n):
        if graph[i][j-1] == graph[i][j]:
            cnt += 1
    if cnt >= m:
        happy += 1

for j in range(n):
    cnt = 1
    for i in range(1,n):
        if graph[i-1][j] == graph[i][j]:
            cnt += 1
    if cnt >= m :
        happy +=1
print(happy)





#for i in range(n):
#    X=False
#    for j in range(n-1):
#        if graph[i][j] == graph[i][j+1]:
#            #graph[i][j],graph[i][j+1] = 0,0
#            X=True
#            continue
#    if X==True:
#        cnt+=1
#for i in range(n-1):
#    x=False
#    for j in range(n):
#        if graph[i][j] == graph[i+1][j]:#조건이 충족되면 하위 for문을 그냥 탈출하는방법?
#            #graph[i][j],graph[i+1][j] = 0,0
#            x=True
#            continue
#    if x==True :
#        cnt+=1
#print(cnt)