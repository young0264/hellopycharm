import sys
sys.setrecursionlimit(60000)

matrix = [list(map(str,input().split())) for _ in range(5)]
result=set()
def dfs(x,y,start) : #start를 따로 0으로 하면 str형을 붙이기가 힘든데
                        #이렇게 설정된 start는 초기화도안햇는데 뭐라고 말해야하지
    if len(start)==6:
        result.add(start)
        return
    if x>4 or x<=-1 or y>4 or y<=-1:#범위밖
        return #다시 되돌아간다?
    start += matrix[x][y]
    dfs(x+1,y,start)#우
    dfs(x-1,y,start)#좌
    dfs(x,y+1,start)#상
    dfs(x,y-1,start)#하

for i in range(5):
    for j in range(5):
        dfs(i,j,"") #여기에서 출발햇을때의 Dfs가 start에 담김
print(len(result))

















#모든노드를 돌면서
#거기에서 6개의 노드를 보고 str형태로 6자리를만든후 배열에 저장해서
#set으로 중복없앤후에 갯수를 print하면 되겟다 하는데
#num=0
#def dfs(x,y):
#    global num
#    if len(num)==6:
#        if num not in result:
#            result.append(num)
#        return
#
#    dx=[1, -1, 0, 0]
#    dy=[0, 0, 1, -1]
#    for k in range(4)
#
#
#    num += arr[x][y]
#    if x<=-1 or x>5 or y<=-1 or y>5:
#        return False
#    else:
#        dfs(x+1,y) #우
#        dfs(x-1,y) #좌
#        dfs(x,y+1) #상
#        dfs(x,y-1) #하
#
#
#
#result=[]
#arr=[]
#for i in range(5):
#    arr.append(list(map(str,input().split())))#문자형으로 받고 +더하기.
#
#for i in range(5):
#    for j in range(5):
#        arr[i][j]
#print(aray)



#import sys
#sys.setrecursionlimit(300000)
#
#def dfs(y,x,start):
#    start += graph[y][x]
#    if len(start) == 6 :
#        result.add(start)
#        return ; #뭐야이건
#    for dy,dx in d:
#        Y,X=y+dy,x+dx
#        if (0<=Y<5) and (0<=X<5):
#            dfs(Y,X,start)
#
##graph=set([])
##for i in range(5):
##    graph.append(list(map(str,input().split())))
#graph=[list(map(str,input().split())) for _ in range(5)]
#d=[(-1,0),(1,0),(0,-1),(0,1)]
#result=set()
#for i in range(5):
#    for j in range(5):
#        start=""
#        dfs(i,j,start)
#print(len(result))
#

