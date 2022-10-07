
#1.중복제거를 위해 배열 하나를 더 만들어 해당 배열에 같은 값이 없을때만 넣어주는 방식으로
# 같은 자릿수에, 이전에 사용한 숫자가 있다면
n, m = map(int,input().split())
arr = sorted(list(map(int,input().split())))
pre_list =[0]*n
res = []
def dfs(box):
    if len(box) == m :
        res.append(list(box))
        return
    for i in range(n):
        if pre_list[i] == False:
            pre_list[i] = True
            #box.append(arr[i])
            dfs(box+[arr[i]])
            #box.pop() #재귀 실행후에 pop?
            pre_list[i] = False
dfs([])
for i in sorted(list(set(map(tuple,res)))): #리스트제거가능
    print(*i)

    #틀린거
#n , m = map(int,input().split())
#arr = sorted(list(map(int,input().split())))
#res = []
#pre = 0
#def dfs(box):
#    global pre
#    if len(box) == m:
#        res.append(box)
#        return
#    #pre = 0
#    for i in range(n):
#        if arr[i] != pre :
#            pre = arr[i]
#            dfs('',box+[arr[i]])
#dfs(0,[])
#print(res)
