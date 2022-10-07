def dfs(x,y):
    global k
    if x <= -1 or x >= n or y >= n or y <= -1 :
        return False
    if arr[x][y]==1:
        arr[x][y]=0 #방문처리
        k+=1
        dfs(x-1,y) #좌
        dfs(x+1,y) #우
        dfs(x,y+1) #상
        dfs(x,y-1) #하
        #box.append(k)
        return True
    return False

n = int(input())
arr=[]
box=[]
for _ in range(n):
    arr.append(list(map(int,input())))
result=0    #덩어리의 횟수
k=0         #각 덩어리의 요소들 갯수
for i in range(n):
    for j in range(n):
        if dfs(i,j)==True:
            result+=1
            box.append(k)
            k=0

print(result)
box.sort()
print(box.sort())
for i in range(len(box)):
    print(box[i])
